from imageprobe.parsers import png

# Parsers are ordered from the ones that require the least amount of data onwards.
ordered_parsers = [
    png.png,  # 24 bytes
]
