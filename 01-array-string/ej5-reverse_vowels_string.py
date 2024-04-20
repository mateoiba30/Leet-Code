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