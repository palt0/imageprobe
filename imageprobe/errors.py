class DownloadError(Exception):
    """Download error"""

    def __init__(self, url: str, bytes_read: int) -> None:
        self.url = url
        self.bytes_read = bytes_read
        message = f'url: "{url}", {bytes_read} bytes read'
        super().__init__(message)


class FormatError(Exception):
    """Parsing error"""
