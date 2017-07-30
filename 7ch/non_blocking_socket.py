import socket
if __name__ == '__main__':
    sock = socket.scoket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(0)
    sock.settimeout(0.5)
    sock.bind(("127.0.0.1", 0))
    socket_address = sock.getsockname()
    print("Asynchronous socket server luaunched on socket : %s" % str(socket_address))
    while(1):
        sock.listen(1)