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

--- task ---

Next, add code to start a preview, wait a few seconds, take a photo and then close the preview:

--- code ---
---
language: python
line_numbers: true
line_number_start: 4
---
cam.start_preview()
sleep(5)
cam.take_photo('image.jpg')
cam.stop_preview()
--- /code ---

--- /task ---

--- task ---

Save and run your code. After 5 seconds an image should appear in the same directory you saved your Python code in. Open it to see a photograph of your cress egg heads.

--- /task ---

