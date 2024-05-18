#exercise 1431
#There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.
#Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.
#Note that multiple kids can have the greatest number of candies.
def canPlaceFlowers(flowerbed, n):
    places=0
    antepenultimo=1
    anterior=0

    for actual in flowerbed:
        if antepenultimo == 0 and anterior == 0 and actual == 0:
            anterior = 1
            places+=1
        antepenultimo = anterior
        anterior = actual
    
    if anterior == 0 and antepenultimo == 0:
        places+=1
        
    return n<=places


print(canPlaceFlowers([0,0,1,0,1], 1))
