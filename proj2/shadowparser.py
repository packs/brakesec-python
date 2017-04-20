#!/usr/bin/python

# File    : shadowparser.py
# Author  : Scott Pack
# Created : April 2017
# Purpose : Parse the password file of a linux system for the username and hash
#           of each user. These two items should be placed into a dictionary
#           for later use.
#
#     Copyright (c) 2017 Scott Pack. All rights reserved.
#
import argparse
import sys


def parseShadow(shadow):
    hashes = {}
    for entry in shadow:
        passwd = entry.split(":")
        username = passwd[0]
        password = passwd[1]
        # If the username is root let's assume it's not a real user
        if(username == "root"):
            continue
        try:
            # Only save out hashes for passwords that are hashed
            saltedHash = password.split("$")
            hash = saltedHash[3]
        except:
            # Skip all locked accounts
            continue
        hashes[username] = hash
    return hashes


parser = argparse.ArgumentParser(description='Short Simple Shadow File Parser')
parser.add_argument('-f', '--file', action='store', dest='file', required=True,
                    help='User supplied shadow file')
results = parser.parse_args()

try:
    shadow = open(results.file, 'r')
    hashes = parseShadow(shadow)
    print hashes
except IOError:
    print 'Cannot Open: ', results.settingsfile
    exit(0)
except:
    print "Unexpected error:", sys.exc_info()[0]
    exit(0)
else:
    shadow.close()
