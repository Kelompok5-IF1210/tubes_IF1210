fileBukaan = open('bahan_bangunan.csv','r')
import random

def kumpul():
   
    lootSand = (random.randint(0,5))
    lootRock = (random.randint(0,5))
    lootWater = (random.randint(0,5))

    return lootSand,lootRock,lootWater
    
hasilkumpul = kumpul()
print(hasilkumpul)
# blm input ke array