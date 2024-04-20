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
