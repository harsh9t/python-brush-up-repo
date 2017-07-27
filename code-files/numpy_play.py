__author__ = "Harsh Thakkar"
__license__ = "Creative Commons Attribution license (CC BY 4.0)"
__email__ = "hthakkar@uni-bonn.de"
__status__ = "Testing"

import numpy as np
import random
# showcasing two styles of declaring two numpy arrays of random numbers between a specified range
# style-1
age = []
for x in xrange(1,101): #101 as xrange doesnt take the last value
    y = random.randrange(15, 72)
    age.append(y)
np_age = np.array(age)
print np_age

# style-2
weight = []
for z in xrange(1,101): #101 as xrange doesnt take the last value
    weight.append(random.randrange(40, 120))
np_weight = np.array(weight)
print np_weight

#demo of zip function of python creating a merged list
#print np_weight[np_weight > 85]
l1 = zip(np_age, np_weight)
print "This is l1"
print l1

#new list with all ppl having weight > 85
l2 = []
for n1, n2 in l1:
    if n2 > 85:
        l2.append((n1, n2))
print "This is l2"
print l2
# TODO - DO THE SAME USING DICTIONARY

# TODO: Try getting this in one line
# weight = [z for z in xrange(1,101) for z in random.randrange(40,120)]


# weight = [y for y in xrange()]
