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


'''
OUTPUT:

Enter the  name of file:
/home/keyur/key.txt
Data encrypted !!!
encrypted data :

|------------------------------------------------------------|

('\x99\xfc\x07\xd9@\x9a\x89\xca\xfc~\x8e\x8d\x83-\xa6P\xf2E\x88\xfd\xf7\xcb\x0f\x1cr\x7f\xae\x97n\xf0\xabr\xcar!\xb9\xc6x\x8dQs\x97\x8c\xa3\xc2 \x8dJ\xcc\xc8\xce\xb1\xc3c\xd0@\x9fo\x93\xfcB}\rZ\xe3}t\x03\xad\x8a_R\xf21\x13K\xed\xea\x13\xce}BD\xae\xd15\x7f\xcdz\xbc\xb8@r\x007!\xa2Z>(\xf9\x94M\xb6\xb2\xd0B\xabJ\xc1r,\xf2\xed3<0\xf5\x8c-\xd3\x0c[\x9c\x97\xfb\x1fS',)
|------------------------------------------------------------|

Data decrypted !!!
decrypted data :

|------------------------------------------------------------|

keyur paralkar

|------------------------------------------------------------|


'''