import aiohttp
import pytest

import imageprobe.parser as parser
from imageprobe.errors import DownloadError
from imageprobe.types import ImageData

pytestmark = pytest.mark.remote


@pytest.mark.asyncio
async def test_e2e_valid_gif():
    url = "https://upload.wikimedia.org/wikipedia/commons/0/0e/Bin_sample.gif"
    image_data = await parser.probe(url)
    assert image_data == ImageData(120, 40, "gif", "image/gif")


@pytest.mark.asyncio
async def test_e2e_valid_png():
    url = "https://upload.wikimedia.org/wikipedia/commons/7/70/Example.png"
    image_data = await parser.probe(url)
    assert image_data == ImageData(172, 178, "png", "image/png")


@pytest.mark.slow
@pytest.mark.asyncio
async def test_e2e_invalid_url():
    url = "http://tina.e.gemma.com/"
    with pytest.raises(DownloadError) as excinfo:
        await parser.probe(url)
    assert excinfo.value.bytes_read == 0


@pytest.mark.asyncio
async def test_e2e_external_client_session():
    url = "https://upload.wikimedia.org/wikipedia/commons/7/70/Example.png"
    async with aiohttp.ClientSession() as session:
        image_data = await parser.probe(url, session)
        assert image_data == ImageData(172, 178, "png", "image/png")
