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


#======================================
#search element from list using binary search
#======================================
def binary_search(arr,target):
    min = 0
    max = len(arr) - 1

    while min <= max:
        mid = (min + max) // 2
        print(mid)
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            min = mid +1
        else:
            max = mid -1
    return -1

l1 = [9, 10, 10, 20, 30, 40, 90, 100, 110, 120]
target = 40
result = binary_search(l1,target)
