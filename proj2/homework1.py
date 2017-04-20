#!/usr/bin/python

# File    : homework1.py
# Author  : Scott Pack
# Created : April 2017
# Purpose : Convert the scripts generated during Day One homework into separate
#           functions, combine them into one script, and execute them in order.
#
#     Copyright (c) 2017 Scott Pack. All rights reserved.
#
import math
import sys
import argparse
import getpass


def maths():
    problem = raw_input('Problem: ')

    try:
        answer = eval(problem)
    except:
        print 'Invalid mathematical statement'
        sys.exit(0)

        print 'Answer: ' + str(answer)


def passchecker(password):
    secret = 'r)FeGEw4MLgL'

    if password is None:
        password = getpass.getpass()
    else:
        password = password

    if password == secret:
        print 'Access Granted'
    else:
        print 'Access Denied'


def storyteller():
    print 'Shakespeare Yourself!'
    name = raw_input('Name: ')
    friend = raw_input('Friend: ')

    print "Alas, poor %s! I knew him, %s: a fellow of infinite jest, of most \
    excellent fancy: he hath borne me on his back a thousand times; and now, \
    how abhorred in my imagination it is!" % (name, friend)


parser = argparse.ArgumentParser(description='Combined Homework 1 Library')
group = parser.add_mutually_exclusive_group()
group.add_argument('-p', '--passchecker', action='store_true',
                   help='Short Simple Password Checker')
group.add_argument('-s', '--story', action='store_true',
                   help='Short Simple MadLibs Story Teller')
group.add_argument('-m', '--math', action='store_true',
                   help='Basic Command Line Calculator')
parser.add_argument('-P', '--password', action='store', dest='password',
                    help='User supplied password (for noninteractive use)')

results = parser.parse_args()

if results.passchecker:
    passchecker(results.password)
elif results.story:
    storyteller()
elif results.math:
    maths()
