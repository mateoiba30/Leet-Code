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