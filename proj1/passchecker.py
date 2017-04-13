#!/usr/bin/python

# File    : passchecker.py
# Author  : Scott Pack
# Created : April 2017
# Purpose : A simple script that checks if a string entered by the user matches
#           the password stored in a variable. Relevant prompts should be
#           displayed to the user.
#
#     Copyright (c) 2017 Scott Pack. All rights reserved.
#
import argparse
import getpass

parser = argparse.ArgumentParser(description='Short Sample Password Checker')
parser.add_argument('-p', '--pass', action='store', dest='password',
                    help='User supplied password (for noninteractive use)')
results = parser.parse_args()

secret = 'r)FeGEw4MLgL'

if results.password is None:
    password = getpass.getpass()
else:
    password = results.password

if password == secret:
    print 'Access Granted'
else:
    print 'Access Denied'
