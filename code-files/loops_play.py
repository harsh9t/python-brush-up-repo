__author__ = "Harsh Thakkar"
__license__ = "Creative Commons Attribution license (CC BY 4.0)"
__email__ = "hthakkar@uni-bonn.de"
__status__ = "Testing"

#play with the range() and xrange() function along with zip()
x = [1, 3, 5]
y = [2, 4, 6]
zipped = zip(x, y)
print zipped
x1, y1 = zip(*zipped)
print x1 #x1 is a tuple
print y1 #y1 is a tuple
print list(x1) #y1 is a list
print list(y1) #y1 is a list
x == list(x1) and y == list(y1) #validating
