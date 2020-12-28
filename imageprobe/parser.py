from typing import Optional

from imageprobe.client import DownloadClient
from imageprobe.parsers import ordered_parsers as parsers
from imageprobe.types import ImageData


async def probe(url: str) -> Optional[ImageData]:
    """Download as little data as possible to determine the dimensions of an image.

    Args:
        url (str): Image URL.

    Raises:
        DownloadError: Image wasn't downloaded successfully.
        FormatError: Image is corrupted.

    Returns:
        Optional[ImageData]: Object containing image metadata. Defaults to None if the
            format is unrecognized.
    """
    async with DownloadClient(url) as client:
        image_data: Optional[ImageData] = None
        for parser in parsers:
            image_data = await parser(client)
            if image_data is not None:
                break
        return image_data
