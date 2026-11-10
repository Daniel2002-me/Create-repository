from cryptography.fernet import Fernet
original_message = "The boys are going to school"
key = Fernet.generate_key()
fnt = Fernet(key)
encrypted_message = fnt.encrypt(original_message.encode())
print(encrypted_message)
decrypted_message = fnt.decrypt(encrypted_message).decode()
print(decrypted_message)
# symmetric Algorithm