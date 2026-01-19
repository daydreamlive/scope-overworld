# scope-overworld

[![Discord](https://img.shields.io/badge/Discord-5865F2?logo=discord&logoColor=white)](https://discord.gg/mnfGR4Fjhp)

<img width="1902" height="911" alt="Screenshot 2026-01-15 153408" src="https://github.com/user-attachments/assets/3ba71d58-e5c8-4fa7-94d0-ed3673692a82" />

[Scope](https://github.com/daydreamlive/scope) plugin providing pipelines for OverWorld ([Wayfarer Labs](https://wayfarerlabs.ai/)) world models.

The plugin uses [world_engine](https://github.com/Wayfarer-Labs/world_engine) under the hood for inference.

> [!IMPORTANT]
> Plugin support is a preview feature in Scope right now and the APIs are subject to breaking change prior to official release.
> Be sure to be running v0.1.0-beta.3+

## Supported Models

- Waypoint-1-Medium-Beta (via the `waypoint` pipeline)

> [!IMPORTANT]
> The Waypoint-1 model is currently in private beta and you must use this [interest form](https://tally.so/r/MeNzW8) to request access.

## Install

Follow the [manual installation](https://github.com/daydreamlive/scope/tree/main?tab=readme-ov-file#manual-installation) (plugin support for the desktop app is not available yet) instructions for Scope.

Install the plugin within the `scope` directory:

```
DAYDREAM_SCOPE_PREVIEW=1 uv run daydream-scope install git+https://github.com/daydreamlive/scope-overworld.git
```

Confirm that the plugin is installed:

```
DAYDREAM_SCOPE_PREVIEW=1 uv run daydream-scope plugins
```

Confirm that the `waypoint` pipeline is available:

```
DAYDREAM_SCOPE_PREVIEW=1 uv run daydream-scope pipelines
```

## Upgrade

Upgrade the plugin to the latest version:

```
DAYDREAM_SCOPE_PREVIEW=1 uv run daydream-scope install --upgrade git+https://github.com/daydreamlive/scope-overworld.git
```

## Usage

### Configure HuggingFace Token

> [!IMPORTANT]
> Scope will only be able to download the model weights for you if you are a part of the Waypoint-1 private beta and your HuggingFace account has access to the model repo.

Configure your `read` HuggingFace [token](https://huggingface.co/docs/hub/en/security-tokens) which will be used for authentication when downloading model weights.

On Windows Command Prompt:

```
set HF_TOKEN=your_token_here
```

On Windows Powershell

```
$env:HF_TOKEN="your_token_here"
```

On Unix/Linux:

```
export HF_TOKEN=your_token_here
```

### Run Scope

Start the server:

`uv run daydream-scope`

The web frontend will be available at `http://localhost:8000` by default.

The `waypoint` pipeline will be available in:
- The frontend under the Pipeline ID dropdown in the Settings panel.
- The [API](https://github.com/daydreamlive/scope/blob/main/docs/server.md) by [loading the pipeline](https://github.com/daydreamlive/scope/blob/main/docs/api/load.md#load-a-pipeline) using the `waypoint` pipeline ID. If you are not using the frontend, `uv run download_models --pipeline waypoint` can be used to download the model weights first.

Once you download the model, it takes about 20 mins for the model to be ready. Go make some tea, come back, and have fun!

## Backlog

- [ ] Configurable mouse sensitivity
- [ ] Text prompt support
- [ ] Additional key mappings








