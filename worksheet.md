# Cress Egg Heads

Plants grow far too slowly for you to see it happening. However, there's a trick that you can use to speed up time and watch them sprout!

If a photo is taken every minute, for instance, the photos can be stitched together into a movie or a GIF and the time between frames reduced to a fraction of a second. This is what we call a time-lapse film.

![flower](images/flower.gif)

You're going to use the technique of time-lapse photography to watch cress growing on some egg heads. The only trouble is you need to let the time pass and capture the images along the way. This is where the Raspberry Pi comes in, but first you'll need to make some cress egg heads!

## Making a cress egg head

1. Begin by soft-boiling the egg in a saucepan: you should ask for some help from an adult. Boil for no more than three minutes. Remove the egg using the spoon and allow to cool before handling.

1. Remove the top of the egg with the knife, as you would if you were going to eat it. Take care to avoid cracking the rest of the shell.

1. Use the spoon to scoop out all of the cooked egg from the inside of the eggshell. Your aim is to have a completely empty shell; don't worry if you spill some yolk on the outside.

1. Use the washing up liquid and bowl to wash the eggshell inside and out. Just use your fingers and handle the shell with care to avoid cracking it. Make sure there's no dried yolk on the outside.

1. Leave the egg to dry on some kitchen roll.

1. Once the egg has dried, you can use the crayons and pencils to carefully decorate it. Remember that the hole will be facing upwards, so bear this in mind if you want to draw a face.

1. Fill the eggs to the top with cotton wool and dampen with water. Top up with extra cotton wool and dampen again if necessary. The cotton wool should reach the top of the hole in the eggshell.

    ![](images/making-cress-egg-head.jpg)

1. Place the egg into an egg cup, then place the egg cup onto a plate.

1. Use your finger and thumb to sprinkle some cress seeds onto the cotton wool; the plate will catch any excess. That's it: the egg head is now ready to grow. Place the egg cup in a spot where it will receive sunlight during the day.

## Setting up the Camera Module

