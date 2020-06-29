from cryptography.fernet import Fernet

# reading key from file
file = open("key.key", "rb")
key = file.read()
file.close()

with open("sample.txt","rb") as file:
    payload = file.read()

fernet_object = Fernet(key)

encrypted_payload  = fernet_object.encrypt(payload)

with open("sample.encrypted.txt","wb") as file:
    file.write(encrypted_payload)
