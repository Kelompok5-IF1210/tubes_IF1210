import random
def csv_to_array(filecsv):
    arraybaru = []
    with open(filecsv, 'r') as file:
        dlmtandapetik = False   # (cek dia di dalam "" or no)
        cell_data = '' 
        row_data = [] 
        for char in file.read():
            if char == ';' and not dlmtandapetik:
                if cell_data != '':
                    row_data += [cell_data]
                cell_data =""
            elif char == '\n' and not dlmtandapetik:
                if cell_data != '':
                    row_data += [cell_data]
                arraybaru += [row_data]
                row_data = []
                cell_data =""
            elif char == '"':
                dlmtandapetik = not dlmtandapetik
            else:
                cell_data += char
        if cell_data != '':
            row_data += [cell_data]
        if row_data != []:
            arraybaru += [row_data]
    return arraybaru

def lenn(string):
    count = 0
    for i in string:
        count += 1
    return count

def bangun():
    candi = csv_to_array("candi.csv")
    bahan_bangunan = csv_to_array("Bahan_bangunan.csv")
    jin_data = csv_to_array("usnm.csv")
    idx_jin = lenn(jin_data)

    Nama = jin_data[idx_jin-1][0]
    Bangun_candi = False
    for i in range (1, lenn(jin_data)):
        if Nama == jin_data[i][0] and jin_data[i][2] == "jin pembangun":
            Bangun_candi = True

    if Bangun_candi == True :
        Butuh_pasir = random.randint(1,5)
        Butuh_batu = random.randint(1,5)
        Butuh_air = random.randint(1,5)
            
        if Butuh_pasir <= int(bahan_bangunan[0][2]) and Butuh_batu <= int(bahan_bangunan[1][2]) and Butuh_air <= int(bahan_bangunan[2][2]):
            bahan_bangunan[0][2] = int(bahan_bangunan[0][2]) - Butuh_pasir 
            bahan_bangunan[1][2] = int(bahan_bangunan[1][2]) - Butuh_batu
            bahan_bangunan[2][2] = int(bahan_bangunan[2][2]) - Butuh_air
            x = lenn(candi)-1
            candi_baru =[[" " for spek in range(5)]for jumlah in range (1)]
            candi_baru[0][0] = x+1
            candi_baru[0][1] = Nama
            candi_baru[0][2] = Butuh_pasir
            candi_baru[0][3] = Butuh_batu
            candi_baru[0][4] = Butuh_air
            
            candi += candi_baru

            sisa = 100 - lenn(candi)+1
            print ("Candi berhasil dibangun")
            print (f"Sisa candi yang perlu di bangun : {sisa}")
        else : 
            print ("Candi tidak bisa dibangun")
    else :
        print("Role anda tidak memiliki akses membangun candi")
