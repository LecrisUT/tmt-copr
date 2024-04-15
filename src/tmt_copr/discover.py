"""
Discover tmt plugin.

This module provides the `discover.how=copr` plugin.
"""

from __future__ import annotations

import attrs
import tmt
import tmt.utils
from tmt.steps.discover import DiscoverPlugin, DiscoverStepData

__all__ = [
    "DiscoverCopr",
]


@attrs.define
class DiscoverCoprData(DiscoverStepData):
    pass


@tmt.steps.provides_method("copr")
class DiscoverCopr(DiscoverPlugin[DiscoverCoprData]):
    """
    Find all ctest tests.

    Must contain a prepare CMake step.
    """

    _data_class = DiscoverCoprData

    def tests(  # noqa: D102
        self,
        *,
        phase_name: str | None = None,
        enabled: bool | None = None,
    ) -> list[tmt.Test]:
        raise NotImplementedError

    def go(self) -> None:  # noqa: D102
        super().go()
