## Taking a test shot

Using a little bit of Python, you can now set up the camera to take a single photograph to begin with, and then start taking multiple shots at timed intervals.

--- task ---

Go to `Menu` > `Programming` > `Python 3 (IDLE)` to open up a Python shell, then click on `File` > `New File`. Click on `File` > `Save` and call your file `cresseggheads.py`.

--- /task ---

--- task ---

The first part of your script will be fairly simple. Import the `picamera` library and the `time` library to begin with. You'll also need to initialise the camera:

```python
from picamera import PiCamera
from time import sleep
camera = PiCamera()
```

--- /task ---

--- task ---

Next, you can start a preview, wait a few seconds, capture an image and then close the preview:

```python
camera.start_preview()
sleep(5)
camera.capture('image.jpg')
camera.stop_preview()
```

--- /task ---

--- task ---

Save (`Ctrl+S`) and run (`F5`) your code, and after 5 seconds an image should appear in your home folder (or whatever directory you saved your script in). If you double-click it, it will open and you should see a still shot of your cress egg heads.

--- /task ---

--- task ---

To take multiple shots, a simple `while True` loop will enable the camera to keep taking photos every 5 seconds. Alter your code so it looks like this:

```python
while True:
	sleep(5)
	camera.capture('image.jpg')
```

--- /task ---

--- task ---

Run the code and see what happens. You can end the script after a minute or so, by pressing `Ctrl+C` on your keyboard.

Have a look in your home directory. There's only one image! This is because the name of the image that is captured doesn't change, so it's constantly overwritten. 

--- /task ---

--- task ---

You need to make sure that the image name keeps changing each time. To do this, you can use a variable to count the number of images taken, and use string formatting to use that number in the image name:

```python
from picamera import PiCamera
from time import sleep

camera = PiCamera()

image_number = 0
while True:
	sleep(5)
	image_name = 'image{0:04d}.jpg'.format(image_number)
	camera.capture(image_name)
	image_number += 1
```

    The line before the loop begins sets the `image_number` variable to be 0. Within the loop, `image_number` is used to create a string called `image_name`. The name is made up of the strings `image` and `.jpg` but in between those strings is the image number, padded so it's 4 digits long (`{0:04d}`). You could alter `{0:04d}` to `{0:02d}` for instance, if you only wanted filename numbers that were two digits long.

--- /task ---

--- task ---

Now save and run your program to see what happens. Do you see lots of images being created in your directory? Quit your script with `Ctrl+C`.

--- /task ---
