/*
 *  test.js - Tests the DebugServer object
 */

'use strict';

/* First arg should be the port number to use for the Debug Server */
port = parseInt(this.arguments[0]);

load(java.lang.System.getenv("DSS_SCRIPTING_ROOT") + "/DebugServer.js");

config = {
    "cwd": "/path/to/repo/debugserver-js"   /* Currently not necessary */
};

print("Test started.");
print("Starting Debug Server...");

var server = new DebugServer(config, port);

print("Debug Server started on port: " + port + ".");

server.run();
server.shutdown();

java.lang.System.exit(0);
