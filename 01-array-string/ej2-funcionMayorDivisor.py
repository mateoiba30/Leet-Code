class Solution:
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
    string1 = "LEET"
    resultado = solution.mayorDivisor(string1, 3)
    print("Resultado:", resultado)
