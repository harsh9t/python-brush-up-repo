__author__ = "Harsh Thakkar"
__license__ = "Creative Commons Attribution license (CC BY 4.0)"
__email__ = "hthakkar@uni-bonn.de"
__status__ = "Production"

print "Insertion sort implementation"
def insertionsort(arr):
    for j in range(1, len(arr)):
        x = arr[j]
        i = j-1
        while (i >= 0 and arr[i] > x ):
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = x
        print arr

def main():
    #print "Ji array daliye"
    #arr = list(input('ese daliye 1, 2, 3, 4, 5 ..'))
    arr = [1, 4, 9, 6, 3, 8, 2]
    insertionsort(arr)

if __name__ == "__main__":
    main()