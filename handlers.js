load(java.lang.System.getenv("DSS_SCRIPTING_ROOT") + "/handlers/erase.js");
load(java.lang.System.getenv("DSS_SCRIPTING_ROOT") + "/handlers/reset.js");
load(java.lang.System.getenv("DSS_SCRIPTING_ROOT") + "/handlers/load.js");
load(java.lang.System.getenv("DSS_SCRIPTING_ROOT") + "/handlers/evaluate.js");
load(java.lang.System.getenv("DSS_SCRIPTING_ROOT") + "/handlers/memory.js");

sessionHandlers = {
    "erase": eraseCommandHandler,
    "reset": resetCommandHandler,
    "load": loadCommandHandler,
    "evaluate": evaluateCommandHandler,
    "readData": memoryReadDataCommandHandler,
    "writeData": memoryWriteDataCommandHandler,
    "readRegister": memoryReadRegisterCommandHandler,
    "writeRegister": memoryWriteRegisterCommandHandler,
}
