from typing import List

class Solution:

    def compress(self, chars: List[str]):
        prev_char = ''
        cont=1
        answer = []

        for char in chars:     
            if prev_char == char:
                cont+=1
            else: #we have to save the last character info
                answer.append(prev_char)
                if cont > 1 and cont <10:
                    answer.append(str(cont))
                elif cont >= 10:
                    self.append_large_num(answer, cont)
                cont=1
            
            prev_char = char

        answer.append(prev_char)
        if cont > 1 and cont <10:
            answer.append(str(cont))
        elif cont >= 10:
            self.append_large_num(answer, cont)
        cont=1
            
        del answer[0]
        return (answer)

    def append_large_num(self, answer, cont):
        first = True#to not change the order of elements by inserting on the second last position
        while cont != 0:
            if first:
                answer.append(str(cont % 10))
            else:
                answer.insert(-2, str(cont % 10 ) ) #insert the last digit on the second last position to put them in order
            cont = cont // 10


if __name__ == "__main__":
    s = Solution()
    chars = ["a","a","b","b","c","c","c", "c", "c","c","c","c", "c", "c"]
    compressed_chars = s.compress(chars)
    print("Compressed characters:", compressed_chars)