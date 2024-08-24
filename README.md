# Password Protected Zip Archive Brute Force Script

This Python script is designed to brute force the password of a protected ZIP archive using a provided password list. Once the correct password is found, the script extracts all the files contained within the archive.

## Features
- Attempts to brute force the password of a ZIP archive using a list of potential passwords.
- Automatically extracts the contents of the archive once the correct password is identified.

## Requirements
- Python 3.x
- zipfile module (comes with Python's standard library)
- argparse module (comes with Python's standard library)

## Usage

To use the script, you will need to have a password-protected ZIP archive and a text file containing a list of potential passwords. Each password should be on a new line in the text file.
### Command Syntax
```python ZipBrute.py -z <zipfile.zip> -p <passwordfile.txt>```

### Arguments
- -z <zipfile.zip>: The path to the ZIP archive you want to brute force.
- -p <passwordfile.txt>: The path to the text file containing the list of potential passwords.

### Example
```python ZipBrute.py -z protected.zip -p rockyou(small).txt```

In this example, the script will attempt to brute force the password of protected.zip using the passwords listed in rockyou(small).txt.
## Script Output
- If the correct password is found, the script will display a banner along with the message:
```Found Password: <password>```
- If none of the passwords in the list match, the script will output:
  ```Password Not Found```

## License

This project is licensed under the MIT License.
## Disclaimer

This script is intended for educational purposes only. Do not use it for illegal activities. The author is not responsible for any misuse of this script.
