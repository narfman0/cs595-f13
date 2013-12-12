import docclass
import os
import sys
import traceback

DATABASE_NAME='sqlite.db'

def read(classifier,titleClassification):
  i=1
  predictionList=[]
  for title,body,feature,category in titleClassification:
    try:
      predictedCategory=str(classifier.classify(body))
    except:
      print('Error calculating ' + title)
      traceback.print_exc()
      sys.exit(0)
    if(i <= len(titleClassification)/2):
      classifier.train(body, category)
      cp=-1
    else:
      cp=round(classifier.cprob(feature,predictedCategory),3)
    print('#' + str(i) + ' Title: ' + title + ' Feature: ' + feature + 
          ' Predicted: ' + predictedCategory + 
          ' Actual: ' + category + ' CProb: ' + str(cp))
    predictionList.append((title, feature, predictedCategory, category, cp),)
    i+=1
  return predictionList

def tex(string):
  return '\\tiny ' + string.replace('&','\&').replace('#','\#')

def writeClassificationResultsLatex(predictionList):
  with open('classificationResults.tex', 'w') as f:
    f.write('\\begin{tabular}{ l l l l l }\n')
    f.write('\\tiny Title & \\tiny Feature & \\tiny Predicted & \\tiny Category & \\tiny CP \\\\ \n')
    for title, feature, predictedCategory, category, cp in predictionList:
      f.write(tex(title) + '&' + tex(feature) + '&' + tex(predictedCategory) + 
              '&' + tex(category) + '&' + tex(str(cp)) + '\\\\ \n')
    f.write('\\end{tabular}\n')

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
        titleClassificationDict.append((title,body,feature.strip(),
                                        category.strip()),)
      except:
        print('Error parsing entry: ' + str(entry))
  predictionList=read(classifier,titleClassificationDict)
  writeClassificationResultsLatex(predictionList)
