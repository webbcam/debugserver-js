import pytest
import time
from test_helpers import create_socket, send_msg, assert_msg_ok, assert_msg_fail
from test_setup import CCXML_PATH, CONNECTION, DEVICETYPE, HOME, SESSION

def test_server_set_config(debug_server):
    s = create_socket(connect=True)
    d = {"name": "setConfig", "args": {
            "path": CCXML_PATH
            }
        }
    result = send_msg(s, d)

    assert_msg_ok(result)

#@pytest.mark.xfail(reason="No validating file path on JS side")
def test_server_set_config_fail(debug_server):
    s = create_socket(connect=True)
    d = {"name": "setConfig", "args": {
            "path": HOME + "/ti/CCSTargetConfigurations/MISSING.ccxml"
            }
        }
    result = send_msg(s, d)

    assert_msg_fail(result)

def test_server_get_config(debug_server):
    s = create_socket(connect=True)

    d = {"name": "setConfig", "args": {
            "path": CCXML_PATH
            }
        }
    result = send_msg(s, d)
    assert_msg_ok(result)

    d2 = {"name": "getConfig"}
    result = send_msg(s, d2)

    assert_msg_ok(result)
    assert result['data']['path'] == d['args']['path']

def test_server_get_empty_config(debug_server):
    s = create_socket(connect=True)

    d = {"name": "getConfig"}
    result = send_msg(s, d)

    assert_msg_ok(result)
    assert result['data']['path'] == None

def test_server_create_config(debug_server):
    s = create_socket(connect=True)
    directory = HOME + "/Develop/tiflash/"
    name = "TEST.ccxml"
    d = {"name": "createConfig", "args": {
            "connection": CONNECTION,
            "device": DEVICETYPE,
            "name": "TEST.ccxml",
            "directory": directory,
            }
        }

    result = send_msg(s, d)

    assert_msg_ok(result)
    assert result['data']['directory'] == directory
    assert result['data']['name'] == name

def test_server_create_config_missing_connection(debug_server):
    s = create_socket(connect=True)
    directory = HOME + "/Develop/tiflash/"
    name = "TEST.ccxml"
    d = {"name": "createConfig", "args": {
            "device": DEVICETYPE,
            "name": "TEST.ccxml",
            "directory": directory,
            }
        }

    result = send_msg(s, d)

    assert_msg_fail(result)
    assert result['message'] == "createConfig: Missing 'connection' argument"

def test_server_create_config_missing_device_and_board(debug_server):
    s = create_socket(connect=True)
    directory = HOME + "/Develop/tiflash/"
    name = "TEST.ccxml"
    d = {"name": "createConfig", "args": {
            "connection": CONNECTION,
            "name": "TEST.ccxml",
            "directory": directory,
            }
        }

    result = send_msg(s, d)

    assert_msg_fail(result)
    assert result['message'] == "createConfig: Missing 'board' or 'device' argument"

def test_server_create_config_missing_name(debug_server):
    s = create_socket(connect=True)
    directory = HOME + "/Develop/tiflash/"
    name = "TEST.ccxml"
    d = {"name": "createConfig", "args": {
            "connection": CONNECTION,
            "device": DEVICETYPE,
            "directory": directory,
            }
        }

    result = send_msg(s, d)

    assert_msg_fail(result)
    assert result['message'] == "createConfig: Missing 'name' argument"

def test_server_create_config_bad_connection(debug_server):
    s = create_socket(connect=True)
    directory = HOME + "/Develop/tiflash/"
    name = "TEST.ccxml"
    d = {"name": "createConfig", "args": {
            "connection": "BAD_CONNECTION",
            "device": DEVICETYPE,
            "name": "TEST.ccxml",
            "directory": directory,
            }
        }

    result = send_msg(s, d)

    assert_msg_fail(result)
    assert result['message'] == "createConfig: com.ti.ccstudio.scripting.environment.ScriptingException: Could not find the specified connection name."

def test_server_create_config_bad_device(debug_server):
    s = create_socket(connect=True)
    directory = HOME + "/Develop/tiflash/"
    name = "TEST.ccxml"
    d = {"name": "createConfig", "args": {
            "connection": CONNECTION,
            "device": "INVALID_DEVICE",
            "name": "TEST.ccxml",
            "directory": directory,
            }
        }

    result = send_msg(s, d)

    assert_msg_fail(result)
    assert result['message'] == "createConfig: com.ti.ccstudio.scripting.environment.ScriptingException: Could not find the specified device name."

def test_server_create_config_bad_board(debug_server):
    s = create_socket(connect=True)
    directory = HOME + "/Develop/tiflash/"
    name = "TEST.ccxml"
    d = {"name": "createConfig", "args": {
            "connection": CONNECTION,
            "board": "INVALID_BOARD",
            "name": "TEST.ccxml",
            "directory": directory,
            }
        }

    result = send_msg(s, d)

    assert_msg_fail(result)
    assert result['message'] == "createConfig: com.ti.ccstudio.scripting.environment.ScriptingException: Could not find the specified board name."

def test_server_create_config_bad_directory(debug_server):
    s = create_socket(connect=True)
    directory = HOME + "/fake_directory/"
    name = "TEST.ccxml"
    d = {"name": "createConfig", "args": {
            "connection": CONNECTION,
            "device": DEVICETYPE,
            "name": "TEST.ccxml",
            "directory": directory,
            }
        }

    result = send_msg(s, d)

    assert_msg_fail(result)
    #assert result['message'] == "createConfig: com.ti.ccstudio.scripting.environment.ScriptingException: Could not find the file specified."

def test_server_getListOfCPUs(debug_server):
    s = create_socket(connect=True)
    d = {"name": "setConfig", "args": {
            "path": CCXML_PATH
            }
        }
    result = send_msg(s, d)

    assert_msg_ok(result)

    d = {"name": "getListOfCPUs"}
    result = send_msg(s, d)

    assert_msg_ok(result)
    assert SESSION in result['data']['cpus']

def test_server_getListOfCPUs_fail(debug_server):
    s = create_socket(connect=True)

    d = {"name": "getListOfCPUs"}
    result = send_msg(s, d)

    assert_msg_fail(result)
