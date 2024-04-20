from typing import List
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = [[] for _ in range(2)] #a 2 row matrix

        dict1 = {n: 0 for n in nums1} #each value of nums1 is a key in the dictionary
        for n in nums2:
            if n in dict1:
                dict1[n]+=1
        for key, value in dict1.items():
            if value == 0:
                answer[0].append(key)

        dict2 = {n: 0 for n in nums2} #each value of nums1 is a key in the dictionary
        for n in nums1:
            if n in dict2:
                dict2[n]+=1
        for key, value in dict2.items():
            if value == 0:
                answer[1].append(key)

        return answer
    
def main():
    nums1 = [1, 2, 3]
    nums2 = [2, 4, 6]

    sol = Solution()
    result = sol.findDifference(nums1, nums2)
    print("Resultado:", result)

if __name__ == "__main__":
    main()