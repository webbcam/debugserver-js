function eraseCommandHandler(session, command) {
    if (session.target.isConnected()) {
        try {
            session.flash.erase();
        } catch (err) {
            return failResult(String(err));
        }
        return okResult()

    } else {
        return failResult("Target is not connected");
    }
}
