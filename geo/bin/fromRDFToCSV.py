__author__ = 'Oscar'

import rdflib
import sys
import os
import pprint


FILE_IN = "../assets/educacio.rdf"

g = rdflib.Graph()

result = g.parse(FILE_IN)

print("graph has %s statements." % len(g))

for subj, pred, obj in g:
    print "%s %s %s" % (subj.encode("utf8"), pred.encode("utf8"), obj.encode("utf8"))
