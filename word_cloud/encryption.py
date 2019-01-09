from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

PADDING     = "+"
BLOCK_SIZE  = 86 # 128 Bytes minus 42 bytes (when using PKCS1_OAEP)
ENCODE_TYPE = "utf-8"

def get_public_key():
    with open("word_cloud/keys/public_key.pem", "rb") as file_handle:
        key = file_handle.read()
    return PKCS1_OAEP.new(RSA.importKey(key))

def get_private_key():
    with open("word_cloud/keys/private_key.pem", "rb") as file_handle:
        key = file_handle.read()
    return PKCS1_OAEP.new(RSA.importKey(key))

def encrypt(word, key):
    padding = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
    word    = padding(word).encode(ENCODE_TYPE)
    encrypted_word = key.encrypt(word)
    return base64.b64encode(encrypted_word)

def decrypt(word, key):
    decrypted_word = key.decrypt(base64.b64decode(word))
    word = decrypted_word.decode(ENCODE_TYPE)
    return word.rstrip(PADDING)

def salted_hash(word):
    ## take note of random seeding, randomly seeded
    ## os.environ['PYTHONHASHSEED'] 
    return hash(word)

