# PyBot-ClapperDetection

# Dependencies
- pyaudio
- requests

# Requirements
- Working microphone
- Live internet connection

This is a python script for detecting a clap to turn on and off the camera system.

It will first make a request to the server to detect if it is currently enabled or disabled.

The python script detects the volume of sound and if above a certain frequency, determines it must be a clap.
After detecting a clap, it will make a request to the server to either enable or disable the server.

It runs in an infinte loop until it is closed through cntrl-c

