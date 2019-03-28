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

#### encode (in_file, out_file, message_file)
* Parameters: a bit-map image as a read file, an empty text file to write the encoded pixels to, and a single-line message as a read file.
* Pseudocode:
  1. Write the lines of the image file to a list.  Originally, our team performed operations on the data taken from the image file and    wrote the output directly to the out-file.  We opted to store the pixels in an array because we felt it would make the ADT amenable to more sophisticated encryption techniques, moving forward.
  2. Store the secret message as a list of bits corresponding to the ASCII characters.
  3. Modify the image file's first pixel's green and blue pixels to contain the length of the message and the amount of overflow in bits, respectively.
  4. With use of an index variable, cycle through the red, green, and blue elements for each new pixel.  Change the least significant bit of the appropriate hexidecimal character to match the corresponding bit in the secret message.
  5. Write the altered pixels to the out-file.

#### decode (encoded_message, message_file)
* Parameters: an image file that contains the secret message and a text file to write the message to
* Pseudocode:
  1. Read the first pixel of the encoded message and declare the length of the message and degree of overflow as variables.
  2. With use of an index variables to point to the appropriate pixel element and to stop reading at the end of the secret message, read through the file and add the bits that correspond to the ASCII characters to a list.
  3. Translate the bits to ASCII characters and write the secret message to the out-file.
  4. Write the length of the message in bits and the degree of overflow in bits to the out-file.

#### ascii_to_bin (message_file)
* Parameter: a text file
* ascii_to_bin reads a line from its parameter and returns the line's contents as a list of binary numbers.  The list of binary numbers corresponds to the appropriate ASCII characters.  The core of the ascii_to_bin function is the from_bytes function.

#### binary_to_ascii (binary_number)
* Parameter: a string
* binary_to_ascii takes a string of binary numbers as its parameter and returns a string of the corresponding ASCII characters.  The core of the binary_to_ascii function is the from_bytes function.

#### hex_to_bin (hex_number)
* Parameter: a string
* hex_to_bin takes a hexidecimal number, cast as a string, and returns a binary number cast as a string.

#### bin_to_hex (bin_number)
* Parameter: a string
* bin_to_hex takes a binary number, cast as a string, and returns a hexidecimal number cast as a string.

#### dec_to_hex (dec_number)
* Parameter: a string
* dec_to_hex takes a decimal number, cast as a string, and returns a hexidecimal number cast as a string.

#### hex_to_dec (hex_number):
* Parameter: a string
* hex_to_dec takes a hexidecimal number, cast as a string, and returns a decimal number cast as a string. 

# Example
Please use the included text files to test the steganography ADT.  They showcase the efficacy of the ADT and its overflow and message length features.  Consider the functions that follow:

```encode("pixel_in.txt", "pixel_out.txt", "message_in.txt")``` 

```decode("pixel_out.txt", "message_out.txt")```

Below is a comparison of sections of the image file before and after the secret message has been encoded:

![alt text](https://github.com/frederickwittman95/Group-project-1/blob/master/before_encode.PNG "Logo Title Text 1")
![alt text](https://github.com/frederickwittman95/Group-project-1/blob/master/before_encode.PNG "Logo Title Text 1")



