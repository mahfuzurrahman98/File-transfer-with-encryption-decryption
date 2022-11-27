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
