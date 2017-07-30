from socket import socket
import ssl

from pprint import pprint

TARGET_HOST = 'localhost'
TARGET_PORT = 8000
CA_CERT_PATH = 'server.crt'

if __name__ == '__main__':
    sock = socket()