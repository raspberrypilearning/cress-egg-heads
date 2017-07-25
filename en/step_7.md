## Setting up for the real time-lapse

Before you start time-lapse recording the cress egg heads, there are several things you should consider. The most important is the physical location where the recording will take place. This needs to be somewhere warm with sunlight that can be left **undisturbed** for a whole week; a classroom windowsill might not be ideal. Even slight movements will be noticeable in the final cut.

Having an electric light source on the cress egg heads will allow growth to be recorded at night, and will make for a nicer end result. Without this setup, the recording will switch abruptly between light and darkness.

If you're using a fresh SD card with Raspbian installed this next part can be ignored, otherwise space on the SD card should also be taken into consideration. If you run out of free space halfway through the week, some footage will be lost. This can be predicted with a simple calculation to ensure there's enough free space on the SD card before starting.

- The first thing to do is to check the size of the images your camera has been taking. The Pi camera image size will default to your screen resolution unless told otherwise, so image sizes may vary.

    To check the size of an image, open a terminal and type the following command:

    ``` bash
    du -h image0001.jpg
    ```

    You should get something that looks like this:

    ``` bash
    4024	image0001.jpg
    ```

    The number on the right is the number of kilobytes of space the image takes up.

- Next, you can see how much space you have left on your micro SD card, by typing:

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

