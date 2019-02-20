import pytest
import time
from test_helpers import create_socket, send_msg, assert_msg_ok, assert_msg_fail
from test_setup import CCXML_PATH, CONNECTION, DEVICETYPE, SESSION


def test_server_create_session(debug_server):
    s = create_socket(connect=True)
    d = {"name": "setConfig", "args": {
            "path": CCXML_PATH
            }
        }
    result = send_msg(s, d)

    assert_msg_ok(result)

    d = {"name": "openSession", "args": {"name": SESSION}}
    result = send_msg(s, d)

    assert_msg_ok(result)
    assert result["data"]["name"] == SESSION
    sessionPort = result["data"]["port"]

    s2 = create_socket(connect=True, port=sessionPort)

    # Check we can send a command successfully
    d = {"name": "connect"}
    result = send_msg(s2, d)

    assert_msg_ok(result)

    s2.close()
    s.close()


def test_server_stop_session(debug_server):
    s = create_socket(connect=True)
    d = {"name": "setConfig", "args": {
            "path": CCXML_PATH
            }
        }
    result = send_msg(s, d)

    assert_msg_ok(result)

    d = {"name": "openSession", "args": {"name": SESSION}}
    result = send_msg(s, d)

    assert_msg_ok(result)
    assert result["data"]["name"] == SESSION
    sessionPort = result["data"]["port"]

    s2 = create_socket(connect=True, port=sessionPort)

    d = {"name": "connect"}
    result = send_msg(s2, d)

    assert_msg_ok(result)

    d = {"name": "stop"}
    result = send_msg(s2, d)

    assert_msg_ok(result)

    s2.close()
    s.close()


def test_server_terminate_session(debug_server):
    s = create_socket(connect=True)
    d = {"name": "setConfig", "args": {
            "path": CCXML_PATH
            }
        }
    result = send_msg(s, d)

    assert_msg_ok(result)

    d = {"name": "openSession", "args": {"name": SESSION}}
    result = send_msg(s, d)

    assert_msg_ok(result)

    sessionPort = result["data"]["port"]

    s2 = create_socket(connect=True, port=sessionPort)

    d = {"name": "connect"}
    result = send_msg(s2, d)

    assert_msg_ok(result)

    s2.close()

    d = {"name": "terminateSession", "args": {"name": SESSION}}
    result = send_msg(s, d)

    assert_msg_ok(result)

    time.sleep(2)   # Give time to close down

    # Check that port was closed on server side
    with pytest.raises(Exception):
        s2 = create_socket(connect=True, port=sessionPort)

def test_server_stop_and_terminate_session(debug_server):
    s = create_socket(connect=True)
    d = {"name": "setConfig", "args": {
            "path": CCXML_PATH
            }
        }
    result = send_msg(s, d)

    assert_msg_ok(result)

    d = {"name": "openSession", "args": {"name": SESSION}}
    result = send_msg(s, d)

    assert_msg_ok(result)
    assert result["data"]["name"] == SESSION
    sessionPort = result["data"]["port"]

    s2 = create_socket(connect=True, port=sessionPort)

    d = {"name": "connect"}
    result = send_msg(s2, d)

    assert_msg_ok(result)

    d = {"name": "stop"}
    result = send_msg(s2, d)

    assert_msg_ok(result)

    s2.close()

    time.sleep(2)

    d = {"name": "terminateSession", "args": {"name": SESSION}}
    result = send_msg(s, d)

    assert_msg_ok(result)

    time.sleep(2)   # Give time to close down

    # Check that port was closed on server side
    with pytest.raises(Exception):
        s2 = create_socket(connect=True, port=sessionPort)

def test_server_create_existing_session_fail(debug_server):
    s = create_socket(connect=True)
    d = {"name": "setConfig", "args": {
            "path": CCXML_PATH
            }
        }
    result = send_msg(s, d)

    assert_msg_ok(result)

    d = {"name": "openSession", "args": {"name": SESSION}}
    result = send_msg(s, d)

    assert_msg_ok(result)
    assert result["data"]["name"] == SESSION
    sessionPort = result["data"]["port"]

    s2 = create_socket(connect=True, port=sessionPort)

    # Check we can send a command successfully
    d = {"name": "connect"}
    result = send_msg(s2, d)

    assert_msg_ok(result)

    # Try to open an existing session
    d = {"name": "openSession", "args": {"name": SESSION}}
    result = send_msg(s, d)

    assert_msg_fail(result)

def test_server_kill_with_session_open(debug_server):
    s = create_socket(connect=True)
    d = {"name": "setConfig", "args": {
            "path": CCXML_PATH
            }
        }
    result = send_msg(s, d)

    assert_msg_ok(result)

    d = {"name": "openSession", "args": {"name": SESSION}}
    result = send_msg(s, d)

    assert_msg_ok(result)
    sessionPort = result["data"]["port"]

    s2 = create_socket(connect=True, port=sessionPort)

    # Check we can send a command successfully
    d = {"name": "connect"}
    result = send_msg(s2, d)

    s2.close()

    # Send kill command to server
    d = {"name": "killServer"}
    result = send_msg(s, d)

    assert_msg_ok(result)

    s.close()

def test_server_get_list_of_sessions(debug_server):
    s = create_socket(connect=True)
    d = {"name": "setConfig", "args": {
            "path": CCXML_PATH
            }
        }
    result = send_msg(s, d)

    assert_msg_ok(result)

    d = {"name": "openSession", "args": {"name": SESSION}}
    result = send_msg(s, d)

    assert_msg_ok(result)
    sessionPort = result["data"]["port"]

    d = {"name": "getListOfSessions"}
    result = send_msg(s, d)

    assert_msg_ok(result)
    assert result['data'][0]['name'] == SESSION
    assert result['data'][0]['port'] == sessionPort
