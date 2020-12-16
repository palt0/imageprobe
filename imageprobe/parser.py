from typing import Optional

from imageprobe.client import DownloadClient
from imageprobe.parsers import ordered_parsers as parsers
from imageprobe.types import ImageData


async def probe(url: str) -> Optional[ImageData]:
    async with DownloadClient(url) as client:
        image_data: Optional[ImageData] = None
        for parser in parsers:
            image_data = await parser(client)
            if image_data is not None:
                break
        return image_data
