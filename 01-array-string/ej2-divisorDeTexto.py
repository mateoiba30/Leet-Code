#exercise 1071
#For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).
#Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
class Solution:

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        self.lim = min ( len(str1), len(str2) )
        print("lim: ", self.lim)
        self.rta= ""
        
        while(self.lim > 0):
            self.divisor1 = self.mayorDivisor(str1, self.lim)
            print("lim: ", self.lim)
            self.divisor2 = self.mayorDivisor(str2, self.lim)
            print("maxdiv1: ",self.divisor1,", maxdiv2; ",self.divisor2,", limite: ",self.lim)
            if(self.divisor1 == self.divisor2 ):
                self.rta = self.divisor1
                self.lim=0 # indicamos el fin
            else:
                self.lim-=1

        return self.rta

    def mayorDivisor(self, str1: str, limiteSup: int) -> str:
        self.str1=str1
        self.limiteSup=limiteSup
        self.terminar = False
        self.divisorMax = ""
        self.l1 = len(str1)

        while(self.terminar == False and self.limiteSup>0):
            self.divisorMax = self.str1[0:self.limiteSup]
            self.divisorAux=self.divisorMax
            #print("divisor max: ",self.divisorMax, "limite: ", self.limiteSup)
            
            while( len(self.divisorAux) <= self.l1 and self.terminar ==False):
                if( self.divisorAux == self.str1 ):
                    self.terminar = True
                    #print("encontramos el divisor max: ",self.divisorMax)
                else:
                    #print(self.divisorAux," y ",self.str1," no coinciden")
                    self.divisorAux = self.divisorAux + self.divisorMax #si no uso divisorAux, el string se ira duplicando
                    #print("nuevo intento con ",self.divisorAux)
            self.limiteSup-=1
        if(self.terminar == False):
            self.divisorMax=""
        #print("divisor Max:", divisorMax)
        return self.divisorMax


if __name__ == "__main__":
    solution = Solution()
    
    # Ejemplo de uso
    string1 = "ABABAB"
    string2 = "ABAB"
    resultado = solution.gcdOfStrings(string1, string2)
    print("Resultado:", resultado)
