#!/usr/bin/python

# File    : portprinter.py
# Author  : Scott Pack
# Created : April 2017
# Purpose : Prints each port in a list to the screen.
#
#     Copyright (c) 2017 Scott Pack. All rights reserved.
#

ports = [22, 23, 80, 135, 137, 389, 443, 445, 636, 3389]

for port in ports:
    print 'Port Number: ' + str(port)
