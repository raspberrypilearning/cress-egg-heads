# Cress Egg Heads

Plants grow far too slowly for you to see it happening. However, there is a trick that you can use to speed up time and watch them sprout!

If a photo is taken every minute, for instance, the photos can be stitched together into a movie or a gif and the time between frames reduced to a fraction of a second. This is what we call a time-lapse film.

![flower](images/flower.gif)

You are going to use the technique of time-lapse photography to watch cress growing on some egg heads. The only trouble is you need to let the time pass and capture the images along the way. This is where the Raspberry Pi comes in. But first you'll need to make some cress egg heads!

## Making a cress egg head

Begin by soft-boiling the egg in a saucepan: you should ask for some help from an adult. Boil for no more than 3 minutes. Remove the egg using the spoon and allow to cool before handling.

Remove the top of the egg with the knife, as you would if you were going to eat it. Take care to avoid cracking the rest of the shell.

Use the spoon to scoop out all of the cooked egg from the inside of the eggshell. Your aim is to have a completely empty shell; don't worry if you spill some yolk on the outside.

Use the washing up liquid and bowl to wash the eggshell inside and out. Just use your fingers and handle the shell with care to avoid cracking it. Make sure there is no dried yolk on the outside.

Leave the egg to dry on some kitchen roll.

Once the egg has dried you can use the crayons and pencils to carefully decorate it. Remember that the hole will be facing upwards, so bear this in mind if you want to draw a face.

Fill the eggs to the top with cotton wool and dampen with water. Top up with extra cotton wool and dampen again if necessary. The cotton wool should reach the top of the hole in the eggshell.

![](images/making-cress-egg-head.jpg)

Place the egg into an egg cup, then place the egg cup onto a plate.

Use your finger and thumb to sprinkle some cress seeds onto the cotton wool; the plate will catch any excess. That's it; the egg head is now ready to grow. Place the egg cup in a spot where it will receive sunlight during the day.

## Setting up the Camera Board

