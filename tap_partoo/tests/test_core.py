"""Tests standard tap features using the built-in SDK tests library."""

import json
from pathlib import Path

from singer_sdk.testing import get_standard_tap_tests

from tap_partoo.tap import TapPartoo

with open(Path(__file__).parents[2] / ".secrets/config.dev.json") as f:
    SAMPLE_CONFIG = json.load(f)


# Run standard built-in tap tests from the SDK:
def test_standard_tap_tests():
    """Run standard tap tests from the SDK."""
    tests = get_standard_tap_tests(TapPartoo, config=SAMPLE_CONFIG)
    for test in tests:
        test()


# TODO: Create additional tests as appropriate for your tap.
