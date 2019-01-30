import pytest
import time
from test_helpers import create_socket, send_msg, assert_msg_ok

def test_server_simple_connect(debug_server):
    s = create_socket(connect=True)
    s.close()


def test_server_multiple_connect(debug_server):
    for i in range(3):
        test_server_simple_connect(debug_server)
