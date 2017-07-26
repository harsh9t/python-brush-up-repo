__author__ = "Harsh Thakkar"
__license__ = "Creative Commons Attribution license (CC BY 4.0)"
__email__ = "hthakkar@uni-bonn.de"
__status__ = "Testing"
phonebook = {"harsh" : 9824578690, "anand" : 20267293727, "deshzen" : 956789098, "vicky" : 9476567987}
for names, numbers in phonebook.items():
    print "The contact for %s is %d" % (names, numbers)

del phonebook["harsh"]
print phonebook

phonebook["harsh"] = 9834567890
print "Updated phonebook is :", phonebook

phonebook.pop("vicky")
print phonebook
