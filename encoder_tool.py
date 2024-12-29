#!/usr/bin/python3

import argparse
import base64

# Setting up the Argument Parser
parser = argparse.ArgumentParser(
    description="Tool used to encode/decode in base64, base32, base16 & base8.",
    usage="%(prog)s -b64/-b32/-b16/-b8 -e/-d cipher",
    epilog="Example: %(prog)s --base64 -e 'Kissu is the best.'"
)

# Adding version argument (-v or --version)
parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')

# Adding arguments to the parser for the base encoding and the operation (encode/decode)
parser.add_argument('-b64', '--base64', action='store_true', help='Use Base64 encoding')
parser.add_argument('-b32', '--base32', action='store_true', help='Use Base32 encoding')
parser.add_argument('-b16', '--base16', action='store_true', help='Use Base16 encoding')
parser.add_argument('-b8', '--base8', action='store_true', help='Use Base8 encoding (Octal)')
parser.add_argument('-e', '--encode', action='store_true', help='Encode the input')
parser.add_argument('-d', '--decode', action='store_true', help='Decode the input')
parser.add_argument('cipher', type=str, help='The string to encode or decode')

# Parse the arguments
args = parser.parse_args()

# Function to handle Base64 encoding/decoding
def process_base64(data, encode):
    if encode:
        return base64.b64encode(data.encode()).decode()
    else:
        return base64.b64decode(data).decode()

# Function to handle Base32 encoding/decoding
def process_base32(data, encode):
    if encode:
        return base64.b32encode(data.encode()).decode()
    else:
        return base64.b32decode(data).decode()

# Function to handle Base16 encoding/decoding
def process_base16(data, encode):
    if encode:
        return base64.b16encode(data.encode()).decode()
    else:
        return base64.b16decode(data).decode()

# Function to handle Base8 (Octal) encoding/decoding
def process_base8(data, encode):
    if encode:
        return ''.join(format(ord(char), 'o') for char in data)
    else:
        octal_chars = [data[i:i+3] for i in range(0, len(data), 3)]
        return ''.join(chr(int(oct_char, 8)) for oct_char in octal_chars)

# Check which base and operation to perform
if args.base64:
    result = process_base64(args.cipher, args.encode)
elif args.base32:
    result = process_base32(args.cipher, args.encode)
elif args.base16:
    result = process_base16(args.cipher, args.encode)
elif args.base8:
    result = process_base8(args.cipher, args.encode)
else:
    raise ValueError("No valid base format selected.")

# Output the result
print(result)