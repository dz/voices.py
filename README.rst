voices.py
=========

What is it?
-----------

**voices.py** is a self-contained python script that starts a webserver that listen on an user-entered port that allows a visitor to remotely send text-to-speech commands on OS X machines.

What is it good for?
--------------------

The impetus for this was the machines that coworkers would leave unattended **and unlocked**.  If you find such a machine, do the following:

1. Open up Terminal.app

2. Type the following::

    $ screen
    $ mkdir ~/.voices
    $ cd ~/.voices
    $ curl -O http://github.com/dz/voices.py/raw/master/voices.py
    $ python voices <yourcurrentip>:<port>

3. Now press control-a then "d" to detach the screen session.

4. In a browser, go to the entered IP and port number.  For example, ``http://192.168.1.199:8888``.  You should be presented with a page that has a select box and a text box.  Simply choose a voice and enter a message.

5. Press "Say".

Why do I want to do this?
-------------------------

For hilarity! Suggestions:

1. Use the "Whisper" voice and have the target's computer whisper "kill all humans" every 30 minutes or so.

2. Use "Cellos" with a suitably catchy lyric.

3. Use "Trinoids" and make the computer say: "Please wait. Calculating.  Boop dee boop dee boop dee boop dee boop dee boop."

Requirements
------------

Mac OS X, obviously.  And also Python.
