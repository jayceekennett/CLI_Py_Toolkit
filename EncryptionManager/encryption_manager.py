# encryption.py

'''
This script saves the user's password (or text) with a private RSA key, and
lets the user set a local password to encrypt it. 
NOTE: for security reasons DO NOT share/commit PEM files.'
'''

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
import base64
from getpass import getpass
import os
from pathlib import Path

class EncryptionManager:
    def __init__(self, dirpath: str):
        self.dirpath = dirpath      # defined storage path
    
    # ----- create/save RSA keys
    def create_save_keys(self) -> None:  
    # generate a new RSA private key
       key_password = getpass("Enter password>> ")  # prompt user to enter a custom password
       private_key = rsa.generate_private_key(
           public_exponent=65537,       # standard paramaters  
           key_size = 2048,             # RSA standard
           backend = default_backend()
       )
       byte_pw = key_password.encode('utf-8')       # encode RSA key with the user's custom password
       public_key = private_key.public_key()        # derive public key from private ky
       pem_private = private_key.private_bytes(     # serialise private key
           encoding = serialization.Encoding.PEM,
           format = serialization.PrivateFormat.PKCS8,
           encryption_algorithm = serialization.BestAvailableEncryption(byte_pw))  # could also be NoEncryption

       # check dir exists to save keys
       tgt_dir = Path(self.dirpath)
        
       if tgt_dir.exists() is False:
           os.mkdir("storage/")
       else:
           pass
       
       # write the serialized private key to a file.
       with open(f'{self.dirpath}/private_key.pem', 'wb') as f:     # serialise private key to PEM format
               f.write(pem_private)
            
       # serialise public key to PEM format
       pem_public = public_key.public_bytes(
           encoding = serialization.Encoding.PEM,
           format = serialization.PublicFormat.SubjectPublicKeyInfo
       )
       
       # write serialised public key
       with open(f'{self.dirpath}/public_key.pem', 'wb') as f:      # save keys
           f.write(pem_public)
    
    # ----- load private key
    def load_private_key(self) -> "rsa.RSAPrivateKey":
        pw_attempt = getpass("Enter password>> ")
        
   # load the private key from a PEM file.
        byte_pw = pw_attempt.encode('utf-8')
        with open(f'{self.dirpath}/private_key.pem', 'rb') as f:
               loaded_private_key = serialization.load_pem_private_key(
                   f.read(),
                   password = byte_pw, 
                   backend = default_backend()
               )
               return loaded_private_key
           
    # ---- load public key       
    def load_public_key(self) -> "rsa.RSAPublicKey":
     # loading the public key from a PEM file.
         with open(f'{self.dirpath}/public_key.pem', 'rb') as f:
             loaded_public_key = serialization.load_pem_public_key(
                 f.read(),
                 backend = default_backend()
             )      
             return loaded_public_key
     
     
    # ----- encrypt password     
    def encrypt(self, loaded_public_key) -> str:
         text = getpass("Password here>> ")         # getpass will NOT hide password in Spyder console
         byte_text = text.encode('utf-8')
         encrypted = loaded_public_key.encrypt(
             byte_text,
             padding.OAEP(
                 mgf = padding.MGF1(algorithm=hashes.SHA256()),
                 algorithm = hashes.SHA256(),
                 label = None
             )
         )
         encrypted = base64.b64encode(encrypted).decode("ascii")
         return encrypted 
     
    # ----- decrypt password 
    def decrypt(self, encrypted, loaded_private_key) -> str:
         encrypted = base64.b64decode(encrypted)
         decrypted = loaded_private_key.decrypt(
             encrypted,
             padding.OAEP(
                 mgf = padding.MGF1(algorithm = hashes.SHA256()),
                 algorithm = hashes.SHA256(),
                 label=None
             )
         )
         decrypted = decrypted.decode('utf-8')
         return decrypted
        
        
     