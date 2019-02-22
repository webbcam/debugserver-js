load(java.lang.System.getenv("DSS_SCRIPTING_ROOT") + "/handlers/erase.js");
load(java.lang.System.getenv("DSS_SCRIPTING_ROOT") + "/handlers/reset.js");
load(java.lang.System.getenv("DSS_SCRIPTING_ROOT") + "/handlers/load.js");

sessionHandlers = {
    "erase": eraseCommandHandler,
    "reset": resetCommandHandler,
    "load": loadCommandHandler,
}
