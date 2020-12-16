import pytest

import imageprobe.parser as parser
from imageprobe.types import ImageData


@pytest.mark.asyncio
async def test_e2e_valid_png():
    url = "https://upload.wikimedia.org/wikipedia/commons/7/70/Example.png"
    image_data = await parser.probe(url)
    assert image_data == ImageData(172, 178, "png", "image/png")
