.. _session:

Session commands are sent to the session socket.

.. warning::
    You must first :ref:`open a session<openSession>` on the DebugServer before sending any session
    commands.

erase
-----

Erases flash on target (must be connected)

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

