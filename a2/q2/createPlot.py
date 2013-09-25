#!/bin/python3
import requests
import sys
from subprocess import call
import re

input = sys.argv[1]
with open(input, 'rU') as f:
	with open('mementoCount.txt', 'w') as o:
		with open('gnuplot.dat', 'w') as gnuplotfile:
			for line in f:
				uri = 'http://mementoproxy.cs.odu.edu/aggr/timemap/link/' + line.strip()
				r = requests.get(uri)
				count = str(len(re.findall(b'rel".*memento.*"',r.content)))
				print('Found ' + count + ' mementos for uri: ' + uri)
				o.write(line.strip() + ' ' + count + '\n')
				gnuplotfile.write(count + '\n')
		call(["gnuplot", "gnuplot.config"])
