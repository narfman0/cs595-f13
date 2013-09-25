#!/bin/python2
import sys
from local import carbonDate
import datetime

#Split a string date in the form 2004-12-08T03:56:43
def getDays(input):
	date = input.split('T')[0]
	now = datetime.datetime.now()
	print(now)
	days = (now.year - int(date.split('-')[0])) * 365.242
        days = (now.month - int(date.split('-')[1])) * 365.242/12 + days
	days = (now.day - int(date.split('-')[2])) + days
	return int(days)

if __name__ == "__main__":
	input = sys.argv[1]
	with open(input, 'r') as f:
		with open('gnuplot.dat', 'w') as o:
			for line in f:
				mementoCount = int(line.split(' ')[1])
				if not mementoCount == 0:
					uri = line.split(' ')[0]
					earliest = carbonDate(uri)
					days = getDays(earliest)
					o.write(str(mementoCount) + " " + str(days) + '\n')
					exit
				else:
					print('Skipping uri ' + line.split(' ')[0])
