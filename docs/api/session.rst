.. _session:

Session commands are sent over a socket connected to the respective session port
(received when :ref:`opening a session<api:opensession>`)

.. warning::
    You must first :ref:`open a session<api:opensession>` on the DebugServer
    and connect to it over a socket before sending any session commands.

.. contents:: Command List:
    :local:
    :backlinks: top

----

connect
-------

Connect to the target

+----------------+---------------+----------------------------------+
| **Request**                                                       |
+================+===============+==================================+
| **Key**        | **Value**     | **Description**                  |
+----------------+---------------+----------------------------------+
| "name"         | "connect"     | \-                               |
+----------------+---------------+----------------------------------+
| "args"         | \-            | \-                               |
+----------------+---------------+----------------------------------+

.. code-block:: javascript

    //  Request
    {
        "name": "connect"
    }

disconnect
----------

Disconnect from the target

+----------------+---------------+----------------------------------+
| **Request**                                                       |
+================+===============+==================================+
| **Key**        | **Value**     | **Description**                  |
+----------------+---------------+----------------------------------+
| "name"         | "disconnect"  | \-                               |
+----------------+---------------+----------------------------------+
| "args"         | \-            | \-                               |
+----------------+---------------+----------------------------------+

.. code-block:: javascript

    //  Request
    {
        "name": "disconnect"
    }

erase
-----

Erases flash on target (must be :ref:`connected<api:connect>` to device)

+----------------+---------------+----------------------------------+
| **Request**                                                       |
+================+===============+==================================+
| **Key**        | **Value**     | **Description**                  |
+----------------+---------------+----------------------------------+
| "name"         | "erase"       | \-                               |
+----------------+---------------+----------------------------------+
| "args"         | \-            | \-                               |
+----------------+---------------+----------------------------------+

.. code-block:: javascript

    //  Request
    {
        "name": "erase"
    }

reset
-----

Resets device (must be :ref:`connected<api:connect>` to device)

+----------------+---------------+----------------------------------+
| **Request**                                                       |
+================+===============+==================================+
| **Key**        | **Value**     | **Description**                  |
+----------------+---------------+----------------------------------+
| "name"         | "reset"       | \-                               |
+----------------+---------------+----------------------------------+
| "args"         | \-            | \-                               |
+----------------+---------------+----------------------------------+

.. code-block:: javascript

    //  Request
    {
        "name": "reset"
    }

load
-----

Loads file into device's flash (must be :ref:`connected<api:connect>` to device)

+----------------+---------------+----------------------------------------------------+
| **Request**                                                                         |
+================+===============+====================================================+
| **Key**        | **Value**     | **Description**                                    |
+----------------+---------------+----------------------------------------------------+
| "name"         | "load"        | \-                                                 |
+----------------+---------------+----------------------------------------------------+
| "args"         | "file"        | Path to file to load                               |
|                +---------------+----------------------------------------------------+
|                | "binary"      | Load image as binary (optional; default=false)     |
|                +---------------+----------------------------------------------------+
|                | "address"     | Address location to load binary image (optional)   |
+----------------+---------------+----------------------------------------------------+

.. code-block:: javascript

    //  Request
    {
        "name": "load",
        "args": {
            "file": "/path/to/image.hex"
        }
    }

    //  Request (binary)
    {
        "name": "load",
        "args": {
            "file": "/path/to/image.bin",
            "binary": true,
            "address": 0x10000000
        }
    }

evaluate
--------

Evaluates an expression (must be :ref:`connected<api:connect>` to device)

+----------------+---------------+-------------------------------------------------------+
| **Request**                                                                            |
+================+===============+=======================================================+
| **Key**        | **Value**     | **Description**                                       |
+----------------+---------------+-------------------------------------------------------+
| "name"         | "evaluate"    | \-                                                    |
+----------------+---------------+-------------------------------------------------------+
| "args"         | "expression"  | Expression to evaluate                                |
|                +---------------+-------------------------------------------------------+
|                | "file"        | Path to symbols (.out) file to load first (optional)  |
+----------------+---------------+-------------------------------------------------------+

.. code-block:: javascript

    //  Request (with symbols)
    {
        "name": "evaluate",
        "args": {
            "expression": "&Sensor_msgStats",
            "file": "/path/to/symbols.out",
        }
    }


    //  Response
    {
        "status": "OK",
        "data": 51234234
    }

stop
----

Stop the session thread (does not :ref:`terminate session<api:terminatesession>`)

+----------------+---------------+----------------------------------+
| **Request**                                                       |
+================+===============+==================================+
| **Key**        | **Value**     | **Description**                  |
+----------------+---------------+----------------------------------+
| "name"         | "stop"        | \-                               |
+----------------+---------------+----------------------------------+
| "args"         | \-            | \-                               |
+----------------+---------------+----------------------------------+

.. code-block:: javascript

    //  Request
    {
        "name": "stop"
    }

