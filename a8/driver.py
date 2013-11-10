#!/usr/bin/python2
import recommendations

#Return prettier string representing a set of movie/rating pairs
def stringify(movieData):
    string=''
    for x in range(0,len(movieData)/2):
        string+=str(movieData[x*2]) + ' '
        string+=str(movieData[x*2+1]) + '\n'
    return string

prefs=recommendations.loadMovieLens()
#print 'Top 5 average score movies:\n' + stringify(recommendations.getTop5Movies(prefs))
#print 'Top 5 movie rating counts:\n' + stringify(recommendations.getTop5MovieRatingCounts(prefs))
#print 'Top 5 movie rating by women:\n' + stringify(recommendations.getTop5MoviesWomen(prefs))
#print 'Top 5 movie rating by men:\n' + stringify(recommendations.getTop5MoviesMen(prefs))
#print 'Most similar ot Top Gun: ' + stringify(recommendations.getSimilarRatings(prefs,"Top Gun (1986)",True))
#print 'Least similar ot Top Gun: ' + stringify(recommendations.getSimilarRatings(prefs,"Top Gun (1986)",False))