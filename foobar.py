#!/usr/bin/env python
# encoding: utf-8

import sys
import time
import os.path

#a linear list of all samples of all nodes
loglines = []

for logfilepath in sys.argv[1:]:
	logfile = open(logfilepath, "r")
	
	#assumption: the name of the innermost directory in logfilepath is node name
	dirpath, filename = os.path.split(logfilepath)
	_, nodename = os.path.split(dirpath)
	for line in logfile:
		#break the line in tokens on comma and whitespace
		logline = line.replace(",", " ").replace(" | ", " ").split()
		#prepend the node name to the log line
		logline = [nodename] + logline
		#convert the time string to seconds since epoch
		logline[2] = time.strptime(" ".join([logline[1], logline[2].partition(".")[0]]), "%Y-%m-%d %H:%M:%S")
		logline[2] = time.mktime(logline[2])
		logline[2] = int(logline[2])
		loglines.append(logline)

#lines now has same format like log file except timestamp
#lines = sorted(lines, lambda x, y: cmp(x[2], y[2]))

#filter out any non-sample log lines
#FIXME: sample log lines should contain magic for easier recognition
loglines = filter(lambda line: len(line) > 4 and "log_neighbour@dessert_monitor" in line[4], loglines)

samples = []

class Sample:
	pass

#SELECT nodeName, timestamp, rssi, packetCount FROM loglines
for line in loglines:
	sample = Sample()
	sample.node = line[0]
	sample.time = line[2]
	sample.rssi = int(line[-5])
	sample.count = int(line[-2])
	samples.append(sample)


#TODO: filter samples to just the ones needed, e.g. certain day, minimal rssi etc.
#samples = filter(lambda sample: sample.count > 5, samples)
samples = filter(lambda sample: sample.time >= 1306235203, samples)

times = [sample.time for sample in samples]
earliest = min(times)
latest   = max(times)

places = [
#("a3-005", "4000", ""),
#("a3-010", "", ""),
#("a3-012", "", ""),
#("a3-020", "", ""),
#("a3-020a", "", ""),
#("a3-022", "", ""),
#("a3-023", "", ""),
#("a3-024", "", ""),
#("a3-025", "", ""),
#("a3-106", "", ""),
#("a3-119", "", ""),
#("a3-201", "", ""),
#("a3-206", "", ""),
#("a3-210", "", ""),
#("a6-005", "", ""),
#("a6-008", "", ""),
#("a6-009", "", ""),
#("a6-010", "", ""),
#("a6-011", "", ""),
#("a6-015", "", ""),
#("a6-016", "", ""),
#("a6-017", "", ""),
#("a6-026a", "", ""),
#("a6-026b", "", ""),
#("a6-028", "", ""),
#("a6-031", "", ""),
#("a6-032a", "", ""),
#("a6-032b", "", ""),
#("a6-102", "", ""),
#("a6-107", "", ""),
#("a6-108a", "", ""),
#("a6-108b", "", ""),
#("a6-115", "", ""),
#("a6-122", "", ""),
#("a6-123", "", ""),
#("a6-124", "", ""),
#("a6-126", "", ""),
#("a6-127", "", ""),
#("a6-139", "", ""),
#("a6-141", "", ""),
#("a6-205", "", ""),
#("a6-207", "", ""),
#("a6-208", "", ""),
#("a6-212a", "", ""),
#("a6-213", "", ""),
#("a6-214", "", ""),
#("a6-215", "", ""),
#("a6-ext-114", "", ""),
#("a6-ext-139", "", ""),
#("a6-ext-201", "", ""),
("t9-004a", "793", "558"),
("t9-004b", "859", "555"),
("t9-004c", "816", "447"),
("t9-006", "337", "700"),
("t9-007", "135", "747"),
("t9-009", "132", "597"),
("t9-011", "130", "450"),
("t9-018", "307", "147"),
("t9-020", "307", "301"),
("t9-022a", "306", "441"),
("t9-035", "1350", "582"),
("t9-040", "1338", "150"),
("t9-105", "552", "805"),
("t9-106", "478", "804"),
("t9-108", "327", "804"),
("t9-111", "118", "753"),
("t9-113", "124", "603"),
("t9-117", "127", "307"),
("t9-124", "304", "463"),
("t9-134", "727", "622"),
("t9-136", "903", "510"),
("t9-137", "903", "624"),
("t9-146", "1320", "544"),
("t9-147", "1320", "453"),
("t9-148", "1320", "385"),
("t9-149", "1320", "306"),
("t9-150", "1320", "231"),
("t9-154", "1500", "310"),
("t9-155", "1500", "382"),
("t9-157t", "1500", "532"),
("t9-158", "1500", "606"),
("t9-160", "1500", "756"),
("t9-162", "1365", "805"),
("t9-163", "1300", "805"),
("t9-164", "1225", "805"),
("t9-165", "1150", "805"),
("t9-166", "1077", "805"),
("t9-169", "847", "805"),
("t9-ext-110", "124", "865"),
("t9-ext-121", "295", "196"),
("t9-ext-150", "1338", "195"),
("t9-ext-154", "1560", "309"),
("t9-k21a", "304", "195"),
("t9-k21b", "304", "244"),
("t9-k23", "304", "350"),
("t9-k36a", "729", "541"),
("t9-k36b", "733", "438"),
("t9-k38", "735", "340"),
("t9-k40", "735", "190"),
("t9-k44", "909", "186"),
("t9-k46", "909", "340"),
("t9-k48a", "909", "436"),
("t9-k48b", "909", "532"),
("t9-k60a", "1338", "507"),
("t9-k60b", "1338", "435"),
("t9-k61", "1338", "381"),
("t9-k63", "1338", "200")]

