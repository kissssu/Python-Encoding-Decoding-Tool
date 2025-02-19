#!/usr/bin/python3

import argparse
import base64

parser = argparse.ArgumentParser(
    description="Tool used to encode/decode in base64, base32, base16 & base8.",
    usage="%(prog)s -b64/-b32/-b16/-b8 -e/-d cipher",
    epilog="Example: %(prog)s --base64 -e 'Kissu is the best.'"
)

parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.1')  # Updated version

parser.add_argument('-b64', '--base64', action='store_true', help='Use Base64 encoding')
parser.add_argument('-b32', '--base32', action='store_true', help='Use Base32 encoding')
parser.add_argument('-b16', '--base16', action='store_true', help='Use Base16 encoding')
parser.add_argument('-b8', '--base8', action='store_true', help='Use Base8 encoding (Octal)')
parser.add_argument('-e', '--encode', action='store_true', help='Encode the input')
parser.add_argument('-d', '--decode', action='store_true', help='Decode the input')
parser.add_argument('cipher', type=str, help='The string to encode or decode')

args = parser.parse_args()

def process_base64(data, encode):
    if encode:
        return base64.b64encode(data.encode()).decode()
    else:
        try:  # Handle potential decode errors
            return base64.b64decode(data).decode()
        except base64.binascii.Error:
            return "Decoding error: Invalid Base64 input."  # More helpful message

def process_base32(data, encode):
    if encode:
        return base64.b32encode(data.encode()).decode()
    else:
        try:
            return base64.b32decode(data).decode()
        except base64.binascii.Error:
            return "Decoding error: Invalid Base32 input."

def process_base16(data, encode):
    if encode:
        return base64.b16encode(data.encode()).decode()
    else:
        try:
            return base64.b16decode(data).decode()
        except base64.binascii.Error:
            return "Decoding error: Invalid Base16 input."

def process_base8(data, encode):
    if encode:
        return ''.join(format(ord(char), 'o') for char in data)
    else:
        try:
            octal_chars = [data[i:i+3] for i in range(0, len(data), 3)]
            return ''.join(chr(int(oct_char, 8)) for oct_char in octal_chars)
        except ValueError: # Handle potential decode errors
            return "Decoding error: Invalid Base8/Octal input."


# Case-insensitive flag handling:
operation = None
if args.encode:
    operation = "encode"
elif args.decode:
    operation = "decode"

if operation is None:
    parser.error("Please specify either -e (encode) or -d (decode).")

base_selected = False
if args.base64:
    base = "base64"
    base_selected = True
elif args.base32:
    base = "base32"
    base_selected = True
elif args.base16:
    base = "base16"
    base_selected = True
elif args.base8:
    base = "base8"
    base_selected = True

if not base_selected:
    parser.error("Please specify a base encoding (-b64, -b32, -b16, or -b8).")


if operation == "encode":
    encode_flag = True
else:
    encode_flag = False

if base == "base64":
    result = process_base64(args.cipher, encode_flag)
elif base == "base32":
    result = process_base32(args.cipher, encode_flag)
elif base == "base16":
    result = process_base16(args.cipher, encode_flag)
elif base == "base8":
    result = process_base8(args.cipher, encode_flag)

print(result)
