import struct
from typing import Optional

from imageprobe.client import DownloadClient
from imageprobe.errors import FormatError
from imageprobe.types import ImageData


async def gif(client: DownloadClient) -> Optional[ImageData]:
    # Validate GIF signature
    await client.read_from_start(6)
    if client.buffer[:6] not in (b"GIF87a", b"GIF89a"):
        return None

    # Fetch dimensions
    await client.read_from_start(10)
    try:
        width, height = struct.unpack("<HH", client.buffer[6:10])
    except struct.error as exc:
        raise FormatError("Invalid GIF file") from exc

    return ImageData(
        width=width,
        height=height,
        extension="gif",
        mime_type="image/gif",
    )
