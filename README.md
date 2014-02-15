Cress Egg Heads
===============

Time lapse photography with the Raspberry Pi Camera Board

![image](./images/cover.jpg "Cover Image")

##Lesson objective
* Understand what time lapse photography is
* Understand how cress seeds germinate and grow
* Understand how to make a time lapse film

##Lesson outcome
* To have grown some cress from seeds
* To have made one or more cress egg heads
* To have recorded a time lapse film of them growing over a period of 1 week
* To play back the time lapse film and see the cress growing rapidly

##Time
*	1-2 hour initially for setting up
*	Further attendance spread over 1 week (or so) as the cress grows
*	1 hour to wrap up

##Requirements
*	An area with sunlight that can be left undisturbed for long periods of time
*	Eggs
*	Saucepan to boil the eggs in
*	Egg cup holders
*	Cotton wool
*	Washing up liquid and bowl
*	Pencils or crayons
*	Kitchen roll
*	1 x Flip book (if possible, can be about anything)
*	1 x Dinner knife
*	1 x Tea Spoon
*	1 x Plate
*	1 x Plastic Spray Bottle with Trigger
*	1 x Packet of cress seeds
*	1 x Raspberry Pi
*	1 x SD card (with latest Raspbian installed)
*	1 x Monitor + cables
*	1 x USB Keyboard
*	1 x Raspberry Pi Camera Board
*	1 x Camera Board 360 Gooseneck Mount (from modmypi.com)

##Introduction
Ideally begin with a discussion of how plants germinate from seeds and that they need to sense the correct conditions in order to start growing.  Usually moisture and the right temperature.

Next discuss the speed at which plants grow.  They grow far too slowly for us to see it happening.  However there is a trick that we can use to speed up time and see it!

![image](./images/intro-flip-book.jpg "Disney Flip Book")

A useful prop to bring out now is a flip book.  A flip book contains a series of pictures that change gradually from one page to the next.  When the pages are turned rapidly the picture appears to move.  This is the fundamental principle behind all TV cartoons and film footage.

Explain that if you were to capture images of the same landscape every hour for a day, you would end up with 24 pictures.  If you were to play back (flip through) those images at normal film speed it will appear that time is moving very fast.  You would see the sun rise, move through the sky and set in just a few moments.  This is what we call a time lapse film.

Wrap up by explaining that if we make cress egg heads we can use the technique of time lapse photography to speed up time see the hair (cress) appearing to grow.  The only trouble is we need to let the time elapse and do the work of capturing the images along the way.  This is where the Raspberry Pi comes in.  First you’ll need to make some cress egg heads though!

##Making a cress egg head

Begin by soft boiling the egg in a saucepan.  Take care to avoid splashing hot water and burning yourself.  Boil for no more than 3 minutes.  Remove the egg using the spoon and allow to cool before handling.

Remove the top of the egg with the knife, as you would if you were going to eat it.  Take care to avoid cracking the remaining shell of the egg.

Use the spoon to scoop out all of the cooked egg from the inside the eggshell.  Your aim is to have a completely empty shell, don’t worry if you spill some yolk on the outside.

Use the washing up liquid and bowl to wash the eggshell inside and out.  Just use your fingers and take care to avoid cracking the shell, be gentle and careful with it.  Make sure there is no dried yolk on the outside.

Leave the egg to dry on some kitchen roll.

Once the egg has dried you can use the crayons and pencils to decorate it - carefully.  Remember that the hole will be facing upwards so bear this in mind if you want to draw a face.

Fill the eggs, to the top, with cotton wool and dampen with water.  Top up with extra cotton wool and dampen again if necessary.  The cotton wool should reach the top of the hole in the eggshell.

![image](./images/making-cress-egg-head.jpg "Cress Egg Head")

Place the egg into an egg cup, then place the egg cup onto a plate.

Use finger and thumb to sprinkle some cress seeds onto the cotton wool, the plate will catch any that miss.  That’s it, the egg head is now ready to grow.  Place the egg cup in a place where it will catch sunlight during the day.

##Setting up the Camera Board

Follow the official instructions [here](http://www.raspberrypi.org/camera "Camera | Raspberry Pi") to setup and test the Raspberry Pi Camera Board.

Next set up the 360 Gooseneck Mount.  This will allow you to aim the camera at the cress egg heads and hold it steady for the duration of the time lapse recording.

![image](./images/camera-mount.jpg "Camera Board 360 Gooseneck Mount")

One end of this inserts into the headphone jack on the Pi (it just uses this to hold itself and does nothing to the audio jack), the other end is a screw with a couple of plastic washers that secure the camera board to the gooseneck. 

Unless you previously changed it you should login to the Pi with the default username `pi` and the password `raspberry`.

You will find yourself at the prompt below.  If you have configured your Pi to automatically go into the desktop interface, use the start button to logout of the desktop.

`pi@raspberrypi ~ $ _`

You can take a still image using the following command.

`raspistill –o test.jpg –t 5000`

This will take a still image and save it to a file called `test.jpg` after a five second delay.  The `–o` means output and the `–t` again means time.  Here we’re specifying 5000 milliseconds or 5 seconds.

If you now use the `ls` command you’ll see the file `test.jpg` is shown in the list.  Clearly it would be too laborious for a person to sit in front of the Raspberry Pi for a whole week (day and night) running this command every hour.  Fortunately there is a way to automate this process which will allow the Raspberry Pi to record the time lapse film completely unattended.
