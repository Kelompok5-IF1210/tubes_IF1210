# len
def lenn(string):
    count = 0
    for i in string:
        count += 1
    return count

# algoritma utama
def laporanjin (role,inputedUser, inputedlooting) :
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
    else: 
        print("Laporan candi hanya bisa diakses oleh akun Bandung Bondowoso.")
