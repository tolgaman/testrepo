import random
import sys
import array
import os

print ("Test")

file1 = "C:\\Users\\tolga\\Documents\\testtesttest111.txt"
#file1 = "C:\\Users\\tolga\\Documents\\TEST1.txt"
file2 = "C:\\Users\\tolga\\Documents\\TEST2.txt"
file2_ = open(file2,'w')

for line in open(file1):
    #print (line)
    Array = line.replace('\n','').split(',')
#    if Array[1] == "\"1001\"":
#      Classi = "\"Yes\""
#    elif Array[1] == "\"1002\"":
#      Classi = "\"OneThousdan2\""
#   elif Array[1].replace('"','') in (1001,1002 
#    else: 
#   
#     Classi = "\"No\""
    Array1strp =  Array[1].replace('"','')
    print(Array[1].replace('"',''))
    if Array1strp in ("1001","1025","6001"):
      Classi = "\"Single-Family\""
    elif Array1strp in ("1002","1003","1004","1005","1006","1007","4301","4316","4317"):  
      Classi = "\"Multi-Family\""
    elif Array1strp in ("4209","4211","4212","4221","4222","4299"):
      Classi = "\"Apartments\""
    elif Array1strp in ("4213","4201","1008"):
      Classi = "\"Residential-Other\"" 
    else:
      Classi = "No Cat" 
       
    Line1_ = Array[0] + "," + Array[1] + "," + Classi + "\n"
    print("X : " + Line1_ )         
    file2_.write(Line1_)



