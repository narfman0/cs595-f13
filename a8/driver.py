#!/usr/bin/python2
import recommendations

#Return prettier string representing a set of movie/rating pairs
def stringify(movieData):
    string=''
    for item in movieData:
        for x in range(0,len(item)):
            string+=str(item[x]) + ' '
        string+='\n'
    return string + '\n'

prefs=recommendations.loadMovieLens()
print 'Top 5 average score movies:\n' + stringify(recommendations.getTop5Movies(prefs))
print 'Top 5 movie rating counts:\n' + stringify(recommendations.getTop5MovieRatingCounts(prefs))
print 'Top 5 movie rating by women:\n' + stringify(recommendations.getTop5Movies(prefs,'F'))
print 'Top 5 movie rating by men:\n' + stringify(recommendations.getTop5Movies(prefs,'M'))
print 'Most similar ot Top Gun: ' + str(recommendations.getSimilarRatings(prefs,"Top Gun (1986)",True))
print 'Least similar ot Top Gun: ' + str(recommendations.getSimilarRatings(prefs,"Top Gun (1986)",False))
print 'Top 5 raters:\n' + stringify(recommendations.getTop5Raters(prefs))
print '5 most similar raters:\n' + stringify(recommendations.get5SimilarRaters(prefs))
print '5 least similar raters:\n' + stringify(recommendations.get5SimilarRaters(prefs, similar=False))
print 'Top 5 movie rating men over 40:\n' + stringify(recommendations.getTop5Movies(prefs,'M','O'))
print 'Top 5 movie rating men under 40:\n' + stringify(recommendations.getTop5Movies(prefs,'M','U'))
print 'Top 5 movie rating women over 40:\n' + stringify(recommendations.getTop5Movies(prefs,'F','O'))
print 'Top 5 movie rating women under 40:\n' + stringify(recommendations.getTop5Movies(prefs,'F','U'))