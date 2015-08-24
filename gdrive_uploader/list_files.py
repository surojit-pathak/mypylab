#! /usr/bin/python

import os
import sys

def list_files(path):
    # print ("List for path - %s" %path)
    dirnames = []
    for (dirpath, dirnames, filenames) in os.walk(path):
         if filenames != None:
             for file in [f for f in filenames if not f.startswith('.')]:
                  print dirpath + '/' + file
         break

    if len(dirnames) != 0:
        for dir in [d for d in dirnames if not d.startswith('.')]:
            list_files(path + '/' + dir)
        

if len(sys.argv) > 1:
   list_files(sys.argv[1].rstrip('/'))
   
