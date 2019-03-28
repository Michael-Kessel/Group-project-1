# ADT Summary

This abstract data type encodes a secret message in bit-map image files.  After encryption, the image file is indistinguishable from an ordinary list of pixels.  Another major feature is 

# Data Items and Operations

## Data Items

This steganography ADT does not include any global variables.  The local variables in the operations encode and decode include:

#### message
message is a sequentially ordered list of the bits the correspond to the ASCII characters of the secret message.

### line_as_list

