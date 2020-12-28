from typing import Awaitable, Callable, Optional, Tuple

import pytest

from imageprobe.client import DownloadClient
from imageprobe.types import ImageData
from tests.mocks.mock_client import MockDownloadClient

ParserFunc = Callable[[DownloadClient], Awaitable[Optional[ImageData]]]


@pytest.fixture
async def probe_local_img():
    async def _probe_local_img(
        filepath: str, parser: ParserFunc
    ) -> Tuple[Optional[ImageData], int]:
        async with MockDownloadClient(filepath) as client:
            image_data = await parser(client)
            bytes_read = client.bytes_read
        return image_data, bytes_read

    return _probe_local_img
