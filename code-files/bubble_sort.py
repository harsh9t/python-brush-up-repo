arr = [5, 8, 4, 2, 1]
for j in range(len(arr), 0, -1):
    for i in range(1, j):
        if arr[i-1] > arr[i]:
            x = arr[i]
            arr[i] = arr[i-1]
            arr[i - 1] = x
        print arr

#print arr