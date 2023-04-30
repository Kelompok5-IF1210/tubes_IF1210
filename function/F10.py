from Type import effective as eff

def laporancandi (role: str, inputedcandi: eff) -> None:
    if role == "bandung_bondowoso":
        # JINN COUNTER USER
        jumlahcandi = inputedcandi.NEff
        nWater = 0
        nRock = 0
        nSand = 0
        
        if jumlahcandi == 0:
            priceyId = "-"
            cheapId = "-"
        else:    
            for i in range (jumlahcandi):
                nSand = (nSand) + int(inputedcandi.mtx[i][2])
                nRock = (nRock) + int(inputedcandi.mtx[i][3])
                nWater = (nWater) + int(inputedcandi.mtx[i][4])
            
            priceyCandi = 32500
            cheapCandi = 162500
            # mencari max dan min
            for i in range (jumlahcandi):
                candiValue = 10000*int(inputedcandi.mtx[i][2]) + 15000*int(inputedcandi.mtx[i][3]) + 7500*int(inputedcandi.mtx[i][4])
                if candiValue > priceyCandi:
                    priceyCandi = candiValue
                if candiValue < cheapCandi:
                    cheapCandi = candiValue
            
            # mencari indeks dari candi max dan min
            # diambil indeks terakhir yang ditemui
            for i in range (jumlahcandi):
                candiValue = 10000*int(inputedcandi.mtx[i][2]) + 15000*int(inputedcandi.mtx[i][3]) + 7500*int(inputedcandi.mtx[i][4])
                if priceyCandi == candiValue:
                    priceyId = inputedcandi.mtx[i][0]
                    priceyId = inputedcandi.mtx[i][0] + " (Rp " + str(priceyCandi) + ")"
                if cheapCandi == candiValue:
                    cheapId = inputedcandi.mtx[i][0]
                    cheapId = inputedcandi.mtx[i][0] + " (Rp " + str(cheapCandi) + ")"
                    
        print(f"> Total candi: {jumlahcandi}")
        print(f"> Total pasir yang digunakan: {nSand}")
        print(f"> Total batu yang digunakan: {nRock}")
        print(f"> Total air yang digunakan: {nWater}")
        print(f"> ID candi termahal: {priceyId}")
        print(f"> ID candi termurah: {cheapId}")
    else:
        print("Laporan candi hanya bisa diakses oleh akun Bandung Bondowoso.")
