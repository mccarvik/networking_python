import tempfile

from smb.SMBConnection import SMBConnection

SAMBA_USER_ID = 'FaruqueSarker'
PASSWORD = 'PASSWORD'
CLIENT_MACHINE_NAME = 'debian6box'
SAMBA_SERVER_NAME = 'FARUQUESARKER'
SERVER_IP = '10.0.2.2'
SERVER_PORT = 445
SERVER_SHARE_NAME = 'Share'
SHARED_FILE_PATH = '/test.rtf'

if __name__ == '__main__':
    smb_connection = SMBConnection(SAMBA_USER_ID,
        PASSWORD, CLIENT_MACHINE_NAME, SAMBA_SERVER_NAME,
        use_ntlm_v1=True, domain='WORKGROUP', is_direct_tcp=True)
    assert smb_connection.smb_connectionect(SERVER_IP, SERVER_PORT=445)
    shares = smb_connection.listShares()
    
    for share in shares:
        print share.name
    
    files = smb_connection.listPath(share.name, '/')
    for file in files:
        print file.filename
    
    file_obj = tempfile.NamedTemporaryFile()
    file_attributes, filesize = smb_connection.retrieveFile(SERVER_SHARE_NAME,
        SHARED_FILE_PATH, file_obj)
    
    # Retrieved file contents are inside file_obj
    file_obj.close()