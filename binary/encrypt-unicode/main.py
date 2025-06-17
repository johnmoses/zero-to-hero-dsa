""" 
Write an encryption algorithm to encrypt unicode
"""
def encrypt_unicode(text: str, key: int) -> str:
    """Encrypts unicode text using a simple shift cipher"""
    # Initialize the encrypted text
    encrypted = ''
    # Iterate over the text
    for char in text:
        # Get the unicode code point
        code_point = ord(char)
        # Shift the code point
        shifted = (code_point + key) % 0x10FFFF # Max unicode code point
        # Add the shifted code point to the encrypted text
        encrypted += chr(shifted)
    # Return the encrypted text
    return encrypted

def decrypt_unicode(encrypted: str, key: int) -> str:
    """Decrypts unicode text encrypted with encrypt_unicode()"""
    decrypted = ''
    for char in encrypted:
        code_point = ord(char)
        shifted = (code_point - key) % 0x10FFFF
        decrypted += chr(shifted)
    return decrypted

print(encrypt_unicode('Hello, World!', 1))
print(decrypt_unicode('Ifmmp-!Xpsme"', 1))

