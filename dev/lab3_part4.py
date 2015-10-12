from Crypto.Cipher import DES
import json

key = input('key: ')
msg = input('message: ')

des = DES.new(key, DES.MODE_ECB)
encrypted = des.encrypt(msg)

#print(encrypted) rekt

encrypted_file = open('secret.txt', '+w')
json.dump(encrypted.decode('latin-1'), encrypted_file)


