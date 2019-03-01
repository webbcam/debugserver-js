import pytest
import time
from test_helpers import (create_socket, send_msg, assert_msg_ok, assert_msg_fail,
                        start_server, start_session, kill_server, stop_session,
                        connect_to_target, disconnect_from_target)
from test_setup import CCXML_PATH, CONNECTION, DEVICETYPE, SESSION


def test_server_list_cpus(debug_server):
    s = start_server()

    d = {"name": "getListOfCPUs"}
    result = send_msg(s, d)

    assert type(result['data']) == list
    assert len(result['data']) > 0

    kill_server(s)
    s.close()

def test_server_list_devices(debug_server):
    s = start_server()

    d = {"name": "getListOfDevices"}
    result = send_msg(s, d)

    assert type(result['data']) == list
    assert len(result['data']) > 0

    kill_server(s)
    s.close()

def test_server_list_connections(debug_server):
    s = start_server()

    d = {"name": "getListOfConnections"}
    result = send_msg(s, d)

    assert type(result['data']) == list
    assert len(result['data']) > 0

    kill_server(s)
    s.close()

def test_server_list_configurations(debug_server):
    s = start_server()

    d = {"name": "getListOfConfigurations"}
    result = send_msg(s, d)

    assert type(result['data']) == list

    kill_server(s)
    s.close()
