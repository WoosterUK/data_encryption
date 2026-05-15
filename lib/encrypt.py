from cryptography.fernet import Fernet

def encrypt_data(data, public_key):
    """
    Encrypts the given data using the provided RSA public key.

    Parameters:
    data (str): The data to be encrypted.
    public_key (rsa.PublicKey): The RSA public key for encryption.

    Returns:
    bytes: The encrypted data.
    """
    f = Fernet(public_key)
    return f.encrypt(data.encode('utf-8'))

def generate_key():
    """
    Generates a new Fernet key for encryption.

    Returns:
    bytes: The generated Fernet key.
    """
    return Fernet.generate_key()