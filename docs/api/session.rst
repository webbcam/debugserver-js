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

Erases flash on target (must be :ref:`connected<api:connect>`)

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

