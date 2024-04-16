"""
Discover tmt plugin.

This module provides the `discover.how=copr` plugin.
"""

from __future__ import annotations

import dataclasses
from typing import TYPE_CHECKING

import tmt
import tmt.utils
from tmt.steps.discover import DiscoverPlugin, DiscoverStepData

if TYPE_CHECKING:
    from typing import Literal

    from tmt.steps import Step

__all__ = [
    "DiscoverCopr",
]


@dataclasses.dataclass
class DiscoverCoprData(DiscoverStepData):
    packages: list[str] = tmt.utils.field(
        option=("-p", "--package"),
        default_factory=list,
        metavar="PACKAGE",
        multiple=True,
        help="Fedora packages",
        normalize=tmt.utils.normalize_string_list,
    )
    downstream: Literal["fedora"] = tmt.utils.field(
        option="--downstream",
        default="fedora",
        choices=[
            "fedora",
        ],
        metavar="DOWNSTREAM",
        help="Downstream distgit to build from",
    )


@tmt.steps.provides_method("copr")
class DiscoverCopr(DiscoverPlugin[DiscoverCoprData]):
    """
    Generate copr tests.

    Main interface for creating copr tests.
    """

    _data_class = DiscoverCoprData
    _tests: list[tmt.Test]

    def __init__(  # noqa: D107
        self,
        *,
        step: Step,
        data: DiscoverCoprData,
        workdir: tmt.utils.WorkdirArgumentType = None,
        logger: tmt.log.Logger,
    ) -> None:
        super().__init__(step=step, data=data, workdir=workdir, logger=logger)
        self._tests = []

    def tests(  # noqa: D102
        self,
        *,
        phase_name: str | None = None,  # noqa: ARG002
        enabled: bool | None = None,  # noqa: ARG002
    ) -> list[tmt.Test]:
        return self._tests

    def go(self) -> None:  # noqa: D102
        for package in self.data.packages:
            test = tmt.Test.from_dict(
                name=f"/{package}",
                logger=self._logger,
                mapping={
                    "framework": "copr",
                    "downstream": self.data.downstream,
                    # TODO: Handle `test` more specifically
                    "test": "",
                },
            )
            self._tests.append(test)
