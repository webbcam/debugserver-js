import pytest
import time
from test_helpers import (create_socket, send_msg, assert_msg_ok, assert_msg_fail,
                        start_server, start_session, kill_server, stop_session,
                        connect_to_target, disconnect_from_target)
from test_setup import RESOURCES_PATH, CCXML_PATH, CONNECTION, DEVICETYPE, SESSION


def test_session_basic_flash(debug_server):
    s = start_server()
    s2 = start_session(s)

    connect_to_target(s2)

    d = {
        "name": "flash",
        "args": {
            "image": RESOURCES_PATH + "/sensor_cc1350lp.hex"
        }
    }
    result = send_msg(s2, d)

    assert_msg_ok(result)

    disconnect_from_target(s2)

    stop_session(s2)
    s2.close()

    kill_server(s)
    s.close()

def test_session_flash_binary(debug_server):
    s = start_server()
    s2 = start_session(s)

    connect_to_target(s2)

    d = {
        "name": "flash",
        "args": {
            "image": RESOURCES_PATH + "/sensor_cc1350lp.bin",
            "binary": True,
            "address": 0x0
        }
    }
    result = send_msg(s2, d)

    assert_msg_ok(result)

    disconnect_from_target(s2)

    stop_session(s2)
    s2.close()

    kill_server(s)
    s.close()

def test_session_flash_with_no_connection(debug_server):
    s = start_server()
    s2 = start_session(s)

    d = {"name": "flash"}
    result = send_msg(s2, d)


    assert_msg_fail(result)

    stop_session(s2)
    s2.close()

    kill_server(s)
    s.close()
