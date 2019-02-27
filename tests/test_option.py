import pytest
import time
from test_helpers import (create_socket, send_msg, assert_msg_ok, assert_msg_fail,
                        start_server, start_session, kill_server, stop_session,
                        connect_to_target, disconnect_from_target)
from test_setup import CCXML_PATH, CONNECTION, DEVICETYPE, SESSION


def test_session_basic_get_option_numeric(debug_server):
    s = start_server()
    s2 = start_session(s)

    connect_to_target(s2)

    d = {
        "name": "getOption",
        "args": {
            "id": "TestNumeric"
        }
    }
    result = send_msg(s2, d)

    assert_msg_ok(result)
    assert type(result['data']) == int
    assert result['data'] == 0

    disconnect_from_target(s2)

    stop_session(s2)
    s2.close()

    kill_server(s)
    s.close()

def test_session_basic_get_option_boolean(debug_server):
    s = start_server()
    s2 = start_session(s)

    connect_to_target(s2)

    d = {
        "name": "getOption",
        "args": {
            "id": "TestBoolean"
        }
    }
    result = send_msg(s2, d)

    assert_msg_ok(result)
    assert type(result['data']) == bool
    assert result['data'] == False

    disconnect_from_target(s2)

    stop_session(s2)
    s2.close()

    kill_server(s)
    s.close()

def test_session_basic_get_option_string(debug_server):
    s = start_server()
    s2 = start_session(s)

    connect_to_target(s2)

    d = {
        "name": "getOption",
        "args": {
            "id": "TestString",
        }
    }
    result = send_msg(s2, d)

    assert_msg_ok(result)
    assert type(result['data']) == str
    assert result['data'] == ""

    disconnect_from_target(s2)

    stop_session(s2)
    s2.close()

    kill_server(s)
    s.close()

def test_session_basic_get_option_object(debug_server):
    s = start_server()
    s2 = start_session(s)

    connect_to_target(s2)

    d = {
        "name": "getOption",
        "args": {
            "id": "DeviceInfoRevision",
        }
    }
    result = send_msg(s2, d)

    assert_msg_ok(result)
    assert type(result['data']) == str
    assert result['data'] == "2.1"

    disconnect_from_target(s2)

    stop_session(s2)
    s2.close()

    kill_server(s)
    s.close()

def test_session_get_option_with_no_connection(debug_server):
    s = start_server()
    s2 = start_session(s)

    d = {
        "name": "getOption",
        "args": {
            "id": "DeviceInfoRevision"
        }
    }
    result = send_msg(s2, d)


    assert_msg_fail(result)

    stop_session(s2)
    s2.close()

    kill_server(s)
    s.close()

def test_session_basic_set_option_numeric(debug_server):
    s = start_server()
    s2 = start_session(s)

    connect_to_target(s2)

    d = {
        "name": "setOption",
        "args": {
            "id": "TestNumeric",
            "value": 0xFF
        }
    }
    result = send_msg(s2, d)

    assert_msg_ok(result)

    disconnect_from_target(s2)

    stop_session(s2)
    s2.close()

    kill_server(s)
    s.close()

def test_session_basic_set_option_boolean(debug_server):
    s = start_server()
    s2 = start_session(s)

    connect_to_target(s2)

    d = {
        "name": "setOption",
        "args": {
            "id": "TestBoolean",
            "value": True,
        }
    }
    result = send_msg(s2, d)

    assert_msg_ok(result)

    disconnect_from_target(s2)

    stop_session(s2)
    s2.close()

    kill_server(s)
    s.close()

def test_session_basic_set_option_string(debug_server):
    s = start_server()
    s2 = start_session(s)

    connect_to_target(s2)

    d = {
        "name": "setOption",
        "args": {
            "id": "TestString",
            "value": "Testing"
        }
    }
    result = send_msg(s2, d)

    assert_msg_ok(result)

    disconnect_from_target(s2)

    stop_session(s2)
    s2.close()

    kill_server(s)
    s.close()

