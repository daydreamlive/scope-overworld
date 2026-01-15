"""Configuration schema for Waypoint pipeline."""

from typing import ClassVar

from pydantic import Field

from scope.core.pipelines.artifacts import Artifact, HuggingfaceRepoArtifact
from scope.core.pipelines.base_schema import BasePipelineConfig, CtrlInput, ModeDefaults


class WaypointConfig(BasePipelineConfig):
    """Configuration for Waypoint pipeline."""

    pipeline_id = "waypoint"
    pipeline_name = "Waypoint"
    pipeline_description = "A streaming pipeline for Waypoint autoregressive video world models from OverWorld."
    docs_url = "https://github.com/Wayfarer-Labs/world_engine"

    supports_prompts = False 
    supports_cache_management = True

    modes = {"text": ModeDefaults(default=True)}

    artifacts: ClassVar[list[Artifact]] = [
        HuggingfaceRepoArtifact(
            repo_id="OverWorld/Waypoint-Medium-Beta-2026-01-11",
            files=["model.safetensors", "config.yaml"],
        ),
        HuggingfaceRepoArtifact(
            repo_id="OpenWorldLabs/owl_vae_f16_c16_distill_v0_nogan",
            files=[
                "encoder.safetensors",
                "encoder_conf.yml",
                "decoder.safetensors",
                "decoder_conf.yml",
            ],
        ),
        HuggingfaceRepoArtifact(
            repo_id="google/umt5-xl",
            files=[
                "config.json",
                "pytorch_model-00001-of-00002.bin",
                "pytorch_model-00002-of-00002.bin",
                "pytorch_model.bin.index.json",
                "special_tokens_map.json",
                "spiece.model",
                "tokenizer.json",
                "tokenizer_config.json",
            ],
        ),
    ]

    # Controller input support - presence of this field enables controller input capture
    ctrl_input: CtrlInput | None = None

    # Reference images for conditioning (presence enables ImageManager UI)
    images: list[str] | None = Field(
        default=None,
        description="List of reference image paths for conditioning",
    )
