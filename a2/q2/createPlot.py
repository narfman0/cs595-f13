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
				original = line.strip()
				uri = 'http://mementoproxy.cs.odu.edu/aggr/timemap/link/' + original
				r = requests.get(uri)
				print(r.content)
				count = str(len(re.findall(b'rel".*memento.*"',r.content)))
				print('Found ' + count + ' mementos for uri: ' + original)
				o.write(original + ' ' + count + '\n')
				gnuplotfile.write(count + '\n')
		call(["gnuplot", "gnuplot.config"])
