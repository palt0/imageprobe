from __future__ import annotations

from types import TracebackType
from typing import Optional, Type

import aiohttp

from imageprobe.errors import DownloadError


class DownloadClient:
    def __init__(self, url: str) -> None:
        self.url = url
        self.buffer = b""
        self._cs: aiohttp.ClientSession
        self._response: aiohttp.ClientResponse

    @property
    def bytes_read(self) -> int:
        return len(self.buffer)

    async def __aenter__(self) -> DownloadClient:
        self._cs = aiohttp.ClientSession()
        try:
            self._response = await self._cs.get(self.url)
            return self
        except aiohttp.ClientError as exc:
            await self._cs.close()
            raise DownloadError(self.url, self.bytes_read) from exc

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: TracebackType,
    ) -> None:
        await self._response.release()
        await self._cs.close()

    async def read(self, nr_bytes: int) -> None:
        try:
            self.buffer += await self._response.content.read(nr_bytes)
        except aiohttp.ClientError as exc:
            await self._response.release()
            await self._cs.close()
            raise DownloadError(self.url, self.bytes_read) from exc

    async def read_from_start(self, nr_bytes: int) -> None:
        bytes_diff = nr_bytes - self.bytes_read
        if bytes_diff:
            await self.read(bytes_diff)
