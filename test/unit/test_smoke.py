from importlib.metadata import version

import tmt_copr


def test_version() -> None:
    assert tmt_copr.__version__ == version("tmt-copr")
