# MODUULI SALAUSAVAINTEN JA FERNET-SALAUKSEEN JA SEN PURKAMISEEN
# ==============================================================

# KIRJASTOJEN JA MODUULINE LATAUKSET
from cryptography.fernet import Fernet

def newKey() -> bytes:
    """Creates a new key for encrypting and decrypting messages

    Returns:
        bytes: a key in byte form
    """
    key = Fernet.generate_key()
    return key

def createCipher(key: bytes) -> object:
    """Creates a new cipher ie. encrypting machine

    Args:
        key (bytes): A fernet generated key

    Returns:
        object: The cipher object to use to encrypt or decrypt
    """
    cipher = Fernet(key)
    return cipher

def encrypt(cipher: object, plainText: bytes) -> bytes:
    """Encrypts a message using Fernet algorithm

    Args:
        cipher (object): Fernet ciphering engine
        plainText (str): Text to be encrypted

    Returns:
        bytes: encrypted text in byte format
    """
    cryptoText = cipher.encrypt(plainText)
    return cryptoText

def decrypt(cipher: object, cryptoText: str | bytes, byteMode: bool=False) -> str | bytes:
    """Decrypts a message

    Args:
        cipher (object): Decrypting engine
        cryptoText (str): Encrypted text to be decrypted
        byteMode (bool, optional): If return value will be in byte form. Defaults to False.

    Returns:
        str | bytes: message in plain text
    """
    if byteMode == True:
        plainText = cipher.decrypt(cryptoText)
    else:
        plainText = cipher.decrypt(cryptoText).decode()
    return  plainText
    
# TODO: Lisää jossain vaiheessa funnktiot, jotka ottavat parametriksi vain avaimen ja tekstin

if __name__ == "__main__":
    
    secretKey = newKey()
    print(secretKey)

