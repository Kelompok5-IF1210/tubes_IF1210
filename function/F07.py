fileBukaan = open('bahan_bangunan.csv','r')
import random

def kumpul(role,data):
    if role == "jin_pengumopul":
            
        lootSand = (random.randint(0,5))
        lootRock = (random.randint(0,5))
        lootWater = (random.randint(0,5))

        sandData = int(data[0][2])
        rockData = int(data[1][2])
        waterData = int(data[2][2])
        
        sandData = lootSand + sandData
        rockData = lootRock + rockData
        waterData = lootWater + waterData
        
        data[0][2] = str(sandData)
        data[1][2] = str(rockData)
        data[2][2] = str(waterData)
        
        print(f"Jin menemukan {lootSand} pasir, {lootRock} batu, {lootWater} air.")
        return data
    else:
        return data    
    hasilkumpul = kumpul()
    print(hasilkumpul)
    # blm input ke array