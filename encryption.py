#implementation of the symmetric key encryption
import fernet
from cryptography.fernet import Fernet
#key = Fernet.generate_key() #to generate the key
#with open('mykey.key','wb') as mykey:
 #   mykey.write(key)
with open('mykey.key','rb') as mykey:
    key = mykey.read()
print(key)
f = Fernet(key)
with open('new.txt','rb') as original_files:
    original = original_files.read()

encrypted = f.encrypt(original)

with open('enc_grades.txt','wb') as encrypted_file:
    encrypted_file.write(encrypted)
