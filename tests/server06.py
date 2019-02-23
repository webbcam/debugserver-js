import pytest
import time
from test_helpers import create_socket, send_msg, assert_msg_ok



def test_server_get_timeout(debug_server):
    s = create_socket(connect=True)

    d = {"name": "getTimeout"}
    result = send_msg(s, d)
    assert_msg_ok(result)
    assert result['data'] == -1

    s.close()

def test_server_set_timeout(debug_server):
    s = create_socket(connect=True)

    d = {
        "name": "setTimeout",
        "args": {
            "timeout": 300
        }
    }

    result = send_msg(s, d)
    assert_msg_ok(result)

    d = {"name": "getTimeout"}
    result = send_msg(s, d)
    assert_msg_ok(result)
    assert result['data'] == 300

    s.close()
