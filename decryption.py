#this is the decryption file of the encryption.py we are implementing the symmetric encryption
import fernet
from cryptography.fernet import Fernet
with open('mykey.key','rb') as mykey:
    key = mykey.read()
f = Fernet(key)
with open('enc_grades.txt','rb') as encrypted_file:
    encrypted = encrypted_file.read()

decrypted = f.decrypt(encrypted)
with open('dec_grades.txt','wb') as decrypted_file:
    decrypted_file.write(decrypted)
