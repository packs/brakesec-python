#!/usr/bin/python

# File    : maths.py
# Author  : Scott Pack
# Created : April 2017
# Purpose : A basic CLI calculator that provides the results of simple
#           mathematical equations
#
#     Copyright (c) 2017 Scott Pack. All rights reserved.
#
import math
import sys

nb = raw_input('Problem: ')

try:
    answer = eval(nb)
except:
    print 'Invalid mathematical statement'
    sys.exit(0)

print 'Answer: ' + str(answer)
