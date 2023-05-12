from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

simple_key = get_random_bytes(32)
print(simple_key)
salt = b'\x19D\x02\xea\xd3\x9bM\x10,\x9d\x9d#\xf6\xf7i~|Tg\xbf\x97\x9fq\xc6x\x915\x183B\x1a{'
password = 'mypassword'
key = PBKDF2(password, salt, dkLen=32)
message = b"Hello Secret World!"
cipher = AES.new(key, AES.MODE_CBC)
ciphered_data = cipher.encrypt(pad(message, AES.block_size))

with open('AES_encrypted.txt', 'wb') as f:
    f.write(cipher.iv)
    f.write(ciphered_data)

with open('AES_encrypted.txt', 'rb') as f:
    iv = f.read(16)
    decrypt_data = f.read()

cipher = AES.new(key, AES.MODE_CBC, iv=iv)
original = unpad(cipher.decrypt(decrypt_data),AES.block_size)
print(original)

with open('key.bin', 'wb') as f:
    f.write(key)

