#!/usr/bin/python3
#Read graphml file representing output from NameGenWeb on facebook and produce
#gnuplot scatter plot for friend count
import xml.etree.ElementTree as ET
import sys

DEFAULT_FILE='output.graphml'
if len(sys.argv) != 2:
        print('Please pass the path to your graphml file representing ' +
                'output from NameGenWeb, defaulting to ' + DEFAULT_FILE)
        path=DEFAULT_FILE
else:
        path=sys.argv[1]

root=ET.parse(path).getroot()
d={}
missing=0
for node in root.findall('node'):
    friend_count=-1
    name=''
    for data in node.iter('data'):
        if data.attrib['key']=='friend_count':
            friend_count=int(data.text)
        if data.attrib['key']=='Label':
            name=data.text
    if friend_count == -1:
        print(name + ' does not share friend count publicly!')
        missing+=1
    else:
        d[name]=friend_count

print('Missing: ' + str(missing))
with open('output.gnuplot', mode='w') as f:
    for entry in sorted(d.items(), key=lambda x: x[1]):
        value=str(entry[1])
        f.write(value + ' ' + value + '\n')
        print(entry)