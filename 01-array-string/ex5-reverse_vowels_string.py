#exercise 345
#Given a string s, reverse only all the vowels in the string and return it.
#The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s_vowels = []
        result=''
        for char in s:
            if char in vowels:
                s_vowels.append(char) #guardo vocales en orden
        for char in s:
            if char in vowels:
                char = s_vowels.pop(-1) #las saco en reversa
            result+=char

        return result