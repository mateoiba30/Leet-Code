from typing import List
from json import loads
from sys import stdin

def findDifference(nums1: List[int], nums2: List[int]) -> List[List[int]]:
    return [list(set(nums1) - set(nums2)), list(set(nums2) - set(nums1))] #this line has all the logic of the excersice, qhere set() eliminates dulpicateds values

#in some IDEs we will need to put this: (not in leetcode)
f = open("user.out","w") #we open a file to write the output
a = 0
for case in map(loads, stdin): #we aplicate the function 'loads' to each array/line of the input (stdin file)
    if a==0: #if a indicates we are reading the first array/line of the case
        b = case #here we store the first array/line of results
        a += 1 #we coninue to the next line
    else:
        print(str(findDifference(b, case)), file = f) # we call the rutine
        a = a - 1
exit(0)