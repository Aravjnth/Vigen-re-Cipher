def vigenere_cipher(text, key):
    result = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            key_char = key[key_index % len(key)]
            result += chr((ord(char) - ascii_offset + ord(key_char) - ascii_offset) % 26 + ascii_offset)
            key_index += 1
        else:
            result += char
    return result

text = "Aravinth_aj"
key = "secret"
encrypted_text = vigenere_cipher(text, key)
print(f"Encrypted text: {encrypted_text}")
