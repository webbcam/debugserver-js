import socket
import json

from test_setup import PORT

def create_socket(connect=False, port=PORT):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if connect:
        s.connect(("localhost", port))
    return s

def send_msg(s, d):
    """Sends msg to socket.
    Args:
        s (socket): socket to send to
        d (dict): message to convert to json and send
    """
    msg = json.dumps(d)
    s.sendall(b"%s\n" % msg.encode())
    r = s.recv(1024)
    result = json.loads(r)

    return result

def assert_msg_ok(result):
    assert result['status'] == "OK"

def assert_msg_fail(result):
    assert result['status'] == "FAIL"
