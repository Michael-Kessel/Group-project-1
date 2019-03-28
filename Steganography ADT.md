# ADT Summary

This abstract data type encodes a secret message in bit-map image files.  After encryption, the image file is indistinguishable from an ordinary list of pixels.  Another major feature is 

# Data Items and Operations

## Data Items

This steganography ADT does not include any global variables.  Major local variables in the operations encode and decode include:

#### message
message is a sequentially ordered list of the bits that correspond to the ASCII characters of the secret message.

#### line_as_list
line_as_list stores pixels, which are strings, as sequentially ordered lists

#### binary_array
binary_array is a sequentially ordered list that stores the binary value of individual hexidecimal characters.

## Operations

#### ascii_to_bin (message_file)
Parameter: a text file
ascii_to_bin reads a line from its parameter and returns the line's contents as a list of binary numbers.  The list of binary numbers corresponds to the appropriate ASCII characters.  The core of the ascii_to_bin function is the from_bytes function.

#### binary_to_ascii (binary_number)
Parameter: a string
binary_to_ascii takes a string of binary numbers as its parameter and returns a string of the corresponding ASCII characters.  The core of the binary_to_ascii function is the from_bytes function.

#### hex_to_bin (hex_number)
Parameter: a string
hex_to_bin takes a hexidecimal number, cast as a string, and returns a binary number cast as a string.

#### bin_to_hex (bin_number)
Parameter: a string
bin_to_hex takes a binary number, cast as a string, and returns a hexidecimal number cast as a string.

#### dec_to_hex (dec_number)
Parameter: a string
dec_to_hex takes a decimal number, cast as a string, and returns a hexidecimal number cast as a string.

#### hex_to_dec (hex_number):
Parameter: a string
hex_to_dec takes a hexidecimal number, cast as a string, and returns a decimal number cast as a string. 



