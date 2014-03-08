#!/bin/python3
import sys

HEADER_LINES=8
DEFAULT_INPUT='zachary.dat'
DEFAULT_OUTPUT='zachary.json'
if len(sys.argv) != 2:
    print('Pass the path to your input dat then output json file. ' +
        'Defaulting to input:' + DEFAULT_INPUT + ' output:' + 
        DEFAULT_OUTPUT)
    input=DEFAULT_INPUT
    output=DEFAULT_OUTPUT
else:
    input=sys.argv[1]
    output=sys.argv[2]

def writeNodes(o, count):
    o.write('{\n  "nodes":[\n')
    for x in range(0, count+1):
        o.write('    {"name":"'+str(x)+'","group":'+str(x)+'}')
        if x != count:
            o.write(',')
        o.write('\n')
    o.write('  ],\n  "links":[\n')

with open(output, 'w') as o:
  with open(input) as f:
    lineNumber=0
    currentPerson=0
    for line in f:
        lineNumber += 1
        if(lineNumber == HEADER_LINES):
            total=len(line.strip().split(' '))-1
            print('Total entries: ' + str(total))
            writeNodes(o, total)
        elif(lineNumber > HEADER_LINES and 
             lineNumber > HEADER_LINES + total):
            currentPersonConnections = []
            for connection in line.strip().split(' '):
                currentPersonConnections.append(int(connection))
            currentConnection=0
            for connection in currentPersonConnections:
                if currentConnection > currentPerson and connection > 0:
                    o.write('    {"source":' + str(currentPerson) + ',
                        "target":' + str(currentConnection) + ',"value":' +
                        str(connection)+'},\n')
                currentConnection+=1
            currentPerson+=1
    o.write('  ]\n}')
