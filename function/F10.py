# len
def lenn(string):
    count = 0
    for i in string:
        count += 1
    return count

# Algoritma utama
def laporancandi (role,inputedcandi) :
    if role == "bandung_bondowoso":
        # JINN COUNTER USER
        jumlahcandi = lenn(inputedcandi) - 1
        nWater = 0
        nRock = 0
        nSand = 0
        
        if jumlahcandi == 0:
            priceyId = "-"
            cheapId = "-"
        else:    
            jumlahbaris = jumlahcandi + 1
            for i in range (1,jumlahbaris):
                nSand = (nSand) + int(inputedcandi[i][2])
                nRock = (nRock) + int(inputedcandi[i][3])
                nWater = (nWater) + int(inputedcandi[i][4])
            
            priceyCandi = 32500
            cheapCandi = 162500
            for i in range (1,jumlahbaris):
                candiValue = 10000*int(inputedcandi[i][2]) + 15000*int(inputedcandi[i][3]) + 7500*int(inputedcandi[i][4])
                if candiValue > priceyCandi:
                    priceyCandi = candiValue
                if candiValue < cheapCandi:
                    cheapCandi = candiValue
            
            for i in range (1,jumlahbaris):
                candiValue = 10000*int(inputedcandi[i][2]) + 15000*int(inputedcandi[i][3]) + 7500*int(inputedcandi[i][4])
                if priceyCandi == candiValue:
                    priceyId = inputedcandi[i][0]
                    priceyId = inputedcandi[i][0] + " (Rp " + str(priceyCandi) + ")"
                if cheapCandi == candiValue:
                    cheapId = inputedcandi[i][0]
                    cheapId = inputedcandi[i][0] + " (Rp " + str(cheapCandi) + ")"
                    
        print(f"> Total candi: {jumlahcandi}")
        print(f"> Total pasir yang digunakan: {nSand}")
        print(f"> Total batu yang digunakan: {nRock}")
        print(f"> Total air yang digunakan: {nWater}")
        print(f"> ID candi termahal: {priceyId}")
        print(f"> ID candi termurah: {cheapId}")
    else:
        print("Laporan candi hanya bisa diakses oleh akun Bandung Bondowoso.")
    

