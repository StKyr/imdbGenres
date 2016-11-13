
# -*- coding: UTF-8 -*-
import sys                                                            # system library for parsing arguments and exiting
import re                                                             # system library for string compilation (?)

try:
	import mechanize                                                  # external library for emulating a web browser
	import urllib                                                     # external library for perfoming http requests
	from bs4 import BeautifulSoup                                     # external library for interfering with HTML tags
except ImportError:
	print("Error importing libraries")
	sys.exit(1)                                                       # cannot work without the libraries

imdb_base_url = "https://www.imdb.com"
imdb_search_url = imdb_base_url + "/find"

_title_ = ' '.join(sys.argv[1:-1])                                    # get movie title and year as command line arguments
_year_ = sys.argv[-1]
if _year_ == "" or _title_ == "":                                     # check for correct input
	sys.exit(2)
brsr = mechanize.Browser()                                            # initializing browser

query_parameters='?q='                                                # preparing search query
for word in _title_.split():
	query_parameters+=word+'+'
query_parameters+="%28"+str(_year_)+"%29"                             # adding year in parenthesis
query_parameters+='&s=all'                                            # adding second query parameter
brsr.open(imdb_search_url+query_parameters)                           # opening connection and recieving page code            

movieResults=[]                                                       # getting all links to movie pages
for link in brsr.links():
	if "/title/" in link.url:
		movieResults.append(link.url)

if len(movieResults)==0:                                              # error: movie not found
	print("movie not found")
	sys.exit(2)
movie_page = imdb_base_url+movieResults[0]                            # getting movie page name in imdb
page_code = urllib.urlopen(movie_page)                                # connect and get the code
soup = BeautifulSoup(page_code, "html.parser")
genreTags = soup.find_all(href=re.compile("ref_=tt_stry_gnr"))        # get all links(tags) to a genre page
genresFound = []
for genre in genreTags:
	newGenre = unicode(genre.string).strip()                          # get the genre name from the html tag
	genresFound.append(newGenre)                                      # storing for potential future use              
	print(newGenre)                                                   # output

sys.exit(0)                                                           # all done, exiting normally


