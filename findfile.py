#!/usr/bin/env python3
#
# Script to find a file
#
# Git managed at
#

import sys, os

# Beautification Class, because I like it.
#
class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

# Don't panic, but PANIC
#
def panic():
    print ( bcolors.WARNING + "You're doing it wrong. File to search for is needed!" + bcolors.ENDC)
    print ("usage: " + sys.argv[0] + " <file> <search path>")
    sys.exit(2)

# Finds the program
#
def findfile(FILE,PATH):
    FULLPATH = 'No file'
    for root, dirs, files in os.walk(PATH):
        if FILE in files:
            FULLPATH = os.path.join(root, FILE)
    return FULLPATH

# MAIN
#

if len(sys.argv) <= 1:
   panic()
else:
   FILE = sys.argv[1]
   try:
      PATH = sys.argv[2]
   except:
      PATH = '/'

   FULLPATH = findfile(FILE,PATH)

   if FULLPATH == 'No file':
      print(bcolors.FAIL + 'File (' + FILE + ') not found in path (' + PATH + ').' + bcolors.ENDC)
      sys.exit(1)

   print('PATH = ' + bcolors.OKGREEN + FULLPATH + bcolors.ENDC)
   RELATIVEPATH = os.path.relpath(FULLPATH,PATH)
   print('Relative PATH = ' + RELATIVEPATH)
