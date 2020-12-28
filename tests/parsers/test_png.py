import pytest

from imageprobe.parsers import png
from imageprobe.types import ImageData


@pytest.mark.asyncio
async def test_valid_png(probe_local_img):
    image_data, bytes_read = await probe_local_img("tests/fxt_data/sample.png", png.png)
    assert image_data == ImageData(172, 178, "png", "image/png")
    assert bytes_read == 24
