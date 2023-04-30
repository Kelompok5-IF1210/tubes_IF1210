from Type import effective as eff
from commands import random_number

def kumpul(role: eff, bahan: list[list[str]]) -> list[list[str]]:
    if role!="jin_pengumpul":
        print("Kamu tidak memiliki akses ke fitur ini!")
    else:
        lootSand = (random_number(0,5))
        lootRock = (random_number(0,5))
        lootWater = (random_number(0,5))

        print(f"Jin menemukan {lootSand} pasir, {lootRock} batu, {lootWater} air.")

        bahan[0][2] = str(int(bahan[0][2]) + lootSand)
        bahan[1][2] = str(int(bahan[1][2]) + lootRock)
        bahan[2][2] = str(int(bahan[2][2]) + lootWater)
