from Type import effective as eff

def laporanjin (role: str, inputedUser: eff, inputedlooting: list[list[str]]) -> None :
    # JINN COUNTER USER
    if role == "bandung_bondowoso":
        print("")
        jumlahbaris = inputedUser.NEff
        
        # jumlah jin pengumpul
        count1 = 0
        for i in range (jumlahbaris):
            if inputedUser.mtx[i][2] == "jin_pengumpul":
                count1 += 1
            else:
                count1 += 0
        
        # jumlah jin pembangun
        count2 = 0
        for i in range (jumlahbaris):
            if inputedUser.mtx[i][2] == "jin_pembangun":
                count2 += 1
            else:
                count2 += 0
        
        for i in range (105):
            if inputedUser.mtx[i] == ["MARK", "MARK", "MARK"]:
                jinTot = i-2
                
                if jinTot != (count1) + (count2):
                    print("NINUNINUNINU")
        
        print(f"> Total Jin: {jinTot}")
        print(f"> Total Jin Pengumpul: {count1}")
        print(f"> Total Jin Pembangun: {count2}")

        print(f"> Jin Terajin: ")
        print(f"> Jin Termalas: ")

        ## LOOT COUNTER
        sandData = int(inputedlooting[0][2])
        rockData = int(inputedlooting[1][2])
        waterData = int(inputedlooting[2][2])
        print(f"> Jumlah Pasir: {sandData} unit")
        print(f"> Jumlah Batu: {rockData} unit")
        print(f"> Jumlah Air: {waterData} unit")        
    
    else: 
        print("Laporan candi hanya bisa diakses oleh akun Bandung Bondowoso.")
