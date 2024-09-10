## Take a test shot

--- task ---
With your Raspberry Pi switched off, connect your camera module.

[[[rpi-picamera-connect-camera]]]
--- /task ---

--- task ---
Switch on the Raspberry Pi. From the **Programming** menu, open Thonny. Save your file as `cresseggheads.py`.

--- /task ---

--- task ---

Add some code to import the `picamera` and `time` libraries, and initialise the camera:


--- code ---
---
language: python
line_numbers: true
line_number_start: 1
---
from picamzero import Camera
from time import sleep
cam = Camera()
--- /code ---

--- /task ---
