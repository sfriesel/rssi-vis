SVGS = $(shell seq --format "build/%05g.svg" --separator " " 0 947)
PNGS := $(patsubst %.svg, %.png, $(SVGS))
#PPMS := $(patsubst %.svg, %.ppm.gz, $(SVGS))

all: anim.mp4
#inkscape -b FFFFFF -y 1 -f '$^' -e $(patsubst %.ppm.gz, %.png, $@) 1>/dev/null

#%.ppm.gz: %.svg
#	convert $^ ppm:- | gzip > $@

#anim.mp4: $(PPMS)
#	gunzip $(PPMS)
#	cat $(patsubst %.gz, %, $(PPMS)) | gst-launch-0.10 fdsrc fd=0 !  'image/ppm,width=1600,height=900,framerate=(fraction)30/1' ! ffdec_ppm !  ffmpegcolorspace ! x264enc speed-preset=10 ! mp4mux ! filesink  location=$@

clean:
	rm -f build/*.{svg,ppm,png,mp4,avi}

%.svg: foobar.stamp

foobar.stamp: foobar.py
	./foobar.py logs/*/des-hello.log
	touch foobar.stamp

%.png: %.svg
	inkscape $^ -e $@ > /dev/null
#	convert $@  -background white -flatten $@

png: $(PNGS)

anim.mp4: foobar.stamp $(PNGS)
	gst-launch multifilesrc location="build/%05d.png" caps="image/png,framerate=30/1" ! pngdec ! ffmpegcolorspace ! ffenc_mpeg4 bitrate=2000000 ! mp4mux ! filesink location=$@
