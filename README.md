Beepy, a hideous product from http://danielthepope.blogspot.com

You are allowed to do anything with this software, but if you make any
improvements, please tell me what you did.

Requirements
	You need to have a few things installed. It's simple:
		> sudo apt-get install alsa-utils
		> sudo apt-get install mpg321
		> sudo apt-get install festival
	After rebooting (sudo reboot) enable sound output through the headphone
	jack
		> sudo modprobe snd-bcm2835
		> sudo amixer cset numid=3 1
	I have no idea what these do, I was following an online	tutorial, but it
	works.

	Before you run Beepy, open it up and modify the locations of the files.
	Also open /etc/profile and add the location of Beepy followed by &.
	e.g.
	/home/pi/apps/alarm/beepy.py &

	Also, make sure beepy.py has executable permissions.
	> chmod 744 beepy.py
	
That's all. Enjoy!