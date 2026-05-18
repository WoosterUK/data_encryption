from Crypto.Cipher import ARC4
from Crypto.Hash import HMAC, SHA256
from Crypto.Random import get_random_bytes

def encrypt_data(data, public_key):
    """
    Encrypts the given data using the provided RSA public key.

    Parameters:
    data (str): The data to be encrypted.
    public_key (rsa.PublicKey): The RSA public key for encryption.

    Returns:
    bytes: The encrypted data.
    """
    cipher = ARC4.new(public_key.encode('utf-8'))
    return cipher.encrypt(data.encode('utf-8'))

def generate_key():
    """
    Generates a new Fernet key for encryption.

    Returns:
    bytes: The generated Fernet key.
    """
    nonce = get_random_bytes(16)
    msg = get_random_bytes(16)
    key = HMAC.new(nonce, msg, digestmod=SHA256).hexdigest()
    return key

if __name__ == "__main__":
    key = generate_key()
    key_print = f"Generated encryption key: {key}"
    print(key_print)
    print("=" * len(key_print))

    text = "Hello, world"
    encrypted_text = encrypt_data(text, key)
    print(f"Plaintext: {text}")
    print(f"Encrypted text: {encrypted_text.hex()}")