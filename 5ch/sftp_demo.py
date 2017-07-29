import getpass
import paramiko

# HOSTNAME = 'localhost'
HOSTNAME = '192.168.43.130'
PORT = 22
FILE_PATH = '/tmp/test.txt'

def sftp_download(username, password, hostname=HOSTNAME, port=PORT):
    ssh_transport = paramiko.Transport(hostname, port)
    ssh_transport.connect(username=username, password=password)
    sftp_session = paramiko.SFTPClient.from_transport(ssh_transport)
    file_path = input("Enter filepath: ") or FILE_PATH
    target_file = file_path.splt('/')[-1]
    sftp_session.get(file_path, target_file)
    print("Downloaded file from: %s" % file_path)
    sftp_session.close()

if __name__ == '__main__':
    hostname = input("Enter the target hostname: ")
    port = input("Enter the targrt port: ")
    username = input("Enter the target port: ")
    password = getpass.getpass(prompt="Enter your password: ")
    sftp_download(username, password, hostname, int(port))