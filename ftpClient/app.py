import os
import shutil
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile

import pysftp
from cryptography.fernet import Fernet


class SFTPClient:
    sftp = None
    hostname = ""
    username = ""
    password = ""
    port = 0
    cnopts = pysftp.CnOpts()

    def __init__(self, hostname, username, password) -> None:
        self.cnopts.hostkeys = None
        self.hostname = hostname
        self.username = username
        self.password = password
        self.port = 22

    def connect(self):
        print("\nConnecting.......")
        try:
            self.sftp = pysftp.Connection(
                host=self.hostname,
                username=self.username,
                password=self.password,
                port=self.port,
                cnopts=self.cnopts
            )
            return True
        except:
            return False

    def uploadFile(self, local_path, remote_path):
        if local_path.find("filekey") == -1:
            print("\nUpolading files......")
        try:
            self.sftp.put(local_path, remote_path)
            return True
        except Exception as e:
            print("exception: ", e)
            return False


class AesEncryptor:
    def run(self, file_path):
        print("\nThe file is encrypting.....")
        # key generation
        key = Fernet.generate_key()

        # string the key in a file
        with open('dir/filekey.key', 'wb') as filekey:
            filekey.write(key)

        # opening the key
        with open('dir/filekey.key', 'rb') as filekey:
            key = filekey.read()

        # using the generated key
        fernet = Fernet(key)

        # opening the original file to encrypt
        with open(file_path, 'rb') as file:
            original = file.read()

        # encrypting the file
        encrypted = fernet.encrypt(original)

        # opening the file in write mode and
        # writing the encrypted data
        with open(file_path, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)


class RotEncryptor:
    def run(self, file_path):
        print("\nThe file is encrypting.....")

        key = "13"
        # string the key in a file
        with open('dir/filekey.key', 'wb') as filekey:
            filekey.write(key)

        # opening the original file to encrypt
        with open(file_path, 'rb') as file:
            original = file.read()

        # encrypting the file
        encrypted = ""
        for c in original:
            if ((c >= 'a' and c <= 'm') or (c >= 'A' and c <= 'M')):
                encrypted += chr(ord(c) + key)
            elif ((c >= 'n' and c <= 'z') or (c >= 'N' and c <= 'Z')):
                encrypted += chr(ord(c) - key)
            else:
                encrypted += c

        # opening the file in write mode and
        # writing the encrypted data
        with open(file_path, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)


class UploaderGUI:
    file_path = ""

    def openWindow(self):
        file = filedialog.askopenfilename()
        f_obj = open(file, 'r')
        self.file_path = f_obj.name
        f_obj.name

    def closeWindow(self, window):
        window.destroy()

    def getPath(self):
        return self.file_path

    def run(self):
        window = tk.Tk()
        window.geometry("210x100")  # Size of the window
        window.resizable(width=False, height=False)
        window.title('ftpClient')
        b1 = tk.Button(window, text='Upload File', width=25,
                       command=lambda: self.openWindow())
        b2 = tk.Button(window, text='Send', width=10,
                       command=lambda: self.closeWindow(window))
        b1.grid(row=2, column=1)
        b2.grid(row=6, column=1)
        window.mainloop()


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
