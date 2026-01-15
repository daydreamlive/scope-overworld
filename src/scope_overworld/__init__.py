"""OverWorld plugin for Daydream Scope."""

import scope.core

from .pipeline import WaypointPipeline


@scope.core.hookimpl
def register_pipelines(register):
    register(WaypointPipeline)


__all__ = ["WaypointPipeline"]
