#Given an encoded string, return its decoded string.
#The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
#You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].
#The test cases are generated so that the length of the output will never exceed 105.

#excersice number 394
class Solution:
    def decodeString(self, s: str) -> str:
        ans, num, stack = '','', []
        for t in s:
            if t.isalpha():
                ans += t
            elif t.isdigit():
                num += t
            elif t == '[':
                stack.append((ans, num)) # we save the initial text and the number of repetitions
                ans, num = '',''
            else: #if we arrive to the end of one structure with the "]" it means we need to repeat what is in ans num times
                a,k = stack.pop()
                ans = a + ans*int(k)
        return ans