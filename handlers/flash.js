/**
 * flash.js - Flash include file that contains the flash handler command used
 * by handlers.js
 */


/**
 * Flash function for loading an image into a device's flash

 * @param {session} DSS Session object
 * @param {command} JSON object containing command name and args
          {command.args.image} (String): the path to the image to load
          {command.args.binary} (Boolean): use binary load (default = false)
          {command.args.address} (Num): Address to load binary image (required if binary = true)
 */
function flashCommandHandler(session, command) {
    if (session.target.isConnected()) {
        try {
            if (command.args['binary'] == true) {
                session.memory.loadBinaryProgram(command.args.image, command.args.address);
            } else {
                session.memory.loadProgram(command.args.image);
            }
        } catch (err) {
            return failResult(String(err));
        }
        return okResult()

    } else {
        return failResult("Target is not connected");
    }
}
