import docclass
import os
import sys
import traceback

DATABASE_NAME='sqlite.db'

def read(classifier,titleClassification):
  i=1
  for title,body,feature,category in titleClassification:
    try:
      predictedCategory=str(classifier.classify(body))
    except:
      print('Error calculating ' + title)
      traceback.print_exc()
      sys.exit(0)
    if(i <= len(titleClassification)/2):
      classifier.train(body, category)
      classifier.insert(i, title, None, predictedCategory, category, None)
      cp=-1
    else:
      cp=round(classifier.cprob(feature,predictedCategory),3)
      try:
        classifier.insert(i, title, feature, predictedCategory, category, cp)
      except:
        print('Fail for values')
    print('#' + str(i) + ' Title: ' + title + ' Feature: ' + feature + ' Predicted: ' + predictedCategory + 
          ' Actual: ' + category + ' CProb: ' + str(cp))  
    i+=1

if __name__ == '__main__':
  try:
    os.remove(DATABASE_NAME)
  except:
    pass
  classifier=docclass.fisherclassifier(docclass.getwords)
  classifier.setdb(DATABASE_NAME)
  titleClassificationDict=[]
  with open('titles.txt') as f:
    for entry in f:
      try:
        title,body,feature,category=entry.split('|')
        title=title.strip().replace("'",'')
        titleClassificationDict.append((title,body,feature.strip(),category.strip()),)
      except:
        print('Error parsing entry: ' + str(entry))
  read(classifier,titleClassificationDict)