You can use the first two sections of the [Getting Started with PiCamera](https://www.raspberrypi.org/learning/getting-started-with-picamera/worksheet/) to test you camera and learn how to take a preview using Python.

It's a good idea to place your camera in a mount, to keep it still during the timelapse shots. You could make your own or use a commerical one like [thih](http://www.modmypi.com/raspberry-pi/camera/camera-board-360-gooseneck-mount)

![](images/camera-mount.jpg)

With the camera in the mount, use the `preview` script from [Getting Started with PiCamera](https://www.raspberrypi.org/learning/getting-started-with-picamera/worksheet/) to test it's pointing at the egg heads and has all of them in focus.

## Taking a test shot

Using a little bit of Python you can now set up the camera to take a single photograph to begin with, and then start taking multiple shots at timed intervals.

Go to `Menu` > `Programming` > `Python 3 (IDLE)` to open up a Python shell. Then click on `File` > `New File`. Click `File` > `Save` and call your file `cresseggs.py`

The first part of your script will be fairly simple. Import the `picamera` library and the `time` library to begin with. You'll also need to initiate the camera.

``` python
from picamera import PiCamera
from time import sleep
camera = PiCamera()
```

Next you can start a preview, wait a few seconds, capture and image and then close the preview.

``` python
camera.start_preview()
sleep(5)
camera.capture('image.jpg')
camera.stop_preview()
```

Save (`ctrl+s`) and run (`F5`) your code and after 5 seconds and image should appear in your home folder (or whatever directory you saved your script in). If you double click it, it will open and you should see a still shot of your cress egg-heads.

To take multiple shots, a simple `while True` loop will enable the camera to keep taking photos every 5 seconds.

Alter your code so it looks like this.

``` python
while True:
    sleep(5)
    camera.capture('image.jpg')
```

Run the code and see what happens. You can end the script after a minute or so, by hitting `ctrl+c` on your keyboard.

Have a look in your home folder. There's only one image!

This is because the name of the image that is captured does not change, so it is constantly written over. You need to make sure that the image name keeps changing each time.

To do this you can use a variable to count the image number, and string formating to use that number in the image name.

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

The first line sets the `image_number` variable to be 0, then the loop begins. The fourth line uses the image_number to create a string called `image_name`. The name is made up of the strings `image` and `.jpg` but in between those strings is the image number, padded so it is 4 digits long.

You could alter `{0:04d}` to `{0:02d}` for instance, if you only wanted filename numbers that were two digits long.

Now save and run your program to see what happens. Do you see lots of images beign created in your directory?

Quit your script with `ctrl+c`

## Setting up the real timelapse



## Creating a time lapse video

Let's take this test run all the way to the end. Next we need to stitch the 60 or so images together to form a film file that can be played back. There are a set of tools called avconv (audio video convert) that we can use for this.

This will ask to download about 20 MB of data; say yes and allow the install to proceed. It will take several minutes. Once complete, you can use the command below to construct the video file from the individual images. Enter it all on one line.

```bash
avconv -r 10 -i test_%04d.jpg -r 10 -vcodec libx264 -crf 20 -g 15 test_timelapse.mp4
```

This will make a video at the same resolution as the individual images (2592 x 1944 pixels). You'll notice it's quite slow on the Raspberry Pi. Press `Ctrl – C` to abort the encoding process. You can speed this up by scaling down each image as they're stitched into the final film; the command below will do just that.

```bash
avconv -r 10 -i test_%04d.jpg -r 10 -vcodec libx264 -crf 20 -g 15 -vf scale=1296:972 test_timelapse.mp4
```

The `-r` specifies the video frame rate. Here we're using 10 frames a second; this is adequate for a time-lapse film. It's used twice to avoid avconv dropping similar looking frames. The `-i` is the input filename; notice the `%04d` from before. The `-vcodec` specifies the codec (encode/decode) format of the video you're making. We've specified H264; YouTube uses this codec for streaming. The `-crf` specifies the compression quality level. 20 is an average value; lower numbers give higher quality but also increase file size. The `-g` specifies the GOP value; this is needed if you upload the video to YouTube later. Finally, the `-vf` specifies a video filter that scales the images down to the given height and width. Scale values can be tweaked as necessary.

Once the encoding process has finished you'll be returned to the command prompt. It may take a while to finish so be patient; maybe it's time for a cup of tea. When the process has completed you can use the command below to play back the film on the Raspberry Pi.

```bash
omxplayer test_timelapse.mp4 -o hdmi
```

Please note that it is much faster to do the encoding on a desktop PC or Mac. Visit [this page](http://libav.org/download.html "Get Libav") to download the appropriate version for your operating system.

If you want to delete all the files from this test run then use the following command:

```bash
rm test_*.*
```

## Start recording the main time-lapse film

Before you start time-lapse recording the cress egg heads there are several things you should consider. The most important is the physical location where the recording will take place. This needs to be somewhere warm with sunlight that can be left **undisturbed** for a whole week; a classroom windowsill might not be ideal. Even slight movements will be noticeable in the final cut.

A power failure will break the sequence of file numbering so you should try to prevent any loss of power after the recording starts. If this does happen you'll need to start again.

Having a man-made light source on the cress egg heads will allow growth to be recorded at night, and will make for a nicer end result. Without this setup, the recording will switch abruptly between light and darkness.

You may also wish to have a network cable plugged in, so that you can log into the Pi remotely and monitor that the file creation process is continuing as expected (read up about [SSH](https://www.raspberrypi.org/documentation/remote-access/ssh/)).

Space on the SD card should also be taken into consideration. If you run out of free space half way through the week some footage will be lost. This can be predicted with a simple calculation to ensure there is enough free space on the SD card before starting.

Let's check this first. On average, an image will be about 3 MB in size. There are 24 hours in a day so if we record one image per hour, the space needed is 3 MB x 24 = 72 MB a day. In a week we will need 72 MB x 7 = 504 MB. 504 MB!  So if we ensure we have at least 1000 MB (1 GB) free on the SD card we should be fine.

You can use the following command to check how much free space you have:

```bash
df -h
```

This should show you something like the text below. Look at the size value for rootfs under the available space column (Avail). In the example below it shows 2 GB is free.

```
Filesystem      Size  Used Avail Use% Mounted on
rootfs          3.6G  1.5G  2.0G  43% /
/dev/root       3.6G  1.5G  2.0G  43% /
devtmpfs        101M     0  101M   0% /dev
tmpfs            22M  232K   22M   2% /run
tmpfs           5.0M     0  5.0M   0% /run/lock
tmpfs            44M     0   44M   0% /run/shm
/dev/mmcblk0p1   56M   19M   38M  34% /boot
```
If it looks like you don't have enough space you can use an SD card with a larger capacity.

Once you have identified a suitable filming location, set the Raspberry Pi, camera board, camera mount, keyboard, monitor and cress egg heads up there. Boot up the Raspberry Pi, log in as normal and use the camera preview command to get everything positioned correctly:

```bash
raspivid -t 0
```

If there are multiple cress egg heads, try to get them all in the shot. Remember that still images will appear a little more zoomed out than the camera preview. Once you're satisfied with the position of the camera and egg heads, you can press `Ctrl – C` to stop the preview.

Now you're ready to start the time-lapse recording. Firstly, we need to work out the interval time and total time in milliseconds to give to the raspistill command. One hour is 1000 x 60 x 60 = 3600000. One day is 3600000 x 24 = 86400000. One week is 86400000 x 7 = 604800000. Therefore our final command should be this:

```bash
raspistill -o cress_%04d.jpg -tl 3600000 -t 604800000
```

The first image will only be captured after the first hour, so you still have one hour to make any final adjustments and disconnect the keyboard and monitor. For extra reliability you could secure the Pi and Gooseneck mount in place with some tape. Write down the exact time you start the time-lapse; you'll want to know this at the end of the week.

Disconnect the keyboard first and with one final check of the camera preview, remove the monitor cable from the Raspberry Pi without moving anything. Your setup is now complete, and should be left undisturbed for 7 days. A quick visual check to confirm that everything is still okay is to check the red LED on the camera board. If the LED goes off, either the time-lapse recording has finished after 7 days of elapsed time, or the recording has been interrupted by a problem such as loss of power. Occasional checks of the LED are recommended.

## Letting the cress grow and looking after it

The main priority now is to avoid touching or moving anything to ensure the final time-lapse film will look good.

Remember to check the cress egg heads at least once a day (preferably more) to ensure the cotton wool does not dry out.

Use the plastic spray bottle to top up the moisture as necessary; the cotton wool should be damp but not soaking. Often a single spray per eggshell is enough.

If the room you have chosen is too cold you may see mould developing, which may mean you'll have to start again. Remember the seeds need warmth, light and water.

When the cress starts to grow, it may lean towards the direction of the sunlight; this is normal. This can be mitigated to a certain extent by rotating the egg cups to face the opposite way; however this will be noticeable in the final time-lapse film.

## Creating the time-lapse film file

The cress should be gaining some height by the end of the week. Wait for the red LED on the camera board to go out before retrieving the images. This should happen exactly one week, to the minute, after you started the time-lapse.

Reconnect the monitor and keyboard and use the `ls` command. You should find that about 170 images have been created. These files must be preserved carefully; it's a good idea to back them up onto a USB flash drive. If you want to move the Raspberry Pi back to the classroom before encoding the time-lapse video, ensure you shut the Pi down using the `sudo halt` command. This will shut down the Pi safely and cleanly; it is generally advisable to wait for the ACT (activity) LED to stop blinking on the Pi before removing the power cable.

Remember that producing the final time-lapse film will be much quicker on a modern desktop PC. The Pi can perform the task but it will require more time for processing the film.

The image files will always remain however many times you encode the film file, so the final time-lapse film can be rebuilt as many times as is necessary. One approach might be to try different video filter scales or frame rates on each attempt. Refer to the test run section if you need a reminder of what the different parts of the avconv command mean. If encoding on the Raspberry Pi, it is recommended to first build the video with a scale video filter as in the command below;  as before, enter the entire command on one line.

```bash
avconv -r 10 -i cress_%04d.jpg -r 10 -vcodec libx264 -crf 20 -g 15 -vf scale=1296:972 cress_timelapse.mp4
```

This will take longer than the test run to finish as there are more frames to encode. When you are returned to the command prompt you can play back the film using the following command:

```bash
omxplayer cress_timelapse.mp4 -o hdmi
```

If you're happy with the way it looks, you could then rebuild the film at full resolution by leaving out the video filter part of the command. This will take a lot longer on the Pi, but the end product will look better if uploaded to social media. Here is the command:

```bash
avconv -r 10 -i cress_%04d.jpg -r 10
-vcodec libx264 -crf 20 -g 15
cress_timelapse_full.mp4
```

Once complete the full video can be played back using the following command:

```bash
omxplayer cress_timelapse_full.mp4 –o hdmi
```

## What next?

- Why not upload the video to YouTube? 
- Could you use your skills to branch out into [stop-motion animation](https://github.com/raspberrypilearning/push-button-stop-motion/)? 
