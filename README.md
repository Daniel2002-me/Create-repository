from cryptography.fernet import Fernet -Imports the encryption tool. 
original_message - Stores the original message. 
Fernet.generate_key()  Generates a secret encryption key. 
Fernet(key) Creates the encryption object. 
original_message.encode()-  Converts text into bytes. 
fnt.encrypt() Encrypts the message. 
print(encrypted_message)-Displays the encrypted message. 
fnt.decrypt()- Decrypts the message. 
.decode()- Converts bytes into readable text. 
print(decrypted_message)- Displays the original message.  
