__author__ = "Harsh Thakkar"
__license__ = "Creative Commons Attribution license (CC BY 4.0)"
__email__ = "hthakkar@uni-bonn.de"
__status__ = "Testing"
# In this exercise, you will need to print an alphabetically sorted list of all functions in the re module, which contain the word find.
import re

# Your code goes here
rel = dir(re)
filtered = [x for x in rel if "find" in x]
print(sorted(filtered))
