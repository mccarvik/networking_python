import ftplib

FTP_SERVER_URL = 'ftp.all.kernel.org'
DOWNLOAD_DIR_PATH = '/pub/software/network/tftp'
DOWNLOAD_FILE_NAME = 'tftp-hpa-0.11.tar.gz'

def ftp_file_download(path, username, email):
    # open ftp connection
    ftp_client = ftplib.FTP(path, username, email)
    # list the files in te download directory
    ftp_client.cwd(DOWNLOAD_DIR_PATH)
    print("File list at %s:" % path)
    files = ftp_client.dir()
    print(files)
    # download a file
    file_handler = open(DOWNLOAD_FILE_NAME, 'wb')
    # ftp_cmd = 'RETR %s ' % DOWNLOAD_FILE_NAME
    ftp_client.retrbinary('RETR tftp-hpa-0.11.tar.gz', file_handler.write)
    file_handler.close()
    ftp_client.quit()

if __name__ == '__main__':
    ftp_file_download(path=FTP_SERVER_URL, username='anonymous', email='nobody@nourl.com')
    
    