def linearsearch(arr1,val):
    for i in range(len(arr1)):
        if arr1[i] == val:
            print(i)
            return i
        
    return -1


arr1 = [2,4,6,8,9,14,10,0]
val = 10
linearsearch(arr1,val)