#!/usr/bin/python
import math
import sys
import os
fil = sys.argv[1]
with open(fil) as f:
    for line in f:
        if os.path.exists(line.rstrip('\n')):
         os.remove(line.rstrip('\n'))
         if True:
          print line.rstrip('\n') + " deleted!"
         else:
          print line.rstrip('\n') + " can not be deleted due to permission issue!" 
        else:
         print line.rstrip('\n') + " doesn't exist!"

