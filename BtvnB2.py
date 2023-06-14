#Bài 1:

file = open(r'B2\name.txt')
name_list = file.readlines()
length = len(name_list)
print("List of names:")
for i in range(length):
    print("- ",name_list[i],end='')
    
file.close()


#Bài 2:

import os.path
from os import path
name_file = input('Input file name: ')
if(path.exists(name_file)):
    file = open(name_file,"r")
    a = file.read()
    lines = a.split("\n")
    print("File contents:")
    for line in lines:
        print(line)
    file.close()
else:
    print("File not found.")


#Bài 3:

print("== Input file contents below ==")
file = open('users-input.txt',"w")
run = True
while run:
    content = input()
    if(content == ""):
        run = False
    else:
        file.write(content + "\n")


#Bài 4:


import datetime
print("== Input file contents below ==")
file = open('input-logs.txt',"a")
run = True
now = datetime.datetime.now()
time2 = now.strftime("%Y-%m-%d %H:%M:%S")
file.write(f'== Input file contents at {time2} ==\n')
while run:
    content = input()
    if(content == ""):
        run = False
    else:
        file.write(content + "\n")
file.write("\n")
file.close()


#Bài 5:
print("Give the correct answer to get point")
file = open('question-bank.txt',"r")
point = 0
list = file.readlines()
total_point = len(list)
for line in list:
    rs = line.split(',')
    print(rs[0],end='')
    key = int(rs[1])
    ans = int(input())
    if key == ans:
        point+=1
    
print(f"== You get {point}/{total_point} points ==")
file.close()
