## Creating a time-lapse video

Once the image sequence has been captured, you need to stitch the images together to form a film file that can be played back. There's a set of tools called ffmpeg that you can use for this.

--- task ---

Open a terminal and make sure you are in the directory with all your images. Then type:

```bash
ffmpeg -r 10 -i image%04d.jpg -r 10 -vcodec libx264 -crf 20 -g 15 timelapse.mp4
```

--- /task ---

The `-r` specifies the video frame rate. Here we're using 10 frames a second; this is adequate for a time-lapse film. It's used twice to avoid ffmpeg dropping similar-looking frames. The `-i` is the input filename; notice the `%04d`. This is because your images have names with 4-digit numbers in them.

The `-vcodec` specifies the codec (encode/decode) format of the video you're making. We've specified H264; YouTube uses this codec for streaming. The `-crf` specifies the compression quality level. 20 is an average value; lower numbers give higher quality but also increase file size. The `-g` specifies the GOP value; this is needed if you upload the video to YouTube later.

Once the encoding process has finished, you'll be returned to the command prompt. It may take a while to finish so be patient; maybe it's time for a cup of tea. When the process has completed, you can use the command below to play back the film on the Raspberry Pi, using the VLC media player.


