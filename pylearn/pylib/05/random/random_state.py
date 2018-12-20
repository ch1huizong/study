#!/usr/bin/env python

import random
import os
import cPickle as pickle

if os.path.exists('state.dat'):
	print'Found state.dat,initializing random module'
	with open('state.dat') as 
