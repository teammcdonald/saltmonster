#!/usr/bin/env python3
#
# Script to find a file(s)
#
# Git managed at https://github.com/teammcdonald/saltmonster.git
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

# Finds the file(s)
#
def findfiles(FILE,PATH):
   FILES = []
   FILESRELATIVE = []
   for root, dirs, files in os.walk(PATH):
      if FILE in files:
         FILES.append(os.path.join(root, FILE))
         FILESRELATIVE.append(os.path.join(os.path.relpath(root, PATH),FILE))
   return FILES, FILESRELATIVE

# MAIN
#

# Did we pass any arguments
#
if len(sys.argv) <= 1:
   panic()
else:
   FILE = sys.argv[1]
   try:
      PATH = sys.argv[2]
   except:
      PATH = '/'

   # Find all the files
   #
   FILESFULL, FILESRELATIVE = findfiles(FILE,PATH)

   if len(FILESFULL) > 0:
      for i in FILESFULL:
         print(i)
      for i in FILESRELATIVE:
         print(i)
   else:
      print(bcolors.FAIL + 'File (' + FILE + ') not found in path (' + PATH + ').' + bcolors.ENDC)