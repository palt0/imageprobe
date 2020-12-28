import pytest

from imageprobe.parsers import gif
from imageprobe.types import ImageData


@pytest.mark.asyncio
async def test_valid_gif(probe_local_img):
    image_data, bytes_read = await probe_local_img("tests/fxt_data/sample.gif", gif.gif)
    assert image_data == ImageData(120, 40, "gif", "image/gif")
    assert bytes_read == 10
