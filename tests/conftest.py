import asyncio
import sys

import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--full",
        action="store_true",
        default=False,
        help="Enable slow tests",
    )


def pytest_configure(config):
    if not config.option.full and not config.option.markexpr:
        config.option.markexpr = "not slow"


# Workaround for known issue of aiohttp on Windows / Python 3.8+
# See: https://github.com/aio-libs/aiohttp/issues/4324
@pytest.fixture
def event_loop():
    if (
        sys.version_info[0] == 3
        and sys.version_info[1] >= 8
        and sys.platform == "win32"
    ):
        loop = asyncio.SelectorEventLoop()
    else:
        loop = asyncio.new_event_loop()

    yield loop
    loop.close()
