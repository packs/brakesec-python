#!/usr/bin/python

# File    : storyteller.py
# Author  : Scott Pack
# Created : April 2017
# Purpose : A "choose your own adventure" script that prints a one paragraph
#           story to the screen based on the input provided by the user
#           (format string operations)
#
#     Copyright (c) 2017 Scott Pack. All rights reserved.
#

print 'Shakespeare Yourself!'
name = raw_input('Name: ')
friend = raw_input('Friend: ')

print "Alas, poor %s! I knew him, %s: a fellow of infinite jest, of most \
excellent fancy: he hath borne me on his back a thousand times; and now, how \
abhorred in my imagination it is!" % (name, friend)
