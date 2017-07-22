__author__ = "Harsh Thakkar"
__license__ = "Creative Commons Attribution license (CC BY 4.0)"
__email__ = "hthakkar@uni-bonn.de"
__status__ = "Testing"

#play with the range() and xrange() function along with zip()
x2 = [1, 3, 5]
y2 = [2, 4, 6]
zipped = zip(x2, y2)
print zipped
x1, y1 = zip(*zipped)
print x1 #x1 is a tuple
print y1 #y1 is a tuple
print list(x1) #y1 is a list
print list(y1) #y1 is a list
x2 == list(x1) and y2 == list(y1) #validating

# Prints out the numbers 0,1,2,3,4 -- range()
for x in range(5):
    print(x)

# Prints out 3,4,5
for x3 in range(3, 6):
    print(x3)

# Prints out 3,5,7
for x4 in range(3, 8, 2):
    print(x4)

#trying xrange
for a in xrange(5):
    print a

#comapring types of range and xrange
#Nicely explained here -- http://www.geeksforgeeks.org/range-vs-xrange-python/, do refer!
print type(x)
print type(a)

