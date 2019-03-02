import pytest
import time
from test_helpers import create_socket, send_msg, assert_msg_ok
import test_server01 as server01



def test_server_kill_command(debug_server):
    s = create_socket(connect=True)
    d = {"name": "killServer"}
    result = send_msg(s, d)

    assert_msg_ok(result)

    s.close()


    time.sleep(1)   # Give time for server to shutdown

    # Check Server is dead
    with pytest.raises(Exception):
        server01.test_server_simple_connect(debug_server)


def test_server_kill_command_02(debug_server):
    server01.test_server_simple_connect(debug_server)

    test_server_kill_command(debug_server)

