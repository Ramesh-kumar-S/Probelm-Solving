import struct

"""

Little-endian: The least significant byte is stored at the lowest memory address.

Big-endian: The most significant byte is stored at the lowest memory address.

Using these methods, you can easily determine the endianness of a machine in different programming languages. The concept remains the same: inspect the bytes of a multi-byte data type to see how they are ordered in memory.
"""


def check_endianness():
    x = 1
    # Pack the integer as bytes
    packed = struct.pack('I', x)
    # Check the first byte
    if packed[0] == 1:
        print("Little-endian")
    else:
        print("Big-endian")


check_endianness()
