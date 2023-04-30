# len
def lenn(string):
    count = 0
    for i in string:
        count += 1
    return count
# Append
def appendx(listlama, ygmauditambah):
    listbaru = [None] * (lenn(listlama) + 1)

    for i in range(lenn(listlama)):
        listbaru[i] = listlama[i]

    listbaru[lenn(listlama)] = ygmauditambah

    return listbaru

# algoritma utama
def laporanjin (role,inputedUser, inputedlooting, candiarry) :
    # JINN COUNTER USER
    if role == "bandung_bondowoso":
        jumlahbaris = lenn(inputedUser)
        
        count1 = 0
        for i in range (jumlahbaris):
            if inputedUser[i][2] == "jin_pengumpul":
                count1 += 1
            else:
                count1 += 0
        
        count2 = 0
        for i in range (jumlahbaris):
            if inputedUser[i][2] == "jin_pemabangun":
                count2 += 1
            else:
                count2 += 0
        
        jinTot = (count1) + (count2)
        
        ## LOOT COUNTER
        sandData = int(inputedlooting[0][2])
        rockData = int(inputedlooting[1][2])
        waterData = int(inputedlooting[2][2])
        # Jin array dan hasil buatan
        jinarry = ["" for i in range (1000)]
        candifromjin = [0 for i in range (1000)]
        buildedcandi = 0
        
        for i in range (1000):
            if inputedUser[i][2] == "jin_pembangun":
                jinarry[buildedcandi] = role[i][0]
                buildedcandi += 1
        
        for i in range (1000):
            for j in range (200):
                if candiarry[j] != ["","","","",""]:
                    if candiarry[j][i] == jinarry[i]:
                        candifromjin[i] += 1
        sortedjinarry = []
        identification = ["A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h"
                        ,"I","i","J","j","K","k","L","l","M","m","N","n","O","o","P","p"
                        ,"Q","q","R","r","S","s","T","t","U","u","V","v","W","w","X","x"
                        ,"Y","y","Z","z"]
        c = 0
        while 52 > c :
            for j in range (count2) :
                if jinarry[j][0] == identification[c] or jinarry[j][0] == identification[c + 1]:
                    appendx(sortedjinarry,jinarry[j])
            c += 2
        jinarry == sortedjinarry
        
        max = candifromjin[0]
        min = candifromjin[0]
        rajin = jinarry[0]
        malas = jinarry[0]
        
        # Searcher rajin malas
        for i in range (count2):
            if jinarry[i] != "":
                if candifromjin[i] > max:
                    max = candifromjin[i]
                    rajin = jinarry[i]
        
        for i in range (count2):
            if jinarry[i] != "":
                min = candifromjin[i]
                malas = jinarry[i]
        print(f"> Total jin: {jinTot}")
        print(f"> Total jin pengumpul: {count1}")
        print(f"Total jin pembangun: {count2}")
        print (f"Jin terajin: {rajin}")
        print (f"Jin termalas: {malas}")
        print(f"Jumlah pasir {sandData} unit")
        print(f"Jumlah batu {rockData} unit")
        print(f"Jumlah air {waterData} unit")
    else: 
        print("Laporan candi hanya bisa diakses oleh akun Bandung Bondowoso.")