from types import TracebackType
from typing import IO, Optional, Type

from imageprobe.client import DownloadClient
from imageprobe.errors import DownloadError


class MockDownloadClient(DownloadClient):
    def __init__(self, filepath: str) -> None:
        self._filepath = filepath
        self._file_stream: IO[bytes]
        super().__init__(f"file://{filepath}")

    async def __aenter__(self) -> "MockDownloadClient":
        try:
            self._file_stream = open(self._filepath, "rb")
            return self
        except IOError as exc:
            raise DownloadError(self.url, self.bytes_read) from exc

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: TracebackType,
    ) -> None:
        self._file_stream.close()

    async def read(self, nr_bytes: int) -> None:
        old_buflen = self.bytes_read
        self.buffer += self._file_stream.read(nr_bytes)

        if self.bytes_read - old_buflen < nr_bytes:
            self._file_stream.close()
            raise DownloadError(self.url, self.bytes_read)
