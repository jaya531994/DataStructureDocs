import math
def binarysearch(arr1, val):
    start = 0
    end = len(arr1) -1
    middle = math.floor((start+end)/2)
    print(start,middle,end)
    while arr1[middle] != val:
        if val < arr1[middle]:
            end = middle -1 
        else:
            start = middle + 1
        middle = math.floor((start+end)/2)
        print(start,middle,end)
    return middle
 
            



binarysearch([1,2,3,4,5,6,7,8,9], 6)