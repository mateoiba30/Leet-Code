#exercise 334
#Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

from typing import List

class Solution:

    
   def increasingTriplet(self, nums: List[int]) -> bool:
        #ejecución O(n) y espacio de O(1), usa siempre al último mínimo como min con índice i
        #minn = float('inf')
        #middle = float('inf')
        #for num in nums:
         #   if num < minn:
          #      minn = num
           #     middle = float('inf') #ante nuevo mínimo debo crear una nueva cola
            #elif num < middle:
             #   middle = num     
           # else:
            #    return True
        #return False

    # ejecucion O(n), not always works
    # dicc = {}
    # i=0
    # for num in nums:#keep the original indexs of each element
    #     dicc.update({i: num})
    #     i+=1
    # sorted_dicc = dict(sorted(dicc.items(), key=lambda item: item[1]))#reorder de dicc values
    # indexes = list(sorted_dicc.keys())

    # for i in range(len(indexes)-2): #search 3 consecutive indexes in ascending order
    #     if indexes[i] < indexes[i+1] and indexes[i+1] < indexes[i+2]:
    #         return True
                
    # return False
        
    #necesita mucha memoria, O(n^2) creo
      #  mins = []
       # mids = []
        #mins.append(float('inf'))
        #mids.append(float('inf'))
        #for num in nums:
        #    for i in range(len(mins)):
        #        if num <= mins[i]:
        #            mins.append(num)
        #            mids.append(float('inf'))
        #            
        #        elif num <= mids[i]:
        #            mins.append(mins[i])
        #            mids.append(num)
        #              
        #        else:
        #            return True
        #return False
        
        #ejecución O(n) y espacio de O(1), similar a la 1er version, pero esta anda siempre
        minn = float('inf')
        middle = float('inf')
        for num in nums:
            if num <= minn:#poner <= , sinó al tener 1,1,1 nos dirá que es ascendente
                minn = num
                #cuando actualizo el mínimo, el valor del medio no le debo asignar infinito, ya que si cambio el mínimo no quiero que me afecte, es como que el mínimo anterior haya sido un poco más bajo
            elif num <= middle:
                middle = num     
            else:
                return True
        return False

    
if __name__ == "__main__":
    solution = Solution()
    test = [100, 20, 12, 5, 13]
    print(solution.increasingTriplet(test)) #true expected