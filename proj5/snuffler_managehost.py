#!/usr/bin/python

# File    : Snuffler.py
# Author  : Scott Pack
# Created : May 2017
# Purpose : Takes a list of IP address for network devices and
#           adds them to the suspicious hosts tracker for
#           extra snort monitoring.
#
#     Copyright (c) 2017 Scott Pack. All rights reserved.
#

# import sys
import argparse

parser = argparse.ArgumentParser(description='Manages the suspicious host \
    tracking database used by Snuffler for more thorough snort monitoring.')
group = parser.add_mutually_exclusive_group()
group.add_argument('-f', '--file', action='store', dest='file',
                   help='sqlite file to store/retrieve host information')
group.add_argument('-i', '--ip', action='store', type=list, dest='host',
                   help='The IP address to operate on')
group.add_argument('-t', '--time', action='store', dest='time', default='120',
                   help='Specify TTL in minutes for monitored hosts (default: 120)')
parser.add_argument('-b', '--bpffile', action='store', dest='bpffile',
                    help='File to save the BPF output filters to')
parser.add_argument('-v', '--verbose', action='store_true', dest='verbose',
                    help='Be chattier with process output')
parser.add_argument('-q', '--quiet', action='store_true', dest='quiet',
                    help='Only print essential messages')

options = parser.parse_args()
