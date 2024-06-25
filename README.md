 Vigenère Cipher

## Overview

The Vigenère Cipher is a method of encrypting alphabetic text by using a simple form of polyalphabetic substitution. This Python-based implementation provides a command-line interface to encrypt and decrypt messages using the Vigenère Cipher technique.

## Features

- Encrypt messages using a keyword.
- Decrypt messages using a keyword.
- Supports both uppercase and lowercase letters.
- Ignores non-alphabetic characters (e.g., numbers, punctuation).

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Aravjnth/Vigen-re-Cipher.git
    cd vigenere-cipher
    ```

## Usage

1. Run the tool to encrypt or decrypt a message:
    ```bash
    python vigenere_cipher.py -m <mode> -t <text> -k <keyword>
    ```

    Replace `<mode>`, `<text>`, and `<keyword>` with the actual values.

### Example

Encrypt a message with a keyword "KEY":

```bash
python vigenere_cipher.py -m encrypt -t "Hello, World!" -k "KEY"
```

Decrypt a message with a keyword "KEY":

```bash
python vigenere_cipher.py -m decrypt -t "Rijvs, Uyvjn!" -k "KEY"
```

## Options

- `-m, --mode`: Mode of operation (encrypt or decrypt).
- `-t, --text`: Text to be encrypted or decrypted.
- `-k, --keyword`: Keyword used for the encryption or decryption.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, feel free to contact me at www.linkedin.com/in/aravinth-aj
