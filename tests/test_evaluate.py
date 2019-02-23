import pytest
import time
from test_helpers import (create_socket, send_msg, assert_msg_ok, assert_msg_fail,
                        start_server, start_session, kill_server, stop_session,
                        connect_to_target, disconnect_from_target)
from test_setup import RESOURCES_PATH, CCXML_PATH, CONNECTION, DEVICETYPE, SESSION


def test_session_basic_evaluate(debug_server):
    s = start_server()
    s2 = start_session(s)

    connect_to_target(s2)

    d = {
        "name": "evaluate",
        "args": {
            "expression": "MassErase();"
        }
    }
    result = send_msg(s2, d)

    assert_msg_ok(result)

    # MassErase() automatically disconnects device
    #disconnect_from_target(s2)

    stop_session(s2)
    s2.close()

    kill_server(s)
    s.close()

def test_session_evaluate_with_no_connection(debug_server):
    s = start_server()
    s2 = start_session(s)

    d = {
        "name": "evaluate",
        "args": {
            "expression": "MassErase();"
        }
    }
    result = send_msg(s2, d)


    assert_msg_fail(result)

    stop_session(s2)
    s2.close()

    kill_server(s)
    s.close()

def test_session_evaluate_with_symbols(debug_server):
    s = start_server()
    s2 = start_session(s)

    connect_to_target(s2)

    d = {
        "name": "evaluate",
        "args": {
            "expression": "&Sensor_msgStats",
            "file": RESOURCES_PATH + "/sensor_cc1350lp.out"
        }
    }
    result = send_msg(s2, d)

    assert_msg_ok(result)
    assert type(result["data"]) == int

    disconnect_from_target(s2)

    stop_session(s2)
    s2.close()

    kill_server(s)
    s.close()

def test_session_evaluate_with_no_expression(debug_server):
    s = start_server()
    s2 = start_session(s)

    connect_to_target(s2)

    d = {
        "name": "evaluate",
        "args": {
            "file": RESOURCES_PATH + "/sensor_cc1350lp.out"
        }
    }
    result = send_msg(s2, d)

    assert_msg_fail(result)

    disconnect_from_target(s2)

    stop_session(s2)
    s2.close()

    kill_server(s)
    s.close()
