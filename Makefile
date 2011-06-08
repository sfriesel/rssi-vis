all: anim.mp4

clean:
	rm -f build/*.{svg} anim.mp4

foobar.stamp: foobar.py
	./foobar.py logs/*/des-hello.log
	touch foobar.stamp

anim.mp4: foobar.stamp
	gst-launch multifilesrc location="build/%012d.svg" index=1306235203 ! "image/svg+xml,width=800,height=450,framerate=10.0" ! rsvgdec ! videoparse width=800 height=450 framerate=10 format=rgba ! ffmpegcolorspace ! x264enc ! mp4mux ! filesink location=$@

.PHONY: clean
