import pytest
import time
from test_helpers import create_socket, send_msg, assert_msg_ok

def test_server_set_console_log_command(debug_server):
    s = create_socket(connect=True)
    d = {
        "name": "setConsoleLevel",
        "args": {
            "level": "ALL"
        }
    }
    result = send_msg(s, d)
    assert_msg_ok(result)

    d = {
        "name": "setConsoleLevel",
        "args": {
            "level": "INFO"
        }
    }
    result = send_msg(s, d)
    assert_msg_ok(result)

    d = {
        "name": "setConsoleLevel",
        "args": {
            "level": "WARNING"
        }
    }
    result = send_msg(s, d)
    assert_msg_ok(result)

    d = {
        "name": "setConsoleLevel",
        "args": {
            "level": "OFF"
        }
    }
    result = send_msg(s, d)
    assert_msg_ok(result)


    s.close()
