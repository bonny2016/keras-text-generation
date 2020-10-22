#!/usr/bin/env python

# encoding: utf-8

import sys

import urllib

import codecs

import json

import dateutil.parser as parser

if len(sys.argv) != 3:  # the program name and the two arguments

    # stop the program and print an error message

    sys.exit("usage: tweet2csv.py <infile> <outfile>")

infile = sys.argv[1]

outfile = sys.argv[2]

writer = codecs.open(outfile, "w", "utf-8")
#writer = unicodecsv.writer(open(outfile, mode='w'), encoding='utf-8', delimiter=',', quotechar='"',
#                           quoting=unicodecsv.QUOTE_NONNUMERIC)

for line in codecs.open(infile, 'r', 'utf8'):
    tweet = json.loads(line)
    # convert the created_at string to friendly ISO date
    #row = []
    #row.append(tweet['full_text'])
    txt = tweet['full_text']
    try:
       writer.write(txt)
    except err:
       print(err)
writer.close()








