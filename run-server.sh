#!/bin/bash
# Change CCS_EXE_PATH to your system's ccs executable:
#   - eclipsec (Windows)
#   - eclipse (Linux)
#   - ccstudio (Mac)
CCS_EXE_PATH=/Applications/ti/ccsv8/eclipse/Ccstudio.app/Contents/MacOS/ccstudio

# Arg1: script to run (e.g. test.js)
# Arg2: port number to use
$CCS_EXE_PATH -noSplash -application com.ti.ccstudio.apps.runScript -ccs.script $1 -ccs.rhinoArgs $2
