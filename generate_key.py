# aes same key for enc and dec
from cryptography.fernet import Fernet

# generating a key
generated_key = Fernet.generate_key()

# storing in file
file = open("key.key","wb")
file.write(generated_key)
file.close()