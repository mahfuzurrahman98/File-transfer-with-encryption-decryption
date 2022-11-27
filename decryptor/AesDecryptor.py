from cryptography.fernet import Fernet


def AesDecryptor(file_name, key):
    def run():
        # using the generated key
        fernet = Fernet(key)

        # opening the encrypted file
        with open(file_name, "rb") as enc_file:
            encrypted = enc_file.read()

        # decrypting the file
        decrypted = fernet.decrypt(encrypted)

        # opening the file in write mode and
        # writing the decrypted data
        with open(file_name, "wb") as dec_file:
            dec_file.write(decrypted)
            print("File is successfully decrypted")