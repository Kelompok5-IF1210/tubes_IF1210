from Type import effective as eff
from commands import random_number, find_ID, sisip_mtx
from main import bahan_bangunan

# batch kumpul
def batchkumpul(role:str, user:eff, bahan:list[list]) -> eff:
    if role!="bandung_bondowoso":
        print("Kamu tidak memiliki akses")
    else:
        countjinpengumpul = 0

        for i in range (user.NEff):
            if ((user.mtx[i][2]) == ("jin_pengumpul")):
                    countjinpengumpul += 1

        if countjinpengumpul == 0:
            print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")

        else:
            pasir, batu, air = 0, 0, 0
            for i in range (countjinpengumpul):
                pasir += random_number(0,5)
                batu += random_number(0,5)
                air += random_number(0,5)

            print(f"Mengerahkan {countjinpengumpul} jin untuk mengumpulkan bahan. Jin menemukan total {pasir} pasir, {batu} batu, dan {air} air.")

            bahan[0][2] = str(int(bahan[0][2])+pasir)
            bahan[1][2] = str(int(bahan[1][2])+batu)
            bahan[2][2] = str(int(bahan[2][2])+air)

    return bahan
