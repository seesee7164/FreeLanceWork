# This file was created by Eric Johnson

# Date of last edit: 12/10/20

# Basic directions to run program

from Merge_Special import *

# This block of code is intended to get all of the input from the user at the
# start of the program
# print("please enter the input file's directory and name")
# print("directory: ", end = '')
# directory1 = input()
# print("name: ", end = '')
# name1 = input()

# print("please enter the desired column name or number: ", end = '')
# column = input()

# print("please enter the output file's directory and name")
# print("directory: ", end = '')
# directory2 = input()
# print("name: ", end = '')
# name2 = input()

# This List object keeps track of all of the objects
List = []

# This function is in charge of breaking the cells into usable data
def Cycle(string):
    i = 0
    while string[i] != '-':
        i+=1
    return [string[:i],int(string[(i+1):])]

Cells = ["this is a test-5", "aa-4", "ab-4", "aa-4", "Aa-4", "aaa-4", "aa-5", "zebra-4", "Zebra-4", "bat-4", "car-10", "extra test-16", "even more tests-16", "almost final test-4", "final test-16", "extratest1-9"]
Cells2 = ["xa-5", "xb-4", "xb-5", "xa-4"]
# Adding everything to the list
i = 0
while i < len(Cells):
    List.append(Cycle(Cells[i]))
    i+=1

#sorting the list
List2 = mergesplit(List)

i = 0
while i < len(List2):
    print(List2[i][0], "\t", List2[i][1])
    i += 1