walk = [["00:00:00", 733, 350],
        ["13:09:00", 733, 350],
        ["13:09:40", 724, 714],
        ["13:10:10", 724, 714],
        ["13:10:34", 724, 714],
        ["13:10:46", 909, 700],
        ["13:11:04", 1420, 670],
        ["13:11:24", 1410, 531],
        ["13:12:00", 1411, 306],
        ["13:12:15", 1467, 219],
        ["13:12:32", 1422, 156],
        ["13:12:51", 1426, 586],
        ["13:13:09", 973, 585],
        ["13:13:25", 444, 517],
        ["13:13:42", 447, 583],
        ["13:14:07", 217, 477],
        ["13:14:22", 216, 115],
        ["13:14:43", 217, 112],
        ["13:15:07", 518, 76],
        ["13:15:43", 1482, 60],
        ["13:16:00", 1630, 15],
        ["13:19:17", 1630, 15],
        ["13:19:41", 17, 738],
        ["13:20:00", 724, 697],
        ["13:20:17", 474, 720],
        ["13:20:31", 210, 606],
        ["13:20:47", 210, 234],
        ["13:21:14", 210, 822],
        ["13:21:35", 550, 718],
        ["13:21:55", 810, 550],
        ["13:22:15", 1150, 720],
        ["13:22:30", 1410, 610],
        ["13:22:40", 1410, 530],
        ["13:23:30", 1500, 530],
        ["23:59:59", 1500, 530]];

for w in walk:
	w[0] = time.mktime(time.strptime("2011-05-24 %s" % w[0], "%Y-%m-%d %H:%M:%S")) - 55

svgHeader = \
"""<svg xmlns=\"http://www.w3.org/2000/svg\" version=\"1.0\" width=\"800\" height=\"450\">
	<defs>
		<style type="text/css">
			<![CDATA[
"""

staticCSS = """\
			circle {
				fill: blue;
				stroke: grey;
				stroke-width: 3px;
				stroke-opacity: 1;
				fill-opacity: 0;
			}
			circle.t9-k {
				fill: red;
			}
			circle.t9-0 {
				fill: green;
			}
			cirlce.t9-1 {
				fill: blue;
			}
"""

for time in range(earliest, latest+1):
	filename = "build/%012d.svg" % time
	out = open(filename, "w")
	out.write(svgHeader)
	out.write(staticCSS)
	
	prev_time, walk_prev_x, walk_prev_y = max(filter(lambda w: w[0] <= time, walk))
	next_time, walk_next_x, walk_next_y = min(filter(lambda w: w[0] > time, walk))
	snapshot = filter(lambda sample: time == sample.time, samples)
	
	for sample in snapshot:
		out.write("\t\t\tcircle." + sample.node + " {\n\t\t\t\tfill-opacity: " + str((sample.rssi+90.0) / 50.0) + ";\n\t\t\t}\n")
	out.write("""\
			]]>
		</style>
	</defs>
	
	<g transform="scale(0.5)">
		<rect x="0" y="0" width="1600" height="900" stroke="none" fill="white"/>
		<g transform="translate(0, 85)">
		<path style="fill: none; stroke: grey; stroke-width: 2px" d="M72 780, 72 78, 370 78, 370 550, 670 550, 670 108, 970 108, 970 550, 1270 550, 1270 108, 1570, 108, 1570 780 z"/></g>
""")
	for p in places:
		cat = p[0]
		if p[0].startswith("t9-k"):
			cat += " t9-k"
		if p[0].startswith("t9-0"):
			cat += " t9-0"
		if p[0].startswith("t9-1"):
			cat += " t9-1"
		if "-ext-" in p[0]:
			cat += " ext"
		#print [s.node for s in snapshot]
		sample = filter(lambda sample: sample.node == p[0], snapshot)
		#print p, sample
		radius = 2
		
		if(len(sample)):
			radius = sample[0].count
		out.write("\t\t<circle class=\"" + cat + "\" cx=\"" + p[1] + "\" cy=\"" + p[2] + "\" r=\"" + str(radius) + "\"/>\n")
	
	interval = next_time - prev_time
	progress = (time - prev_time) / interval
	walk_x = (1 - progress) * walk_prev_x + progress * walk_next_x
	walk_y = (1 - progress) * walk_prev_y + progress * walk_next_y
	out.write("<g transform=\"translate(" + str(walk_x) + ", " + str(walk_y) + ")\">\n")
	out.write("""<path style="fill: purple; fill-opacity: 0.5; stroke: none" d="M-25 0 L 0 25 L 25 0 L 0 -25 z"/>""")
	out.write("</g>")
	out.write("\t\t<text style=\"font-size:20px\" x=\"10\" y=\"10\">" + str(time) + "</text>\n")
	out.write("\t</g>\n")
	out.write("</svg>\n")
	out.close()

