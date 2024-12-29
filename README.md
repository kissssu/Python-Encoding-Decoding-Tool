# Python Encoding/Decoding Tool
This script is a command-line tool for encoding and decoding strings using various encoding schemes, including Base64, Base32, Base16, and Base8 (Octal). It simplifies encoding and decoding operations with straightforward arguments.

## Features
- Supports Base64, Base32, Base16, and Base8 (Octal) encoding schemes.
- Allows both encoding and decoding operations.
- User-friendly interface with clear instructions and examples.
- Lightweight and portable Python script.

## Requirements
- Python 3.x

## Usage 
- Run the script using the command line with the following structure:
```bash
python3 encoder_tool.py [BASE] [ACTION] [STRING]
```
### Arguments:
1. BASE:
- ```-b64``` or ```--base64```: Use Base64 encoding.
- ```-b32``` or ```--base32```: Use Base32 encoding.
- ```-b16``` or ```--base16```: Use Base16 encoding.
- ```-b8``` or ```--base8```: Use Base8 (Octal) encoding.
2. ACTION:
- ```-e``` or ```--encode```: Encode the provided string.
- ```-d``` or ```--decode```: Decode the provided string.
3. STRING:
- The text to encode or decode (must be a valid string for the operation).

## Examples
#### Encode to Base64
```ash
pyton3 encoder_tool.py -b64 -e "Hello, World!"
```

- Otput:
```laintext
SGVbG8sIFdvcmxkIQ==
```

#### Decode from Base64
```bash
python3 encoder_tool.py -b64 -d "SGVsbG8sIFdvcmxkIQ=="
```

Output:
```
Hello, World!
```

## Error Handling
- **No Base Selected**: If no valid base (```-b64```, ```-b32```, ```-b16```, ```-b8```) is selected, the script raises an error.
- **Invalid Encoded String**: Ensure the input for decoding is a valid encoded string to avoid runtime errors.

## Version
1.0

## Notes
- The script is for educational purposes only.
- Ensure to use a valid string for encoding and decoding to avoid unexpected behavior.
- Base8 (Octal) encoding uses ASCII values in octal format, and decoding expects a properly formatted string of octal values.

## License
This project is provided under the MIT License.
