mqtt-spawn
==========

spawn a process per MQTT message, provide message on stdin

usage:

    ./mqtt-spawn.py <host> <cmd> <topic1> <topic2> ..

example:

    ./mqtt-spawn.py 172.16.68.10 'dotty -' oneshot/dot

will plot every graphviz message received on `oneshot/dot`