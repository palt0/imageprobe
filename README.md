# imageprobe

Asynchronous library to get image dimensions by fetching as little data as possible.

It temporarily supports only GIF, PNG because development is still in a very early stage.

## Usage

To install this library, run:

    pip install imageprobe

The `probe()` function returns metadata of an image from an URL, or throws an exception if an error occurred.

```python
import asyncio
from imageprobe import probe

loop = asyncio.get_event_loop()
url = "https://upload.wikimedia.org/wikipedia/commons/7/70/Example.png"
image_data = loop.run_until_complete(probe(url))
print(image_data.width, image_data.height)

# 172 178
```

## Contributing

I won't accept pull requests until the first beta release.
