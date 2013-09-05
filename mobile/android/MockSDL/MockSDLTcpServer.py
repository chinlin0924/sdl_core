import socket


TCP_IP = '192.168.42.254'
TCP_PORT = 12345
BUFFER_SIZE = 20  # Normally 1024, but we want fast response


def startMobileNavSessionAck():
    """
    >>> startMobileNavSessionAck()
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)

    conn, addr = s.accept()
    print 'Connection address:', addr
    while 1:
        data = conn.recv(BUFFER_SIZE)
        if not data: break
        print "received data: %r" % data
        if compareMobileNavData(data):
            conn.send(startMobileNaviSessionACK())
    conn.close()


def startSessionAck():
    return str(bytearray([32, 7, 2, 48, 0, 0, 0, 0, 0, 0, 0, 48]))


def startMobileNavSession():
    return str(bytearray([32, 11, 1, 48, 0, 0, 0, 0, 0, 0, 0, 48]))


def startMobileNaviSessionACK():
    return str(bytearray([32, 11, 2, 48, 0, 0, 0, 0, 0, 0, 0, 48]))


def compareMobileNavData(expected):
    """test
    >>> compareMobileNavData(startMobileNavSession())
    True
    """
    if len(expected) > 3:
        expected = expected[:3]
    actual = startMobileNavSession()[:3]
    res = expected == actual
    return res

