all: anim.mp4

clean:
	rm -f anim.mp4

anim.mp4: logs/*/des-hello.log
	echo $|
	./foobar.py $^ | gst-launch fdsrc fd=0 ! "image/svg,framerate=15/1" ! rsvgdec ! videoparse width=800 height=450 format="bgra" framerate=15 ! ffmpegcolorspace ! x264enc bitrate=1000 ! mp4mux ! filesink location=$@
