#!/usr/bin/python
import docclass

preclassified=[]
postclassified=[]
classifications=set()
cl=docclass.fisherclassifier(docclass.getwords)
cl.setdb('')
with open('titles.txt') as f:
  for line in f:
    if '|' in line:
      title,substring,classification=line.split('|')
      preclassified.append((title,substring,classification))
      classifications.update(classification)
      cl.train(title,classification)
    else:
      title=line.strip()
      print('cprob for ' + title + ': ')
      for classification in classifications:
        print(classification + ': ' + cl.cprob(title,classification))