You can use the first two sections of the [Getting Started with PiCamera](https://www.raspberrypi.org/learning/getting-started-with-picamera/worksheet/) to test your camera and learn how to take a preview using Python.

It's a good idea to place your camera in a mount, to keep it still during the time-lapse shots. You could make your own, or use a commercial one like [this](http://www.modmypi.com/raspberry-pi/camera/camera-board-360-gooseneck-mount).

![](images/camera-mount.jpg)

With the camera in the mount, use the `preview` script from [Getting Started with PiCamera](https://www.raspberrypi.org/learning/getting-started-with-picamera/worksheet/) to test that the camera is pointing at the egg heads and has all of them in frame.

## Taking a test shot

Using a little bit of Python, you can now set up the camera to take a single photograph to begin with, and then start taking multiple shots at timed intervals.

1. Go to `Menu` > `Programming` > `Python 3 (IDLE)` to open up a Python shell, then click on `File` > `New File`. Click on `File` > `Save` and call your file `cresseggheads.py`.

1. The first part of your script will be fairly simple. Import the `picamera` library and the `time` library to begin with. You'll also need to initialise the camera:

    ``` python
    from picamera import PiCamera
    from time import sleep
    camera = PiCamera()
    ```

1. Next, you can start a preview, wait a few seconds, capture an image and then close the preview:

    ``` python
    camera.start_preview()
    sleep(5)
    camera.capture('image.jpg')
    camera.stop_preview()
    ```

1. Save (`Ctrl+S`) and run (`F5`) your code, and after 5 seconds an image should appear in your home folder (or whatever directory you saved your script in). If you double-click it, it will open and you should see a still shot of your cress egg heads.

1. To take multiple shots, a simple `while True` loop will enable the camera to keep taking photos every 5 seconds. Alter your code so it looks like this:

    ``` python
    while True:
        sleep(5)
        camera.capture('image.jpg')
    ```

    Run the code and see what happens. You can end the script after a minute or so, by pressing `Ctrl+C` on your keyboard.

    Have a look in your home directory. There's only one image! This is because the name of the image that is captured doesn't change, so it's constantly overwritten. 

1. You need to make sure that the image name keeps changing each time. To do this, you can use a variable to count the number of images taken, and use string formatting to use that number in the image name:

    ``` python
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

    Now save and run your program to see what happens. Do you see lots of images being created in your directory? Quit your script with `Ctrl+C`.

## Setting up for the real time-lapse

Before you start time-lapse recording the cress egg heads, there are several things you should consider. The most important is the physical location where the recording will take place. This needs to be somewhere warm with sunlight that can be left **undisturbed** for a whole week; a classroom windowsill might not be ideal. Even slight movements will be noticeable in the final cut.

Having an electric light source on the cress egg heads will allow growth to be recorded at night, and will make for a nicer end result. Without this setup, the recording will switch abruptly between light and darkness.

If you're using a fresh SD card with Raspbian installed this next part can be ignored, otherwise space on the SD card should also be taken into consideration. If you run out of free space halfway through the week, some footage will be lost. This can be predicted with a simple calculation to ensure there's enough free space on the SD card before starting.

1. The first thing to do is to check the size of the images your camera has been taking. The Pi camera image size will default to your screen resolution unless told otherwise, so image sizes may vary.

    To check the size of an image, open a terminal and type the following command:

    ``` bash
    du -h image0001.jpg
    ```

    You should get something that looks like this:

    ``` bash
    4024	image0001.jpg
    ```

    The number on the right is the number of kilobytes of space the image takes up.

1. Next, you can see how much space you have left on your micro SD card, by typing:

    ```bash
    df -h
    ```

    You should get something like this:

    ``` bash
    Filesystem      Size  Used Avail Use% Mounted on
    /dev/root       7.2G  3.3G  3.6G  49% /
    devtmpfs        182M     0  182M   0% /dev
    tmpfs           186M     0  186M   0% /dev/shm
    tmpfs           186M  4.5M  182M   3% /run
    tmpfs           5.0M  4.0K  5.0M   1% /run/lock
    tmpfs           186M     0  186M   0% /sys/fs/cgroup
    /dev/mmcblk0p1   63M   21M   43M  33% /boot
    tmpfs            38M     0   38M   0% /run/user/1000
    ```

    You're only interested in the top number in the `Avail` column. Here, it's showing 3.6 gigabytes of space left.

    So multiplying 3.6 by 1,000,000 tells you there are 3,600,000 kilobytes of space left on the micro SD card. With each image taking up 4024 kilobytes, 3,600,000 divided by 4024 is approximately 895 images. If there was to be one image captured every hour, that would mean 895 ÷ 24 or around 37 days of photographs, which in this case is more than enough to capture some cress seeds growing.

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

## Letting the cress grow and looking after it

The main priority now is to avoid touching or moving anything, to ensure the final time-lapse film will look good.

Remember to check the cress egg heads at least once a day (preferably more), to ensure the cotton wool does not dry out.

Use the plastic spray bottle to top up the moisture as necessary; the cotton wool should be damp but not soaking. Often a single spray per eggshell is enough.

If the room you have chosen is too cold you may see mould developing, which may mean you'll have to start again. Remember that the seeds need warmth, light, and water.

When the cress starts to grow, it may lean towards the direction of the sunlight; this is normal. This can be mitigated to a certain extent by rotating the egg cups to face the opposite way; however, this will be noticeable in the final time-lapse film.

## Creating a time-lapse video

Once the image sequence has been captured, you need to stitch the images together to form a film file that can be played back. There's a set of tools called audio video convert (avconv) that you can use for this. Look at the following command:

```bash
avconv -r 10 -i image%04d.jpg -r 10 -vcodec libx264 -crf 20 -g 15 timelapse.mp4
```

The `-r` specifies the video frame rate. Here we're using 10 frames a second; this is adequate for a time-lapse film. It's used twice to avoid avconv dropping similar-looking frames. The `-i` is the input filename; notice the `%04d`. This is because your images have names with 4-digit numbers in them.

The `-vcodec` specifies the codec (encode/decode) format of the video you're making. We've specified H264; YouTube uses this codec for streaming. The `-crf` specifies the compression quality level. 20 is an average value; lower numbers give higher quality but also increase file size. The `-g` specifies the GOP value; this is needed if you upload the video to YouTube later.

Once the encoding process has finished, you'll be returned to the command prompt. It may take a while to finish so be patient; maybe it's time for a cup of tea. When the process has completed, you can use the command below to play back the film on the Raspberry Pi:

```bash
omxplayer test_timelapse.mp4 -o hdmi
```

## What next?

- Why not upload the video to YouTube? 
- Could you use your skills to branch out into [stop-motion animation](https://github.com/raspberrypilearning/push-button-stop-motion/)? 
