#!/Users/bayuwilson/anaconda3/bin/python

import functools
import sys

def juric_func(*arg): 
	return functools.reduce(lambda x,y:float(x)*float(y),arg)
juric_func(sys.argv[1:])
#print(sys.argv)

