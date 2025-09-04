from pyzipper import AESZipFile, WZ_AES
from string import digits 
import random
import os

if not os.path.exists('raw.txt'):
    with open('raw.txt', 'w') as f:
        f.write('This is a test file for ZIP archive with password.\n')
        f.close()
    print("[*] Created 'raw.txt' for archiving.")



def create_zip(file_to_add, archive_name,password_length):
    # Generate a random password
    
    table = digits
    password = "".join(random.choices(table, k=password_length)).encode()
    print(f"[*] Generated password: {password.decode()}")

    # Create zip archive
    with AESZipFile(archive_name, mode='w') as zf:
        zf.setpassword(password)
        zf.setencryption(WZ_AES, nbits=128)
        zf.write(file_to_add, arcname=file_to_add)

    print(f"[*] Archive '{archive_name}' containing '{file_to_add}' created successfully with password!")   




# Prefix to create a zip file
# You can increase the length of the password or rename the file by changing the variables below

file_to_add = 'raw.txt'                 # file to be archived (must create or have the specific file before)
archive_name = 'archive_withpass.zip'   # the name of the archive
password_length = 6                     # length of the password



if __name__ == "__main__":
    create_zip(file_to_add, archive_name, password_length)
