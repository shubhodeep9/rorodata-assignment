#!/usr/bin/env python
#    _____       ___ __               
#   / ___/____  / (_) /_  ____  __  __
#   \__ \/ __ \/ / / __/ / __ \/ / / /
#  ___/ / /_/ / / / /__ / /_/ / /_/ / 
# /____/ .___/_/_/\__(_) .___/\__, /  
#     /_/             /_/    /____/   

# usage: python split.py <destination>/<filename>.<ext> <number of lines limit per file>
# output: files with contents of parent file
#			writing <destination>/<filename>-part1.<ext>
#			writing <destination>/<filename>-part2.<ext> .. so on

class Split:
	'''
	data members
	'''
	FILENAME = ""
	EXT = ""
	LINES = 0

	'''
	@name __init__ (constructor)
	@params filename lines
	'''
	def __init__(self, filename, lines):
		# split filename into filename and ext
		try:
			self.FILENAME, self.EXT = filename.split(".")
			self.LINES = lines
		except ValueError:
			raise SystemExit('Please provide file extension')

	'''
	@name execute
	@algorithm open file, convert into list of lines, create new files with sublines
	'''
	def execute(self):
		# read file line by line
		try:
			with open(self.FILENAME+'.'+self.EXT) as parent:
				listoflines = parent.readlines()
			totallines = len(listoflines)
			div = totallines/self.LINES
			if totallines % self.LINES != 0:
				div = div + 1
			for i in range(div):
				partnumber = i+1
				filecontent = ''.join(listoflines[i*self.LINES:self.LINES*(i+1)])
				# write to part-file
				partfile = open(self.FILENAME+'-part'+str(partnumber)+'.'+self.EXT, 'w')
				partfile.write(filecontent)
				print 'writing '+self.FILENAME+'-part'+str(partnumber)+'.'+self.EXT
				partfile.close()

		except IOError:
			raise SystemExit('File not present, Try Again!')

def main():
	import sys
	try:
		filename, lines = sys.argv[1], int(sys.argv[2])
	except IndexError:
		raise SystemExit('Please provide filename and number of lines')
	except ValueError:
		raise SystemExit('Please provide lines as numbers')

	split = Split(filename, lines)
	split.execute()

if __name__ == '__main__':
	main()