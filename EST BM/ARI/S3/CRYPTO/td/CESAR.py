def caesar_cipher(text, shift):
    encrypted_text = ""

    for char in text:
        if 'A' <= char <= 'Z':
            encrypted_char = chr(
                (ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char

    return encrypted_text


# Example usage:
text = "HELLO"
shift = 3
encrypted_text = caesar_cipher(text, shift)
print(encrypted_text)
