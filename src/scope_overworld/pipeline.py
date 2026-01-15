from typing import TYPE_CHECKING

import torch
from torchvision.io import read_image

from scope.core.config import get_model_file_path
from scope.core.pipelines.controller import CtrlInput, convert_to_win_keycodes
from scope.core.pipelines.interface import Pipeline
from world_engine import WorldEngine, CtrlInput as WorldCtrlInput

from .schema import WaypointConfig

if TYPE_CHECKING:
    from scope.core.pipelines.schema import BasePipelineConfig


class WaypointPipeline(Pipeline):
    @classmethod
    def get_config_class(cls) -> type["BasePipelineConfig"]:
        return WaypointConfig

    def __init__(
        self,
        prompt: str = "A fun game",
        n_frames: int = 4096,
        device: torch.device | None = None,
        dtype: torch.dtype = torch.bfloat16,
        warmup_frames: int = 3,
        **kwargs,
    ):
        self.device = (
            device
            if device is not None
            else torch.device("cuda" if torch.cuda.is_available() else "cpu")
        )
        self.dtype = dtype

        # Build local model paths from DAYDREAM_SCOPE_MODELS_DIR
        model_path = str(get_model_file_path("Waypoint-Medium-Beta-2026-01-11"))
        ae_path = str(get_model_file_path("owl_vae_f16_c16_distill_v0_nogan"))
        prompt_encoder_path = str(get_model_file_path("umt5-xl"))

        self.engine = WorldEngine(
            model_path,
            ae_uri=ae_path,
            prompt_encoder_uri=prompt_encoder_path,
            device=self.device,
            dtype=self.dtype,
            model_config_overrides={
                "n_frames": n_frames,
            },
        )
        self.engine.set_prompt(prompt)
        # Track current prompt to avoid redundant encoding
        self._current_prompt: str | None = prompt

        self._warmup(warmup_frames)

    def _warmup(self, n_frames: int) -> None:
        """Run warmup frames to trigger JIT compilation."""
        for _ in range(n_frames):
            self.engine.gen_frame(ctrl=WorldCtrlInput())

    def __call__(self, **kwargs) -> torch.Tensor:
        """Generate a frame with controller input.

        Args:
            ctrl_input: CtrlInput with W3C button codes and mouse velocity
            prompts: List of prompt dicts with "text" key (uses first one)
            init_cache: If True, reset engine state

        Returns:
            torch.Tensor: Frame in THWC format (1, H, W, 3) in [0, 1] range
        """
        manage_cache = kwargs.get("manage_cache", False)
        init_cache = kwargs.get("init_cache", False)
        images = kwargs.get("images")
        prompts = kwargs.get("prompts")

        if manage_cache and images and len(images) > 0:
            init_cache = True

        if init_cache:
            self.engine.reset()

        # Handle image conditioning
        if images and len(images) > 0:
            # Read image from path and convert to uint8 HWC
            image = read_image(images[0])  # CHW uint8
            image = image.permute(1, 2, 0)  # HWC uint8
            self.engine.append_frame(image)

        # Handle prompt changes
        if prompts and len(prompts) > 0:
            first_prompt = prompts[0]
            # Prompts can be strings or dicts with "text" key
            new_prompt = (
                first_prompt["text"] if isinstance(first_prompt, dict) else first_prompt
            )
            if new_prompt != self._current_prompt:
                self.engine.set_prompt(new_prompt)
                self._current_prompt = new_prompt

        # Get controller input (scope's CtrlInput with W3C codes)
        ctrl_input: CtrlInput = kwargs.get("ctrl_input") or CtrlInput()

        # Convert W3C codes to Windows Virtual Keycodes for world_engine
        win_keys = convert_to_win_keycodes(ctrl_input)
        ctrl = WorldCtrlInput(button=win_keys, mouse=ctrl_input.mouse)

        frame = self.engine.gen_frame(ctrl=ctrl)
        return frame.unsqueeze(0).float() / 255.0
