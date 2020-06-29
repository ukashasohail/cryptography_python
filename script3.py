from cryptography.fernet import Fernet

# reading key from file
file = open("key.key", "rb")
key = file.read()
file.close()

with open("sample.encrypted.txt","rb") as file:
    payload = file.read()

fernet_object = Fernet(key)

decrypted_payload  = fernet_object.decrypt(payload)

with open("sample.txt","wb") as file:
    file.write(decrypted_payload)
