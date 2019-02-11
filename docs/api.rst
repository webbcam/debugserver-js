.. _api:

API Reference
=============

Introduction
~~~~~~~~~~~~

After connecting to the DebugServer, you can send commands in the form of
:ref:`requests<Requests>`. For every :ref:`request<Requests>` sent the
DebugServer will reply with a :ref:`response<Responses>`.
The general format of :ref:`requests<Requests>`/:ref:`responses<Responses>` are shown below:

.. note::
    All requests and responses are in JSON format.

Requests
--------
Requests are sent to the DebugServer to execute a command. A Request will
always have a "name" field. A Request may also have an "args" field if the
command takes any parameters.

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
Responses are sent back by the DebugServer after completing a Request. A Response
will always have a "state" value which will either be "OK" (successful command)
or "FAIL" (failed command).

    - The "data" field is present when a successful command returns a value.
    - The "message" field is present when a command raises an error.

+----------------+---------+----------------------------------+----------------------------+--------------------------------------+
| Key            | Type    | Description                      | Values                     | Present                              |
+================+=========+==================================+============================+======================================+
| "state"        | String  | Result of a command              | "OK" or "FAIL"             | Always                               |
+----------------+---------+----------------------------------+----------------------------+--------------------------------------+
| "data"         | JSON    | Return value of a command        |                            | When a command returns a value       |
+----------------+---------+----------------------------------+----------------------------+--------------------------------------+
| "message"      | String  | Error message of failed command  |                            | When a command returns an error      |
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

----

Server Commands
~~~~~~~~~~~~~~~

.. include:: api/server.rst

Session Commands
~~~~~~~~~~~~~~~~

.. include:: api/session.rst
