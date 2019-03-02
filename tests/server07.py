import pytest
import time
from test_helpers import (create_socket, send_msg, assert_msg_ok, assert_msg_fail,
                        start_server, start_session, kill_server, stop_session,
                        connect_to_target, disconnect_from_target)
from test_setup import CCXML_PATH, CONNECTION, DEVICETYPE, SESSION

def test_server_attach_ccs(debug_server):
    s = create_socket(connect=True)

    d = {"name": "setConfig", "args": {
            "path": CCXML_PATH
            }
        }
    result = send_msg(s, d)

    assert_msg_ok(result)

    d = {
        "name": "attachCCS"
    }
    result = send_msg(s, d)
    assert_msg_ok(result)

    time.sleep(10)

    s.close()

def test_server_fail_attach_ccs_twice(debug_server):
    s = create_socket(connect=True)

    d = {"name": "setConfig", "args": {
            "path": CCXML_PATH
            }
        }
    result = send_msg(s, d)

    assert_msg_ok(result)

    d = {
        "name": "attachCCS"
    }
    result = send_msg(s, d)
    assert_msg_ok(result)

    result = send_msg(s, d)
    assert_msg_fail(result)

    time.sleep(10)

    s.close()

def test_server_attach_ccs_with_session(debug_server):
    s = start_server()
    s2 = start_session(s)

    connect_to_target(s2)

    d = {"name": "attachCCS"}
    result = send_msg(s, d)

    assert_msg_ok(result)

    time.sleep(20)

    disconnect_from_target(s2)

    time.sleep(10)

    stop_session(s2)
    s2.close()

    kill_server(s)
    s.close()
