from Crypto.Cipher import DES
import json

key = input('key: ')

des = DES.new(key, DES.MODE_ECB)
encrypted = json.load(open('secret.txt')).encode('latin-1')
#print(encrypted)

decrypted = des.decrypt(encrypted)

if encrypted != des.encrypt(decrypted):
    print('wtf')
print(decrypted.decode())
