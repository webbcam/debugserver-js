.. _api:

API Reference
=============

.. note::
    All requests and responses are in a JSON format.

Requests
--------
Requests are sent to the DebugServer to execute a command.

+----------------+---------+----------------------------------+----------------------------+--------------------------------------+
| Key            | Type    | Description                      | Values                     | Required                             |
+================+=========+==================================+============================+======================================+
| "name"         | String  | Name of command to call          |                            | Always                               |
+----------------+---------+----------------------------------+----------------------------+--------------------------------------+
| "args"         | JSON    | Arguments to pass to command     |                            | When a command takes an argument(s)  |
+----------------+---------+----------------------------------+----------------------------+--------------------------------------+

.. code-block:: javascript

    //  Request
    {
        "name": "commandName",
        "args": {
            "arg1": "value",
            "arg2": true
        }
    }

----

Responses
---------
Responses are received from the DebugServer upon sending a Request.

+----------------+---------+----------------------------------+----------------------------+--------------------------------------+
| Key            | Type    | Description                      | Values                     | Present                              |
+================+=========+==================================+============================+======================================+
| "state"        | String  | Result of a command              | "OK" or "FAIL"             | Always                               |
+----------------+---------+----------------------------------+----------------------------+--------------------------------------+
| "data"         | JSON    | Return value of a command        |                            | When a command returns a value       |
+----------------+---------+----------------------------------+----------------------------+--------------------------------------+
| "message"      | JSON    | Error message of failed command  |                            | When a command returns an error      |
+----------------+---------+----------------------------------+----------------------------+--------------------------------------+

.. code-block:: javascript

    //  Success Response
    {
        "state": "OK",
        "data": {
            "key": "value"
        }
    }


    //  Failure Response
    {
        "state": "FAIL",
        "message": "Error message description"
    }
