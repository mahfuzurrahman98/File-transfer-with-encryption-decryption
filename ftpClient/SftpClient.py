import pysftp


class SftpClient:
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

