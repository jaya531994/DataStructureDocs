#find third_large value from list.
def Thired_large(val):
    fisrt,second,third = float('-inf'),float('-inf'),float('-inf')
    for num in val:
        if num > fisrt:
            third = second
            second = fisrt
            fisrt = num
        elif second > num & second != fisrt:
            third = second
            second = num
        else:
            third = num

    return third

L1 = [10,20,100,50,60,70,110]
thired_val = Thired_large(L1)
print(thired_val)


# ========================================
#reverse string in python palindrom
# ======================================

str = "jaya"
print(str[::-1])
str2 = ""
for i in str:
    print(i)
    str2 = i + str2
    
print(str2)


# ========================================
#reverse number in python palindrom
# ======================================
# approch-1
#if 0 is present in the last it will remove zero while converting in int
#=======================================

num = 1010
str = str(num)
print(type(str))
str2 = ""
for i in str:
    print(i)
    str2 = i + str2

print(int(str2))


# approch-2
#===========================================
num = 101 
reversed_num = 0
original = num

while num > 0:
    reminder = num % 10
    reversed_num = reversed_num * 10 + reminder
    num //= 10

print(reversed_num) 

if reversed_num == original:
    print("palindrome")
else:
    print("not palindrome")


#=======================================================
# "aabbccaadbc"
# output = "a4b3c3d1"
#=======================================================
# from collections import Counter

str1 = "aabbccaadbc"
count = Counter(str1)

output = "".join(f"{key}{val}" for key,val in count.items())
print(output)



#=============================================================
# convert list to str
#=============================================================
l2= [10,'a','b',20]
str2 = "".join(str(i) for i in l2)
print(str2)

l1 = ['a','b','c']
str1 = "".join(l1)
print(str1)


#========================================================
#convert str to list
#========================================================
str1 = "jaya dwivedi"
list1 = list(str1.split())
list2 = list(str1)
print(list1)


#========================================================
# find common letter from two string and list
#========================================================
str1 = "jaya"
str2 = "haya"
str3 = str(set(str1) & set(str2))
print(str3)

# #list common element
l1 = [10,20,30,40]
l2 =[10,50,20,70]
l3 = list(set(l1) & set(l2))
print(l3)


#====================================================
#quick sort
#===================================================
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr  # Base case: already sorted

#     pivot = arr[0]  # Pick the first element as pivot
#     left = [x for x in arr[1:] if x <= pivot]  # Elements <= pivot
#     right = [x for x in arr[1:] if x > pivot]  # Elements > pivot

#     return quick_sort(left) + [pivot] + quick_sort(right)


def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: already sorted
    
    pivot = arr[0]
    print(pivot)
    smaller_val =[]
    larger_val = []
    
    for item in arr[1:]:
        if item > pivot:
            larger_val.append(item)
        else:
            smaller_val.append(item)

    return quick_sort(smaller_val) + [pivot] + quick_sort(larger_val)


l1 = [10,40,30,90,100,20,10,9,120,110]
output = quick_sort(l1)
print(output)


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

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")


#===============================================================
# missing number from list
#===============================================================
#if order of value is consistent 
#*************************************
arr = [1,2,3,5,6]
n = len(arr) + 1
expected_sum = n*(n+1)//2
actual_sum = sum(arr)
print(actual_sum)

expected_val = expected_sum - actual_sum
print(expected_val)

#**************************************
#if order of value has gap
#l1 = [10,20,30,40,60,70]
#***************************************
l1 = [10,20,30,40,60,70]
start, end = min(l1), max(l1)

expected_sum = set(range(start,end+1,10))
print(expected_sum)

actual_sum = set(l1)
missing_num = list(expected_sum - actual_sum)
print(missing_num)

#***************************************
# approch 3 using for loop
#****************************************
step = l1[0] -l1[1]
for i in range(len(l1)-1):
    if l1[i+1] != l1[i] + step:
        print(l1[i] + step)


#=============================================
#decorator example
#++++++++++++++++++++++++++++++++++++++++++++=

def swap_if_needed(func):
    def inner_fun(a,b):
        if b > a:
            a,b = b,a
        return func(a,b)
    return inner_fun

@swap_if_needed
def divide(a,b):
    return a/b

print(divide(5,15))


# ========================================
#find duplicate elements from list
# ======================================
l1 = [10,20,10,20,10,50,30,40,60,70]
l2 = list(set([i for i in l1 if l1.count(i) > 1]))
print(l2)


#+++++++++++++++++++++++++++++++++++++++
# using for loop?
#++++++++++++++++++++++++++++++++++++++
l1 = [10,20,10,20,10,50,30,40,60,70]
l2 =[]
for i in l1:
    if l1.count(i) > 1:
        l2.append(i)
print(list(set(l2)))


