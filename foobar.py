#!/usr/bin/env python
# encoding: utf-8

import sys
import time

lines = []

for filename in sys.argv[1:]:
	f = open(filename, "r")
	for l in f:
		logline = l.replace(",", " ").split()
		logline = [filename] + logline
		logline[2] = time.strptime(" ".join([logline[1], logline[2].partition(".")[0]]), "%Y-%m-%d %H:%M:%S")
		lines.append(logline)

#lines now has same format like log file except timestamp
lines = sorted(lines, lambda x, y: cmp(x[2], y[2]))

lines = [val for val in lines if len(val) > 8 and val[1] == "2011-05-24" and val[8] == "00:1f:1f:09:08:7b"]
lines = [(val[0].lstrip("logs/").rstrip("/des-hello.log"), val[2], val[-5], val[-2]) for val in lines]

#lines now has format (location, time, rssi, packet_count)
lines = [x for x in lines if int(x[3]) > 30]

timehash = {}

for line in lines:
	snapshot = (line[0], line[2], line[3])
	if line[1] in timehash:
		timehash[line[1]].append(snapshot)
	else:
		timehash[line[1]] = [snapshot]

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

first, _ = sorted(timehash.iteritems())[0]
last, _ = sorted(timehash.iteritems())[-1]

timeline = []

for count, frame in enumerate(sorted(timehash.iteritems())):
	k, v = frame
	#print count
	filename = "build/%05d.svg" % count
	#out = open(filename, "w")
	#out = open("temp.svg", "w")
	out = sys.stdout
	out.write("""\
<svg xmlns=\"http://www.w3.org/2000/svg\" version=\"1.0\" width=\"800\" height=\"450\">
	<defs>
		<style type="text/css"><![CDATA[
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
			}\n""")
	for node in v:
		out.write("\t\t\tcircle." + node[0] + " {\n\t\t\t\tfill-opacity: " + str((float(node[1])+90) / 50) + ";\n\t\t\t}\n")
	out.write("""\
		]]></style>
	</defs>
	<rect x="0" y="0" width="800" height="450" stroke="none" fill="white"/>
	<g transform="scale(0.5)">
	""")
	for p in places:
		cat = p[0]
		if p[0].startswith("t9-k"):
			cat += " t9-k"
		if p[0].startswith("t9-0"):
			cat += " t9-0"
		if p[0].startswith("t9-1"):
			cat += " t9-1"
		out.write("\t<circle class=\"" + cat + "\" cx=\"" + p[1] + "\" cy=\"" + p[2] + "\" r=\"17\"/>\n")
	out.write("<text x=\"10\" y=\"10\">" + str(count) + "</text>\n")
	out.write("""</g>""")
	out.write("""</svg>""")
	#out.close()

