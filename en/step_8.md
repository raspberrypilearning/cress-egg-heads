## Creating a time-lapse sequence

You can now make a slight edit to your script, so that images are taken every hour rather than every five seconds:

``` python
from picamera import PiCamera
from time import sleep

camera = PiCamera()

image_number = 0
while True:
    sleep(3600)
    image_name = 'image{0:04d}.jpg'.format(image_number)
    camera.capture(image_name)
    image_number += 1
```

Now run your script and leave it to record the images. Once your cress has finished growing (after a few days), you can stop the script with `Ctrl+C`.

