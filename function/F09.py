from Type import effective as eff
from commands import count_candi

def laporanjin (role: str, inputedUser: eff, inputedCandi: eff, inputedlooting: list[list[str]]) -> None :
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
        
        print(f"> Total Jin: {jinTot}")
        print(f"> Total Jin Pengumpul: {count1}")
        print(f"> Total Jin Pembangun: {count2}")

        if inputedUser.NEff==2 or inputedCandi.NEff==0:
            print("> Jin Terajin: -")
            print("> Jin Termalas: -")
        else:
            # array jumlah candi per jin
            num_built=[0 for i in range (inputedUser.NEff)]
            
            # dari indeks 2, menghindari Bandung dan Roro
            for i in range (2,inputedUser.NEff):
                num_built[i]=count_candi(inputedUser.mtx[i][0], inputedCandi, 0, 0)
            
            '''debug'''
            print(num_built)

            # see terajin termalas
            terajin=""
            termalas=""
            count_rajin=(-1)
            count_malas=120
            for i in range (2, inputedUser.NEff):
                '''debug'''
                print(inputedUser.mtx[i][0], inputedUser.mtx[i][2], num_built[i])

                # update malas jin pembangun -> (lebih malas or leksikal tinggi)
                if inputedUser.mtx[i][2]=="jin_pembangun" and (num_built[i]<count_malas or (num_built[i]==count_malas and inputedUser.mtx[i][0]>termalas)):
                    termalas=inputedUser.mtx[i][0]
                    count_malas=num_built[i]
                # update rajin (lebih rajin or leksikal rendah)
                if num_built[i]>count_rajin or (num_built[i]==count_rajin and inputedUser.mtx[i][0]<terajin):
                    terajin=inputedUser.mtx[i][0]
                    count_rajin=num_built[i]
            
            print(f"> Jin Terajin: {terajin}")
            print(f"> Jin Termalas: {termalas}")

        ## LOOT COUNTER
        sandData = int(inputedlooting[0][2])
        rockData = int(inputedlooting[1][2])
        waterData = int(inputedlooting[2][2])
        print(f"> Jumlah Pasir: {sandData} unit")
        print(f"> Jumlah Batu: {rockData} unit")
        print(f"> Jumlah Air: {waterData} unit")        
    
    else: 
        print("Laporan jin hanya bisa diakses oleh akun Bandung Bondowoso.")
