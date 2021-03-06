import pytest
import time
from test_helpers import (create_socket, send_msg, assert_msg_ok, assert_msg_fail,
                        start_server, start_session, kill_server, stop_session,
                        connect_to_target, disconnect_from_target)
from test_setup import CCXML_PATH, CONNECTION, DEVICETYPE, SESSION


def test_session_basic_memory_read(debug_server):
    s = start_server()
    s2 = start_session(s)

    connect_to_target(s2)

    d = {
        "name": "readData",
        "args": {
            "page": 0,
            "address": 0x500012F0,
            "numBytes": 1
        }
    }
    result = send_msg(s2, d)

    assert_msg_ok(result)
    assert len(result['data']) == 1

    disconnect_from_target(s2)

    stop_session(s2)
    s2.close()

    kill_server(s)
    s.close()

def test_session_basic_memory_read_multiple_bytes(debug_server):
    s = start_server()
    s2 = start_session(s)

    connect_to_target(s2)

    d = {
        "name": "readData",
        "args": {
            "page": 0,
            "address": 0x500012F0,
            "numBytes": 4
        }
    }
    result = send_msg(s2, d)

    assert_msg_ok(result)
    assert len(result['data']) == 4

    disconnect_from_target(s2)

    stop_session(s2)
    s2.close()

    kill_server(s)
    s.close()

def test_session_read_memory_with_no_connection(debug_server):
    s = start_server()
    s2 = start_session(s)

    d = {
        "name": "readData",
        "args": {
            "page": 0,
            "address": 0x500012F0,
            "numBytes": 1
        }
    }
    result = send_msg(s2, d)


    assert_msg_fail(result)

    stop_session(s2)
    s2.close()

    kill_server(s)
    s.close()

def test_session_memory_read_invalid_address(debug_server):
    s = start_server()
    s2 = start_session(s)

    connect_to_target(s2)

    d = {
        "name": "readData",
        "args": {
            "page": 0,
            "address": 0xFFFFFFFF,
            "numBytes": 4
        }
    }
    result = send_msg(s2, d)

    assert_msg_fail(result)

    disconnect_from_target(s2)

    stop_session(s2)
    s2.close()

    kill_server(s)
    s.close()


def test_session_basic_memory_write(debug_server):
    s = start_server()
    s2 = start_session(s)

    connect_to_target(s2)

    d = {
        "name": "writeData",
        "args": {
            "page": 0,
            "address": 0x20000000,
            "data": 0x88
        }
    }
    result = send_msg(s2, d)

    assert_msg_ok(result)

    disconnect_from_target(s2)

    stop_session(s2)
    s2.close()

    kill_server(s)
    s.close()

def test_session_basic_memory_write_multiple(debug_server):
    s = start_server()
    s2 = start_session(s)

    connect_to_target(s2)

    d = {
        "name": "writeData",
        "args": {
            "page": 0,
            "address": 0x20000000,
            "data": [0x77, 0x88, 0x99, 0xAA]
        }
    }
    result = send_msg(s2, d)

    assert_msg_ok(result)

    disconnect_from_target(s2)

    stop_session(s2)
    s2.close()

    kill_server(s)
    s.close()

def test_session_memory_write_invalid_address(debug_server):
    s = start_server()
    s2 = start_session(s)

    connect_to_target(s2)

    d = {
        "name": "writeData",
        "args": {
            "page": 0,
            "address": 0xFFFFFFFF,
            "data": [0x77, 0x88, 0x99, 0xAA]
        }
    }
    result = send_msg(s2, d)

    assert_msg_fail(result)

    disconnect_from_target(s2)

    stop_session(s2)
    s2.close()

    kill_server(s)
    s.close()
