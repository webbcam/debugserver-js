# This module is used to specify configurations to use for tests
import os
import platform

PORT = 4444

HOME = os.environ['USERPROFILE'] if platform.system() == "Windows" else os.environ['HOME']
DEVELOP_PATH = HOME + "/Develop/debugserver-js" # Set this to wherever the repo is


CCS_PREFIX = "/Applications/ti/ccsv8"
CCS_EXE = CCS_PREFIX + "/eclipse/Ccstudio.app/Contents/MacOS/ccstudio"


CCXML_PATH = HOME + "/ti/CCSTargetConfigurations/L400A85P.ccxml"
CCXML_PATH = HOME + "/ti/CCSTargetConfigurations/L2000JFL.ccxml"
CONNECTION = "Texas Instruments XDS110 USB Debug Probe"
DEVICETYPE = "CC1350F128"
SESSION = "Texas Instruments XDS110 USB Debug Probe/Cortex_M3_0"
