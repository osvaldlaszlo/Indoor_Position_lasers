
from __future__ import division
from numpy import pi


def deg2rad(arr): 
	for i in xrange(len(arr)):
		arr[i] = float(arr[i])*pi/180
	return arr

def rad2deg(arr): 
	for i in xrange(len(arr)):
		arr[i] = float(arr[i])*180/pi
	return arr

def deg2radf(a): 
	return float(a)*pi/180

def rad2degf(a): 
	return float(a)*180/pi


