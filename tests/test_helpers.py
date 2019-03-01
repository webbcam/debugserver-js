import socket
import json

from test_setup import PORT, CCXML_PATH, CONNECTION, DEVICETYPE, SESSION

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

    r = bytearray()
    while b'\n' not in r:
        r.extend(s.recv(1024))

    result = json.loads(r)
    return result

def assert_msg_ok(result):
    assert result['status'] == "OK"

def assert_msg_fail(result):
    assert result['status'] == "FAIL"


def start_server():
    s = create_socket(connect=True)
    d = {"name": "setConfig", "args": {
            "path": CCXML_PATH
            }
        }
    result = send_msg(s, d)

    assert_msg_ok(result)

    return s

def kill_server(s):
    """Kills server using 's' debug server socket"""
    d = {"name": "killServer"}
    result = send_msg(s, d)

    assert_msg_ok(result)

def start_session(s):
    """Starts session using 's' debug server socket"""
    d = {"name": "openSession", "args": {"name": SESSION}}
    result = send_msg(s, d)

    assert_msg_ok(result)
    assert result["data"]["name"] == SESSION
    sessionPort = result["data"]["port"]

    s2 = create_socket(connect=True, port=sessionPort)

    return s2

def stop_session(s):
    """Stops session using 's' session socket"""
    d = {"name": "stop"}
    result = send_msg(s, d)

    assert_msg_ok(result)

def connect_to_target(s):
    """Connects to target on session 's' socket"""
    # Connect to target
    d = {"name": "connect"}
    result = send_msg(s, d)

    assert_msg_ok(result)

def disconnect_from_target(s):
    """Disconnects from target on session 's' socket"""
    # Disconnect from target
    d = {"name": "disconnect"}
    result = send_msg(s, d)

    assert_msg_ok(result)
