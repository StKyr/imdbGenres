

try:                      # for python v3
	pageCode = input()
except ValueError:       # for python v2
	pageCode = raw_input()


def getGenresFromPage(pageCode):
	# version 0.0
	# assuming the place of the page where genre is contained is:
	#	<div .... >
	#		<...> Genre: </...>
	#			<a href="..."> genre1 </a>...
	#			<a href="..."> genre2 </a>...
	#			...
	#
	# if this change, the script should also change.

	divItems = pageCode.split("<div")			# split the code into <div> elements
												# this will help searching
												# in case there is more than one <div>'s containing genre
												# nested <div>'s don't matter
	
	genresFound = []
												
	for div in divItems:						# search all <div>'s for the pattern

		if "Genres:" not in div:				# this <div> does not contain the genre
			continue

												# this is the right <div>
		
		ahrefs = div.split('<a href="')			# split all the references/genres into a list
		for ref in ahrefs:
			starting = ref.find('">') + 2		# where the genre starts appearing according to the pattern
			ending = ref[starting:].find("</a>")# find the end of the genre's name (first </a> after starting of the name)
			genre = ref[starting:ending]		# get the specified substring
			genresFound.append(genre)			# store it

	return genresFound

print getGenresFromPage(pageCode)	