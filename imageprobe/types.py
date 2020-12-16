from dataclasses import dataclass


@dataclass(frozen=True)
class ImageData:
    width: int
    height: int
    extension: str
    mime_type: str
    w_units: str = "px"
    h_units: str = "px"
