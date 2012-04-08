#!/bin/python
# Author: AJ v Bahnken -- ajvb

# Simple PyMongo example.

from pymongo import Connection
import argparse
import datetime
import pprint
import sys

# Arguments for specifying port if needed.
parser = argparse.ArgumentParser(description='''Basic example of PyMongo,
                                 with a CLI because I wanted one''')
parser.add_argument('-p', '--port', action='store', default=27017, 
                    dest='port', help='''specify port if you are not using 
                    MongoDBs default (27017)''', type=int,)
args = parser.parse_args()

# Mongo DB running at it's defaults, locally:
connection = Connection('127.0.0.1', args.port)

# Check connection
if not connection:
    sys.stderr.write( """Script is not able to connect to MongoDB, 
                         specify port if needed. (-p <port>)""" )

# Access a database from the connection.
db = connection.testdb

# Access a collection from selected database
# (Not using so code doesn't get to layered, helps readability.)
# collection = db.testcollection

# Create some records/documents
team = [{"Name": "AJ",
         "Handle": "ajvb",
         "Skills": ['frontend', 'swagging', 'python', 'linux'],
         "Date added": datetime.datetime.now()},
        {"Name": "Steve",
         "Handle": "elimisteve",
         "Skills": ['backend', 'go', 'python', 'linux', 'moreicantthinkof'],
         "RelatedSkills": "Mathz", #Example of how Mongo is scheme-free
         "Date added": datetime.datetime.now()},
        {"Name": "Jim",
         "Handle": "smoochy",
         "Second Handle": "JimmyMc", #Example of how Mongo is scheme-free
         "Skills": ['backend', 'python', 'linux', 'frontend', 'moreprobably'],
         "Date added": datetime.datetime.now()},
        {"Name": "Jay",
         "Handle": "jaymottz",
         "Skills": ['backend', 'pimpin', 'python', 'linux', 'waterknowledge'],
         "Date added": datetime.datetime.now()}]

# Added records/documents to collection
db.testcollection.insert(team)

#
# Now the records/documents are saved. It is that easy. Next few lines are 
# examples in relation to accessing the records/documents.
# 

print "Counting the amount of documents \n"
print "There are "+ str(db.testcollection.count()) +" documents in this collection."
print "\n"

print "Finding a specific document \n"
pprint.pprint(db.testcollection.find_one({"Name": "AJ" }))

print "Finding all with a specific perameter \n"
for mem in db.testcollection.find({"Skills": 'python'}):
    pprint.pprint(mem)

print "Finding all \n"
for mem in db.testcollection.find():
    pprint.pprint(mem)

## There is a lot more, but this is about what you need to get started.
