#exercise 443
#Given an array of characters chars, compress it using the following algorithm:
#Begin with an empty string s. For each group of consecutive repeating characters in chars:
#If the group's length is 1, append the character to s.
#Otherwise, append the character followed by the group's length.
#The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.
#After you are done modifying the input array, return the new length of the array.
#You must write an algorithm that uses only constant extra space.

from typing import List

class Solution:

    def compress(self, chars: List[str]):
        prev_char = ''
        cont=1
        answer = 0

        for char in chars:     
            if prev_char == char:
                cont+=1
            else:
                answer += 1
                if cont != 1:
                    answer += len( str (cont))
                    cont = 1 
            prev_char = char

        answer += len( str (cont))
        
        return (answer)
    

if __name__ == "__main__":
    s = Solution()
    chars = ["a","a","b","b","c","c","c", "c","c","c","c","c", "c"]
    compressed_chars = s.compress(chars)
    print("Compressed characters:", str(compressed_chars))