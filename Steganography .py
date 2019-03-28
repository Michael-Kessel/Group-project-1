# Team Members: Frederick Wittman, Cameron Peete, Nico Shober, Michael Kessel, and Colin Woods
# Dr. Hill
# COSC 2030-01
# 28 March 2019

def ascii_to_bin (message_file):
    
    message = open(message_file, "r")
    line = message.readline()
    a = (bin(int.from_bytes(line.encode(), 'big')))
    b = list(a)
    b.pop(1)
    return b

def binary_to_ascii (binary_number):
    
    binary_number = str(binary_number)
    tmp = int(binary_number, 2)
    a = tmp.to_bytes((tmp.bit_length() + 7) // 8, 'big').decode()
    return a

def hex_to_bin (hex_number):
    
    hex_number = str(hex_number)
    scale = 16
    return bin(int(hex_number, scale))

def bin_to_hex (bin_number):
    
    bin_number = str(bin_number)
    scale = 2
    return hex(int(bin_number, scale))[2:]

def dec_to_hex (dec_number):

    dec_number = str(dec_number)
    scale = 10
    return hex(int(dec_number, scale))[2:]

def hex_to_dec (hex_number):
    
    hex_number = str(hex_number)
    scale = 16
    return int(hex_number, scale)
             
def encode (in_file, out_file, message_file):
    
    # Open base pixel file, write file, and message file
    infile = open(in_file, "r")
    outfile = open(out_file, "w")
    messageFile = open(message_file, "r")
    
    # Declare lists to store the pixels and the secret message as binary numbers, get and declare the secret message as 
    # a variable, and declare an index variable
    pixels = []
    message = ascii_to_bin(message_file)
    message_length = len(message)
    i = 1

    # Store the pixels in a list.  See the documentation for the reason why our team opted to store the array as a list
    for line in infile:
        pixels.append(line[2:])
    
    # Store message size and pixel overflow in first pixel
    
    first_line = list(pixels[0])
    message_length_hex = dec_to_hex(str(message_length))
    tmp = message_length_hex.zfill(2)
    message_length_hex = list(tmp)
    first_line[2] = message_length_hex[0]
    first_line[3] = message_length_hex[1]
    
    if (message_length > len(pixels)):
        overflow = dec_to_hex(str(message_length - len(pixels)))
        tmp = overflow.zfill(2)
        overflow = list(tmp)
    
    else:
        overflow = ['0', '0']
        
    first_line[4] = overflow[0]
    first_line[5] = overflow[1]
    first_line = "".join(first_line)
    
    pixels[0] = first_line
    
    # Cycle through the pixels in the order r, g, b.  Modify the least significant bit of each pixel to match the corresponding
    # secret message bit.  Reinsert the modified pixel value and write to the output file
    
    for line in pixels:
        if(len(message) > 0):
            line_as_list = list(line)
            binary_array = list(hex_to_bin(str(line_as_list[i])))
            binary_array.pop()
            binary_array.append(message.pop(0))
            tmp = "".join(binary_array)
            tmp = bin_to_hex(tmp)
            line_as_list[i] = tmp
                
        tmp = "".join(line_as_list)
        tmp = "ff" + tmp
        outfile.write(tmp)
        i = (i + 2) % 6
        
def decode (encoded_message, message_file):
    
    # Open encoded file and message file
    infile = open(encoded_message, "r")
    outfile = open(message_file, "w")
    
    # Declare an index variable, a count variable, and an array to store the secret message in bit form
    i = 1
    count = 0
    message = []
    
    # Cycle through the pixels in the encoded file in the order r, g, b.  Store the least significant bit of each pixel in an 
    # array
    for line in infile:
        if count == 0:
            message_length = hex_to_dec(line[4:6])
            overflow = hex_to_dec(line[6:8])   
            
        line_as_list = list(line[2:])
        binary_array = list(hex_to_bin(line_as_list[i]))[2:]
        message.append(binary_array.pop())
        i = (i + 2) % 6
        count = count + 1
        
        if count == message_length:
            break
    
    # Convert the list of binary values to a string of letters and write to the output file
    tmp = "".join(message)
    tmp1 = tmp[0] + "b" + tmp[1:]
    outfile.write("The secret message is: " + binary_to_ascii(tmp1))
        
    outfile.write("\n" + "The secret message consisted of " + str(message_length) + " bits. \nThere were " + str(overflow) + " bits of information excluded from the message for lack of pixels to store them in.")

# encode("pixel_in.txt", "pixel_out.txt", "message_in.txt") 
# decode("pixel_out.txt", "message_out.txt")

