#!/usr/bin/python3
import urllib.request
from urllib.parse import urlparse
import os
import sys
DEFAULT_PATH='../q1/results'

# read path or use default
def getPath():
	if len(sys.argv) != 2:
        	print('Please pass the path to the directory containing files representing parsed links. Defaulting to ' + DEFAULT_PATH)
	        return DEFAULT_PATH
	else:
        	return sys.argv[1]

#create dot-friendly string for the file given in path
def getDOTString(path):
	i=0
	output=''
	with open(path) as f:
		for line in f:
			if i == 1:
				original=line.strip()
			elif i > 2:
				outputAppend = original + ' -> ' + line.strip() + ';'
				output=output + outputAppend + '\n'
			i+=1
	return output

def createDOT(path):
	with open('graph.dot', 'w') as o:
		o.write('digraph graph {\n')
		for filename in os.listdir(path):
			filepath=path + '/' + str(filename)
			dotString=getDOTString(filepath)
			o.write(dotString)
			print('Processed ' + filepath + ': \n' + dotString)
		o.write('}')

path=getPath()
createDOT(path)
