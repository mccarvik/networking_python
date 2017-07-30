import sshtunnel
from getpass import getpass

ssh_host = '192.168.56.101'
ssh_port = 22
ssh_user = 'YOUR_SSH_USERNAME'

REMOTE_HOST = '192.168.56.101'
REMOTE_PORT = 21

from sshtunnel import SSHTunnelForwarder
ssh_password = getpass('Enter YOUR_SSH_PASSWORD: ')

server = SSHTunnelForwarder(
    ssh_address=(ssh_host, ssh_port),
    ssh_username=ssh_user,
    ssh_password=ssh_password,
    remote_bind_address=(REMOTE_HOST, REMOTE_PORT))

server.start()
print('Connect the remote service via local port: %s' % server.local_bind_port)
# work with FTP SERVICE via the 'server.local_bind_port'
try:
    while True:
        pass
    except KeyboardInterrupt:
        print('Exiting user user request.\n')
        server.stop()