from picamzero import Camera

cam = PiCamera()
cam.capture_sequence("cress.jpg", num_images=24, interval=3600, make_video=True)
