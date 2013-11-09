#!/usr/bin/python2
import recommendations

#Return prettier string representing a set of movie/rating pairs
def stringifyTuple(tuple):
    string=''
    for x in range(0,len(tuple)/2):
        string+=str(tuple[x*2]) + ' '
        string+=str(tuple[x*2+1]) + '\n'
    return string

prefs=recommendations.loadMovieLens()
print('Top 5 average score movies:\n' + stringifyTuple(recommendations.getTop5Movies(prefs)))
