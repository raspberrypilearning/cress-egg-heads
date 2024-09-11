## Creating a time-lapse sequence

Now that you have checked your camera is working and that your egg is in shot, you can set up a time-lapse sequence. 

--- task ---

Change your program so that it captures a sequence of 12 images, at 2 seconds apart:

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 4
---
from picamzero import Camera

cam = PiCamera()
cam.capture_sequence(
        "cress.jpg", 
        num_images=12, 
        interval=2, 
        make_video=True
)
--- /code ---

--- /task ---

--- task ---
Save and run your program, then look at the images that have been taken. The program will also create a video called `cress.mp4` using the images.
--- /task ---

Now that you know how to use `capture_sequence` to create a time-lapse, you can set it up to run over a longer period of time by changing the parameters.

--- task ---

Change the parameters in your script so that it runs for a longer time. For example, if you want to take one image every hour, the `interval` can be calculated as:

60 seconds in one minute * 60 minutes in 1 hour = 3600 seconds

This code will take one picture every hour, for a whole day (24 hours).

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
line_highlights: 4
---
from picamzero import Camera

cam = PiCamera()
cam.capture_sequence(
    "cress.jpg", 
    num_images=24, 
    interval=3600, 
    make_video=True
)
--- /code ---

--- /task ---

--- collapse ---
---

title: Letting the cress grow and looking after it

---

Avoid touching or moving your cress to ensure the final time-lapse film will look good.

Remember to check the cress egg heads regularly, and spray with water to ensure the cotton wool does not dry out.

If the room you have chosen is too cold you may see mould developing, which may mean you'll have to start again. Remember that the seeds need warmth, light, and water.

--- /collapse ---



