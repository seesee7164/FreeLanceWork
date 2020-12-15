# This file was created by Eric Johnson

# Date of last edit: 12/10/20

# Basic directions to run program

from Merge_Special import *
import csv
import os

# This block of code is intended to get all of the input from the user at the
# start of the program
print("Do you want a file from a different directory: ", end = '')
ans = input()
if ans == "no":
    true = True
else:
    print("What directory is the file in: ", end = '')
    os.chdir(input())
print("What is the file's name: ", end = '')
name1 = input()

print("please enter the desired column number: ", end = '')
column = int(input())

print("What should the output file be called: ", end = '')
name2 = input()

# This function is in charge of counting the number of times each name appears
def Cycle(L):
    wordList = []
    countList = []
    retList = []
    for i in L:
        if i in wordList:
            continue
        else:
            wordList.append(i)
            countList.append(L.count(i))
    for i in range(len(wordList)):
        retList.append([wordList[i],countList[i]])
    return retList

# This section is responsible for getting the data from the csv file
Counter1 = []
ColumnName = ''
with open(name1) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            ColumnName = row[column]
            line_count += 1
        else:
            # print(row[22])
            if '-' in row[column]:
                Counter1 += row[column].split('-')
            # elif ' ' in row[column]:
            #     Counter1 += row[22].split(' ')
            else:
                Counter1.append(row[column])
            line_count += 1

# Adding everything to the list
List = Cycle(Counter1)

#sorting the list
List2 = mergesplit(List)

i = 0
with open(name2, mode='w') as output_file:
    output_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    output_writer.writerow([ColumnName, 'Frequency'])
    while i < len(List2):
        print(List2[i][0], "\t", List2[i][1])
        output_writer.writerow(List2[i])
        i += 1