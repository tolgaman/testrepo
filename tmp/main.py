#!/usr/bin/python
import math
import sys
import os



workdirectory = "/home/harun/Desktop/testrepo/tmp/tmp"
logfile1 = "/home/harun/Desktop/testrepo/tmp/tmp/logs"
fo = open(logfile1, "wb")

def prgfls1(file2delete):
 fil = file2delete
 with open(fil) as f:
   for line in f: 
        if os.path.exists(line.rstrip('\n')):
         os.remove(line.rstrip('\n'))
#         if True:
#          print line.rstrip('\n') + " deleted!"
         fo.write(line.rstrip('\n') + " deleted!\n")
#         elif False:
#          print line.rstrip('\n') + " can not be deleted due to permission issue!"
#          fo.write(line.rstrip('\n') + " can not be deleted due to permission issue!")
        else:
         print line.rstrip('\n') + " doesn't exist!"
         fo.write(line.rstrip('\n') + " doesn't exist!\n")






#file2delete = sys.argv[1]
#prgfls1(file2delete)

##/home/harun/Desktop/testrepo/tmp
filelist1 = []
for root, dirs, files in os.walk(workdirectory):
    for file in files:
        if file.endswith(".txt"):
             print(os.path.join(root, file))
             filelist1.append(os.path.join(root, file))

print filelist1
for i in filelist1:
 print i
 prgfls1(i)

fo.close() 
