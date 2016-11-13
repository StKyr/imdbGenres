from config import *
import sys

def getTitle(argv):
	title = ' '.join(argv[1:-1])                             # title is all command line arguments joint but for the first and final
	if title == '':
		if _debug_ == True: print(errors[3])
		sys.exit(3)

	return title

def getYear(argv):
	year = argv[-1]                                         # year is the final argument
	if year == '':
		if _debug_ == True: print(errors[4])
		sys.exit(4)

	return year

def createQueryParameters(title,year):
	query = '?'+imdb_search_movie_query_parameter+'='       # format of a get request: ?variable1=words+like+this&variable2=and+so+on
	query+= title.replace(' ','+')
	query+= '%28'+year+'%29'
	query+= '&'+imdb_search_type_query_parameter+'='
	query+= imdb_earch_type_default_value
	return query


def getLinkToMoviePage(search_page_url, parameters):
	pageCode = urllib.urlopen(search_page_url+parameters)
	soup = BeautifulSoup(pageCode, html_parser)
	links = soup.findAll()

