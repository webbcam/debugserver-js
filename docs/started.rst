.. _started:

===============
Getting Started
===============

Prerequisites
=============
You will need to have `Code Composer Studio`_ installed along with drivers
for any devices you plan to use (offered during installation of CCS or
available in CCS’s Resource Explorer).

Install
=======

::

    git clone https://github.com/webbcam/debugserver-js.git

Configure
=========

Open the file: ``run-server.sh`` and modify the ``CCS_EXE_PATH`` variable to
reflect your machine and CCS installation location.

Run
===

Open a terminal and run the ``run-server.sh`` script. (Leave this terminal
running in background)

.. image:: images/debug_server.png

Mac OS or Linux
---------------

::

    ./run-server.sh 4444

Windows
-------

Connect
=======

Once the DebugServer is running, you can then connect to the Server's socket
using any language that supports sockets. Here we show an example in Python:

::

    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("localhost", 4444))


Send Commands
=============

Commands can be sent to the Server over the socket in JSON format. Please see
the :ref:`API<API Reference>` for a full list of commands and their format.

::

    cmd = json.loads({"name": "ping"})
    s.sendall(cmd + "\n")

.. External Links
.. _Debug Server Scripting: http://software-dl.ti.com/ccs/esd/documents/users_guide/sdto_dss_handbook.html
.. _Code Composer Studio: http://www.ti.com/tool/CCSTUDIO
.. _Test Server: http://software-dl.ti.com/ccs/esd/documents/users_guide/sdto_dss_handbook.html#examples

