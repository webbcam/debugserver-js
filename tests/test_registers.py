import pytest
import time
from test_helpers import (create_socket, send_msg, assert_msg_ok, assert_msg_fail,
                        start_server, start_session, kill_server, stop_session,
                        connect_to_target, disconnect_from_target)
from test_setup import CCXML_PATH, CONNECTION, DEVICETYPE, SESSION


def test_session_basic_register_read(debug_server):
    s = start_server()
    s2 = start_session(s)

    connect_to_target(s2)

    d = {
        "name": "readRegister",
        "args": {
            "name": "PC",
        }
    }
    result = send_msg(s2, d)

    assert_msg_ok(result)
    assert type(result['data']) == int

    disconnect_from_target(s2)

    stop_session(s2)
    s2.close()

    kill_server(s)
    s.close()

def test_session_read_register_with_no_connection(debug_server):
    s = start_server()
    s2 = start_session(s)

    d = {
        "name": "readRegister",
        "args": {
            "name": "PC"
        }
    }
    result = send_msg(s2, d)


    assert_msg_fail(result)

    stop_session(s2)
    s2.close()

    kill_server(s)
    s.close()

def test_session_register_read_invalid_name(debug_server):
    s = start_server()
    s2 = start_session(s)

    connect_to_target(s2)

    d = {
        "name": "readRegister",
        "args": {
            "name": "INVALIDREG",
        }
    }
    result = send_msg(s2, d)

    assert_msg_fail(result)

    disconnect_from_target(s2)

    stop_session(s2)
    s2.close()

    kill_server(s)
    s.close()


def test_session_basic_register_write(debug_server):
    s = start_server()
    s2 = start_session(s)

    connect_to_target(s2)

    d = {
        "name": "writeRegister",
        "args": {
            "name": "R1",
            "value": 0xBEEF,
        }
    }
    result = send_msg(s2, d)

    assert_msg_ok(result)

    disconnect_from_target(s2)

    stop_session(s2)
    s2.close()

    kill_server(s)
    s.close()

def test_session_register_write_invalid_name(debug_server):
    s = start_server()
    s2 = start_session(s)

    connect_to_target(s2)

    d = {
        "name": "writeRegister",
        "args": {
            "name": "INVALIDREG",
            "value": 0xBEEF
        }
    }
    result = send_msg(s2, d)

    assert_msg_fail(result)

    disconnect_from_target(s2)

    stop_session(s2)
    s2.close()

    kill_server(s)
    s.close()
