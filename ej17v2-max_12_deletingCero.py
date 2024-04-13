class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        left = 0 #como el start
        zeros = 0 #ceros en el arreglo
        ans = 0 #como el end

        for right in range(n): #para todas las ventanas posibles
            if nums[right] == 0: #esto es para ir contando los ceros dentro de la ventana actual
                zeros += 1

            while zeros > 1: #tengo que avanzar el inicio de la ventana hasta solo tener 1 cero (imaginamos que eliminamos una vez este cero restante)
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            ans = max(ans, right - left + 1 - zeros)#vemos si es la mejor ventana

        return ans - 1 if ans == n else ans #si nunca eliminamos, lo debemos hacer una vez