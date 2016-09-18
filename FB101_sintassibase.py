# -*- coding: utf-8 -*-
"""
Created on Sat Oct 03 21:00:31 2015

@author: 105028218
"""
print "*********EX1..IF *************"
var = 100
if ( var  == 100 ) : print "Value of expression is 100"


print "*********EX2 .. WHILE  *************"
count = 0
while (count < 9):
   print 'The count is:', count
   count = count + 1

print "*********EX3 .. WHILE ELSE *************"
count = 0
while count < 5:
   print count, " is  less than 5"
   count = count + 1
else:
   print count, " is not less than 5"

print "*********EX4 .. BREAK *************"

#!/usr/bin/python

for letter in 'Python':     # First Example
   if letter == 'o':
      break
   print 'Current Letter :', letter
  
var = 10                    # Second Example
while var > 0:              
   print 'Current variable value :', var
   var = var -1
   if var == 3:
      break

print "Good bye!"

print "********* THE END  *************"