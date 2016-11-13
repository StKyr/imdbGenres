
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#                                                                     #
# This is the configuration file of the script.                       #
# Its purpose is to be imported so that variables to be used.         #
#                                                                     #
# It is advisable not to change any values unless explicitly needed.  #
#                                                                     #
# This also helps fro versioning and easily updating in case of       #
# change in the host's site architecture.                             #
#                                                                     #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

if __name__ == '__main__':	                                            # this file is not designed to run as an autonomus script
	import sys
	sys.exit()

_version_                         = 1.0                                 # software version
_debug_                           = True                                # setting this true will activate debugging messages as output
                                                                        # also equivalent with '--debug' option in command line


imdb_base_url                     = "https://www.imdb.com"              # configuring imdb home page url
imdb_search_url                   = imdb_base_url + "/find"             # configuring imdb search page url

imdb_search_movie_query_parameter = 'q'                                 # name of field containing the movie title in search bar in imdb homepage
imdb_search_type_query_parameter  = 's'                                 # name of field containing the movie type in search bar in imbd homepage
imdb_earch_type_default_value     = 'all'                               # default value of movie type field

imdb_genre_page_url               = "ref_=tt_stry_gnr"                  # after some mining, it turns out all (and only) tags containing a genre have a reference there
                                                                        # So, it is the string used to locate tags that contain a genre

html_parser                       = "html.parser"                       # default system HTML/XML parser to work with BeautifulSoup library


errors = {                                                              # defining error codes and explanations for debugging

	1 : 'Corrupt Config file',
	2 : 'Library not found',
	3 : 'Name not given',
	4 : 'Year not given',
	5 : 'Title not found',
	6 : 'Page not found (404)',

	0 : 'No errors'
}
