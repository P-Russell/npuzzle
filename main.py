#from data import Data
import sys

def main():

	if len(sys.argv) == 2:
		fd = 0
		try:
			fd = open(sys.argv[1], 'r')
			text = fd.read()
			print(text)
			fd.close()
		except OSError:
			if sys.argv[1].isdigit():
				print (sys.argv[1])
			else:
				print ("usage: main.py [path to puzzle] OR [number for size of puzzle. number + 1 must be perfect square]")
	else:
		print ("usage: main.py [path to puzzle] OR [number for size of puzzle. number + 1 must be perfect square]")


if __name__ == '__main__':
	main()