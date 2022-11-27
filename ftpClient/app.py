import os
import shutil

from AesEncryptor import AesEncryptor
from RotEncryptor import RotEncryptor
from SFTPClient import SFTPClient
from UploaderGUI import UploaderGUI

if __name__ == "__main__":
    hostname = input("Host Address: ")
    username = input("Username: ")
    password = input("Password: ")

    # hostname = "192.168.1.12" 
    # username = "sftpuser"
    # password = "pass"
    # port = 22

    sftp = SFTPClient(hostname, username, password)
    conn = sftp.connect()
    if (conn):
        print("Connection established successfully.")
        print(
            "\nEncrypt a file\nChose 1 for [ROT13 Cipher], 2 for [AES Encryption]")
        ch = input("Enter: ")
        gui = UploaderGUI()
        gui.run()
        local_path = gui.getPath()
        file_name = os.path.basename(local_path)

        remote_path = "files/" + file_name
        remote_key_path = "files/filekey.key"

        # make a copy of the uploaded file in tempdir
        shutil.copy(local_path, 'dir/')
        cwd = os.path.abspath(os.getcwd())
        cur_file_path = cwd + "/dir/" + file_name
        cur_key_path = cwd + "/dir/filekey.key"

        # run encryption
        if (ch == 1):
            encryptor = RotEncryptor()
        else:
            encryptor = AesEncryptor()
        encryptor.run(cur_file_path)
        print("Encrypted successfully.")

        upload2 = sftp.uploadFile(cur_key_path, remote_key_path)
        upload1 = sftp.uploadFile(cur_file_path, remote_path)

        if (upload1 and upload2):
            print("Uploaded successfully.")
            os.remove(cur_file_path)
            os.remove(cur_key_path)
        else:
            print("Failed to upload.")
    else:
        print("Failed to connect")
