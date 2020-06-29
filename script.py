from cryptography.fernet import Fernet

# reading key from file
file = open("key.key", "rb")
key = file.read()
file.close()

# payload
msg = "IEEE Cyber Security Webinar"

# encoding & encrypting msg 
encoded_msg = msg.encode()
fernet_object = Fernet(key)
encrypted_msg = fernet_object.encrypt(encoded_msg)

# printing encrypted msg
print(f"msg after encryption: {encrypted_msg}")

# decrypting & decoding msg
fernet_object2 = Fernet(key)
decrypted_msg = fernet_object2.decrypt(encrypted_msg)
decoded_msg = decrypted_msg.decode()
print(f"msg after decryption: {decoded_msg}")