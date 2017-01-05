#!/usr/bin/python
import math
import sys
import os
import shutil


workdirectory = "/home/harun/Desktop/testrepo/tmp/tmp"
###logfile1 = "/home/harun/Desktop/testrepo/tmp/tmp/logs"
logfile2 = "/home/harun/Desktop/testrepo/tmp/tmp/logs.big"
###fo = open(logfile1, "wb")

def prgfls1(file2delete):
 fil = file2delete
 fo_name1 = fil + ".log"
 foi = open(fo_name1, "wb")
 
 deletedfilenumber=0
 nonexistingfilenumber=0
 with open(fil) as f:
   for line in f: 
        if os.path.exists(line.rstrip('\n')):
         os.remove(line.rstrip('\n'))
#         if True:
###         print line.rstrip('\n') + " deleted!"
         foi.write(line.rstrip('\n') + " deleted!\n")
         deletedfilenumber += 1
#         elif False:
#          print line.rstrip('\n') + " can not be deleted due to permission issue!"
#          fo.write(line.rstrip('\n') + " can not be deleted due to permission issue!")
        else:
###         print line.rstrip('\n') + " doesn't exist!"
         foi.write(line.rstrip('\n') + " doesn't exist!\n")
         nonexistingfilenumber += 1
         
### print "\n\n\nDeleted File Number: " + str(deletedfilenumber) + "\nWrong File Name numbers: " + str(nonexistingfilenumber) + "\n"
 foi.write("\n\n\nDeleted File Number: " + str(deletedfilenumber) + "\nWrong File Name numbers: " + str(nonexistingfilenumber) + "\n") 

# logfile1_ = fil+".log"
# shutil.copy(logfile1, logfile1_)



#file2delete = sys.argv[1]
#prgfls1(file2delete)

##/home/harun/Desktop/testrepo/tmp
filelist1 = []
for root, dirs, files in os.walk(workdirectory):
    for file in files:
        if file.endswith(".txt"):
###             print(os.path.join(root, file))
             filelist1.append(os.path.join(root, file))

###print filelist1
for i in filelist1:
### print i
 prgfls1(i)

###fo.close() 

