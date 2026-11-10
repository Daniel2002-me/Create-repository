from cryptography.fernet import Fernet loads the Fernet tool from the cryptography library. Fernet does symmetric encryption, meaning the same key locks and unlocks the data.
		original_message = "The boys are going to school" is the plain text you want to protect.
		key = Fernet.generate_key() creates a random secret key. Anyone with this key can decrypt the message.
	fnt = Fernet(key) builds an encryption object that uses that key.
		encrypted_message = fnt.encrypt(original_message.encode()) does the encryption. .encode() first converts the text into bytes, because Fernet only works on bytes, not regular strings.
		print(encrypted_message) shows the result, which looks like random text starting with b'gAAAAA....
