## Take a test shot

First, check that your camera is working and positioned correctly.

--- task ---
With your Raspberry Pi switched off, connect your camera module.

[[[rpi-picamera-connect-camera]]]
--- /task ---

--- task ---
Position your Raspberry Pi near your egg, and point the camera in the right direction - you may find a camera mount helpful if you have one. Switch on the Raspberry Pi. 

![A Raspberry Pi with a camera mount attached](images/camera-mount.jpg)
--- /task ---

--- task ---
From the **Programming** menu, open Thonny. Save your file as `cresseggheads.py`.
--- /task ---

--- task ---

Add some code to import the `picamzero` and `time` libraries, and create the camera:

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

Underneath, add code to start a preview, wait a few seconds, take a photo and then close the preview:

--- code ---
---
language: python
line_numbers: true
line_number_start: 4
---
cam.start_preview()
sleep(5)
cam.take_photo('cress.jpg')
cam.stop_preview()
--- /code ---

--- /task ---

--- task ---

Save and run your code. After 5 seconds an image called `cress.jpg` should appear in the same directory you saved your Python code in. Open it to see a photograph of your cress egg heads.

--- collapse ---
---
title: It didn't work?
---

- Check that you have installed the `picamzero` software, using the instructions on the first page of this project.
- Check that you are looking in the same folder as your Python code for the image.

--- /collapse ---

--- /task ---

