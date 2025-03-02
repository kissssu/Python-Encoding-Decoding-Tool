# Python Encoding/Decoding Tool

This script is a command-line tool for encoding and decoding strings using various encoding schemes, including Base64, Base32, Base16, Base8 (Octal), and URL encoding. It simplifies encoding and decoding operations with straightforward arguments.

## Features

* Supports Base64, Base32, Base16, Base8 (Octal), and URL encoding schemes.
* Allows both encoding and decoding operations.
* Case-insensitive input for encode/decode flags.
* Improved error handling with informative messages.
* User-friendly interface with clear instructions and examples.
* Lightweight and portable Python script.
* Help message when the script is called incorrectly.

## Requirements

Python 3.x

## How to Run

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/kissssu/Python-Encoding-Decoding-Tool.git
    cd Python-Encoding-Decoding-Tool
    ```
    
2.  **Make the Script Executable:**
    ```bash
    chmod +x encoder_tool.py
    ```
    (chmod +x encoder_tool.py - chmod +x encoder_tool.py (make the file executable))

3.  **Run the Script:**
    ```bash
    python3 encoder_tool.py -h
    ```

## Usage

Run the script using the command line with the following structure:

```bash
python3 encoder_tool.py [BASE] [ACTION] [STRING]
```

## Arguments:

#### BASE:
- -b64 or --base64: Use Base64 encoding.
- -b32 or --base32: Use Base32 encoding.
- -b16 or --base16: Use Base16 encoding.
- -b8 or --base8: Use Base8 (Octal) encoding.
- -u or --url: Use URL encoding.

#### ACTION:
- -e or --encode: Encode the provided string.
- -d or --decode: Decode the provided string.

#### STRING:
- The text to encode or decode (must be a valid string for the operation).

## Output:
```bash
python3 encoder_tool.py -h 
```
```
usage: encoder_tool.py -b64/-b32/-b16/-b8/-u -e/-d cipher

Tool used to encode/decode in base64, base32, base16, base8 & URL.

positional arguments:
  cipher          The string to encode or decode

options:
  -h, --help      show this help message and exit
  -v, --version   show program's version number and exit
  -b64, --base64  Use Base64 encoding
  -b32, --base32  Use Base32 encoding
  -b16, --base16  Use Base16 encoding
  -b8, --base8    Use Base8 encoding (Octal)
  -u, --url       Use URL encoding
  -e, --encode    Encode the input
  -d, --decode    Decode the input

Example: encoder_tool.py --base64 -e 'Kissu is the best.'
```

## Error Handling
- **Missing Arguments**: If any required arguments (base, action, string) are missing, the script prints the help message.
- **Invalid Encoded String**: Ensure the input for decoding is a valid encoded string to avoid runtime errors. The script now provides more specific error messages for invalid input.

## Version
```
1.2
```

## Future Enhancements
- **Input/Output from Files**: The ability to read the input from a file and write the output to a file.
- **Default Encoding**: If no -e or -d is specified, encoding will be the default behavior.
- **Short Flags**: Shorter aliases for the flags (e.g., -64 for --base64).
- **More Encoding Options**: Adding support for other encoding schemes.
- **Interactive Mode**: A mode where the user can repeatedly enter strings to encode or decode without re-running the script.
- **Batch Processing**: The ability to encode or decode multiple strings at once.

## Notes
The script is for educational purposes. Ensure to use a valid string for encoding and decoding to avoid unexpected behavior. Base8 (Octal) encoding uses ASCII values in octal format, and decoding expects a properly formatted string of octal values.
