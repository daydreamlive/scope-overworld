# scope-overworld

[Daydream Scope](https://github.com/daydreamlive/scope) plugin providing pipelines for OverWorld ([Wayfarer Labs](https://wayfarerlabs.ai/)) world models.

The plugin uses [world_engine](https://github.com/Wayfarer-Labs/world_engine) under the hood for inference.

> [!IMPORTANT]
> Plugin support is a preview feature in Scope right now and the APIs are subject to breaking change prior to official release.

## Supported Models

- Waypoint-1-Medium-Beta (via the `waypoint` pipeline)

> [!IMPORTANT]
> The Waypoint-1 model is currently in private beta and you must use this [interest form](https://tally.so/r/MeNzW8) to request access.

## Install

Follow the [manual installation](https://github.com/daydreamlive/scope/tree/main?tab=readme-ov-file#manual-installation) (plugin support for the desktop app is not available yet) instructions for Scope.

Install the plugin within the `scope` directory:

```
DAYDREAM_SCOPE_PREVIEW=1 uv run daydream-scope git+https://github.com/daydreamlive/scope-overworld.git
```

Confirm that the plugin is installed:

```
DAYDREAM_SCOPE_PREVIEW=1 uv run daydream-scope plugins
```

Confirm that the `waypoint` pipeline is available:

```
DAYDREAM_SCOPE_PREVIEW=1 uv run daydream-scope pipelines
```

## Usage

### Configure HuggingFace Token

> [!IMPORTANT]
> Scope will only be able to download the model weights for you if you are a part of the Waypoint-1 private beta and your HuggingFace account has access to the model repo.

Configure your `read` HuggingFace [token](https://huggingface.co/docs/hub/en/security-tokens) which will be used for authentication when downloading model weights.

On Windows:

```
set HF_TOKEN=your_token_here
```

On Unix/Linux:

```
export HF_TOKEN=your_token_here
```

### Run Scope

Start the server:

`uv run daydream-scope`

The web frontend will be available at `http://localhost:8000` by default.

## Backlog

- [ ] Configurable mouse sensitivity
- [ ] Text prompt support
- [ ] Additional key mappings


