import pytest
import time
import subprocess
import os

from test_setup import CCXML_PATH, CONNECTION, DEVICETYPE, HOME, DEVELOP_PATH, CCS_EXE, PORT

@pytest.fixture(scope="function")
def debug_server(request):
    os.environ['DSS_SCRIPTING_ROOT'] = DEVELOP_PATH
    ccsexe = [CCS_EXE, "-noSplash", "-application", "com.ti.ccstudio.apps.runScript", "-ccs.script"]
    ccsexe.append(DEVELOP_PATH + "/test.js")
    ccsexe.append("-ccs.rhinoArgs")
    ccsexe.append(str(PORT))

    #p = subprocess.Popen(ccsexe)
    p = subprocess.Popen(ccsexe, stdout=subprocess.PIPE)

    # Wait until Debug Server has started
    line = ""
    while "Waiting for connections" not in str(line):
        line = p.stdout.readline()
    #time.sleep(10)

    def teardown():
        p.terminate()
    request.addfinalizer(teardown)
