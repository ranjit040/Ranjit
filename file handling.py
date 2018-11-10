# a file named "geek", will be opened with the reading mode.
file = open('geek.txt', 'r')
# This will print every line one by one in the file
for x in file:
    print (x)

====================================


# Python code to illustrate read() mode
file = open("geek.txt", "r")
print (file.read()) 

======================================

 Creating a file using write() mode
#
# Let’s see how to create a file and how write mode works:
# To manipulate the file, write the following in your Python environment:

# Python code to create a file
file = open('geek1.txt','w')
file.write("This is the write command")
file.write("It allows us to write in a particular file")
file.close()

========================================

# Working of append() mode
#
# Let’s see how the append mode works:

# Python code to illustrate append() mode
file = open('geek3.txt','a')
file.write("This will add this line")
file.close()

=============================================

# Using write along with with() function
#
# We can also use write function along with with() function:
#
# # Python code to illustate with() alongwith write()
with open("geek4.txt", "w") as f:
    f.write("Hello World!!!")
===============================================

# split() using file handling
#
# We can also split lines using file handling in Python.
# This splits the variable when space is encountered. You can also split using any characters as we wish. Here is the code:

# Python code to illustrate split() function
with open("geek5.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)

=================================================

# f = open("abc.txt", "r")
# print(f.readline())


# f = open("abc.txt", "r")
# print(f.readline())
# print(f.readline())

f = open("abc.txt", "r")
for x in f:
  print(x)

======================================================

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

===================================================

import os,sys
fname=input("enter file name: ")
if os.path.isfile(fname):
    print("file Exists: ",fname)
    f=open(fname,"r")
else:
    print("file does not exist",fname)
    sys.exit(0)
print("the content of file is: ")
print(f.read())
