#Given an encoded string, return its decoded string.
#The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
#You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].
#The test cases are generated so that the length of the output will never exceed 105.

#exercise number 394

#THIS VERSION ONLY WORKS FOR CASES WITH ONE RECURSIVE SET OF BRACKETS (LOOK THE FOLLOWING VERSIONS), LIKE "a2[ac]f", "3[a2[c]]", etc. Not for "2[abc]3[cd]ef", "3[a]2[bc]", etc"
class Solution:
    def decodeString(self, s: str) -> str:
        if s == "":
            return ""
        
        new_struct = ""
        string_num = ""
        text = ""
        text2 = ""
        limit = len(s) - 1
        i = 0

        while i <= limit:
            while i <= limit and s[i].isalpha():
                text += s[i]
                i += 1
            while i <= limit and s[i].isdigit():
                string_num += s[i]
                i += 1
            if i <= limit and s[i] == "[":
                i += 1
            while i <= limit and s[i] != "]":
                new_struct += s[i]
                i += 1
            while i <= limit and s[i] == "]":
                i += 1
            while i <= limit and s[i].isalpha():
                text2 += s[i]
                i += 1
        
        if string_num == "":
            return text
        else:
            return text + int(string_num) * self.decodeString(new_struct) + text2
    
solution = Solution()
result = solution.decodeString("2[abc]3[cd]ef")
print("Resultado:", result)