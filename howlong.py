#!/usr/bin/env python
#  _    _               _                         _____       
# | |  | |             | |                       |  __ \      
# | |__| | _____      _| |     ___  _ __   __ _  | |__) |   _ 
# |  __  |/ _ \ \ /\ / / |    / _ \| '_ \ / _` | |  ___/ | | |
# | |  | | (_) \ V  V /| |___| (_) | | | | (_| |_| |   | |_| |
# |_|  |_|\___/ \_/\_/ |______\___/|_| |_|\__, (_)_|    \__, |
#                                          __/ |         __/ |
#                                         |___/         |___/ 

# usage: python howlong.py [location1] [location2]
# output: <distance (km)> (newline) <time (days, hrs, mins)>

class HowLong:
	'''
	data members
	'''
	LOCATION1 = ""
	LOCATION2 = ""
	MATRIXURI = "https://maps.googleapis.com/maps/api/distancematrix/json"

	'''
	@name __init__ (constructor)
	@params location1, location2
	'''
	def __init__(self, location1, location2):
		self.LOCATION1 = location1.replace(" ", "+")
		self.LOCATION2 = location2.replace(" ", "+")

	'''
	@name execute
	@algorithm fetch data from distancematrix uri with locations params and return distance
			   and time to travel from one place to another.
	'''
	def execute(self):
		# import requests library for easy access
		import requests
		uridata = {
			'units':'metric',
			'origins':self.LOCATION1,
			'destinations':self.LOCATION2
		}
		response = requests.get(self.MATRIXURI, params=uridata)
		print response.json()


def main():
	import sys
	try:
		location1, location2 = sys.argv[1], sys.argv[2]
	except IndexError:
		raise SystemExit('Please provide both the locations')
	
	howlong = HowLong(location1,location2)
	howlong.execute()

if __name__ == '__main__':
	main()