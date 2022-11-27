def RotDecryptor(file_name):
    def run():
        # opening the encrypted file
        with open(file_name, "rb") as enc_file:
            encrypted = enc_file.read()

        decrypted = ""
        for c in encrypted:
            if ((c >= 'a' and c <= 'm') or (c >= 'A' and c <= 'M')):
                decrypted += chr(ord(c) + 13)
            elif ((c >= 'n' and c <= 'z') or (c >= 'N' and c <= 'Z')):
                decrypted += chr(ord(c) - 13)
            else:
                decrypted += c

        # opening the file in write mode and
        # writing the decrypted data
        with open(file_name, "wb") as dec_file:
            dec_file.write(decrypted)
            print("File is successfully decrypted")