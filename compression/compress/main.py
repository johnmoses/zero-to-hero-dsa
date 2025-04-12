""" 
Compression of data
"""
import zlib

# Original data
data = b"This is an example of data that we want to compress."

# Compress the data
compressed_data = zlib.compress(data)
print("Compressed Data:", compressed_data)

# Decompress the data
decompressed_data = zlib.decompress(compressed_data)
print("Decompressed Data:", decompressed_data.decode())
