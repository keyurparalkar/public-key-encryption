from Crypto.Hash import SHA256
from Crypto.Cipher import DES
from Crypto.Cipher import ARC4
from Crypto import Random
from Crypto.PublicKey import RSA

print "Enter the  name of file:"
orig = raw_input()

file_file1 =open(orig).read()               #Open a file to encrypt.

random_generator = Random.new().read
key = RSA.generate(1024, random_generator)

public_key = key.publickey()

enc_data = public_key.encrypt(file_file1, 32)

print ("Data encrypted !!! ")
print ("encrypted data :\n")
print ("|------------------------------------------------------------| \n")
print (enc_data)
print ("|------------------------------------------------------------| \n")


print ("Data decrypted !!!")
print ("decrypted data :\n")
print ("|------------------------------------------------------------| \n")
print (key.decrypt(enc_data))
print ("|------------------------------------------------------------| \n")





