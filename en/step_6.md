## Creating a time-lapse sequence

--- task ---

You can now make a slight edit to your script, so that images are taken every hour rather than every five seconds:

```python
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

--- /task ---

--- task ---

Now run your script and leave it to record the images. Once your cress has finished growing (after a few days), you can stop the script with `Ctrl+C`.

--- /task ---

--- collapse ---
---

title: Letting the cress grow and looking after it

---

The main priority now is to avoid touching or moving anything, to ensure the final time-lapse film will look good.

Remember to check the cress egg heads at least once a day (preferably more), to ensure the cotton wool does not dry out.

Use the plastic spray bottle to top up the moisture as necessary; the cotton wool should be damp but not soaking. Often a single spray per eggshell is enough.

If the room you have chosen is too cold you may see mould developing, which may mean you'll have to start again. Remember that the seeds need warmth, light, and water.

When the cress starts to grow, it may lean towards the direction of the sunlight; this is normal. This can be mitigated to a certain extent by rotating the egg cups to face the opposite way; however, this will be noticeable in the final time-lapse film.

--- /collapse ---



