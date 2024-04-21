#exercise 151
#Given an input string s, reverse the order of the words.
#A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
#Return a string of the words in reverse order concatenated by a single space.
#Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
class Solution:
    def reverseWords(self, s: str) -> str:
        i=0
        limit=len(s)
        prev_char='a'
        result=''
        actual_word=''
        
        while i<limit:
            
            if s[i]!=' ':#recorriendo palabra
                actual_word+=s[i]
            elif len(actual_word)>0: #terminé palabra
                actual_word+=(" "+result)
                result=actual_word
                actual_word=''
            #si tengo un espacio, debo avanzar sin importar lo que había antes

            prev_char=s[i]
            i+=1
        
        if s[i-1]!=' ':
            actual_word+=(" "+result)
            result=actual_word

        return result[:-1]#lo ultimo siempre es un espacio
    
if __name__ == "__main__":
    sol = Solution()
    s = "  hello world  "
    reversed_words = sol.reverseWords(s)
    print("Original string:", s)
    print("Reversed words:", reversed_words)