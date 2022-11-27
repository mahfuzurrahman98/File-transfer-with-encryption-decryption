from cryptography.fernet import Fernet


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
