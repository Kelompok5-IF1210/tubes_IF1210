# Sistem pembangunan candi akan random per jin. Setiap jin akan membangun candi dengan 
# bahan yang di random untuk setiap candi, artinya bukan dilakukan satu random bahan 
# kemudian dikalikan dengan jumlah semua jin, tetapi setiap candi di-loop kemudian 
# dilakukan random bahan, kemudian dijumlahkan.

import random

# bisa pake bahan random dari 1-5

# len
def lenn(string):
    count = 0
    for i in string:
        count += 1
    return count

# ubah csv ke array
def csv_to_array(filecsv):
    arraybaru = []
    with open(filecsv, 'r') as file:
        dlmtandapetik = False   # (cek dia di dalam "" or no)
        cell_data = '' # simpen data untuk csv yang lg di proses. 
        # untuk kumpulin karakter dari file sampe koma atau smpe ktmu jeda baris.
        row_data = [] # nyimpen data untuk baris yg lg di proses. 
        # kalo ad jeda baris, ditambahin ke daftar array_csv
        for char in file.read():
            if char == ',' and not dlmtandapetik:
                if cell_data != '':
                    row_data += [cell_data]
                cell_data = ''
            elif char == '\n' and not dlmtandapetik:
                if cell_data != '':
                    row_data += [cell_data]
                arraybaru += [row_data]
                row_data = []
                cell_data = ''
            elif char == '"':
                dlmtandapetik = not dlmtandapetik
            else:
                cell_data += char
        if cell_data != '':
            row_data += [cell_data]
        if row_data != []:
            arraybaru += [row_data]
    return arraybaru

array = csv_to_array("usnm.csv")

# algoritma utama
file = open("usnm.csv", 'r')
jumlahbaris = lenn(list(file))

# cari jumlah bahan yang dibutuhkan untuk batch bangun
countjinpembangun = 0
for i in range (jumlahbaris):
    if "jin_pembangun" in array[i]:
        countjinpembangun += 1

if countjinpembangun == 0:
    print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
else:
    sumpasir = 0
    sumbatu = 0
    sumair = 0

    arraybahan = csv_to_array("bahan_bangunan.csv")
    arraycandi = csv_to_array("candi.csv")

    stockpasir = int(arraybahan[1][2])
    stockbatu = int(arraybahan[2][2])
    stockair = int(arraybahan[3][2])

    pasir = [0 for i in range (jumlahbaris)]
    batu = [0 for i in range (jumlahbaris)]
    air = [0 for i in range (jumlahbaris)]

    for i in range (jumlahbaris):
        if "jin_pembangun" in array[i]:
            usernamejin = array[i][0]

            pasir[i] = random.randint(1,5)
            batu[i] = random.randint(1,5)
            air[i] = random.randint(1,5)

            sumpasir += pasir[i]
            sumbatu += batu[i]
            sumair += air[i]

    print("Mengerahkan " + str(countjinpembangun) + 
        " jin untuk membangun candi dengan total bahan " + str(sumpasir) + " pasir, " 
        + str(sumbatu) + " batu, dan " + str(sumair) + " air.")

    selisihpasir = stockpasir-sumpasir
    selisihbatu = stockbatu-sumbatu
    selisihair = stockair-sumair

    if (selisihpasir < 0) and (selisihbatu < 0) and (selisihair < 0):
        print("Bangun gagal. Kurang " + str(sumpasir-stockpasir) + " pasir, " + str(sumbatu-stockbatu) + " batu, dan " 
            + str(sumair-stockair) + " air.")
    elif (selisihpasir < 0) and (selisihbatu < 0):
        print("Bangun gagal. Kurang " + str(sumpasir-stockpasir) + " pasir dan " + str(sumbatu-stockbatu) + " batu.")
    elif (selisihpasir < 0) and (selisihair < 0):
        print("Bangun gagal. Kurang " + str(sumpasir-stockpasir) + " pasir dan " + str(sumair-stockair) + " air.")
    elif (selisihbatu < 0) and (selisihair < 0):
        print("Bangun gagal. Kurang " + str(sumbatu-stockbatu) + " batu dan " + str(sumair-stockair) + " air.")
    elif (selisihpasir < 0):
        print("Bangun gagal. Kurang " + str(sumpasir-stockpasir) + " pasir.")
    elif (selisihbatu < 0):
        print("Bangun gagal. Kurang " + str(sumbatu-stockbatu) + " batu.")
    elif (selisihair < 0):
        print("Bangun gagal. Kurang " + str(sumair-stockair) + " air.")
    else:
        filecandi = open("candi.csv", 'r')
        baris1 = filecandi.readline()
        baris2 = filecandi.readline()

        if baris2 != "":
            jumlahline = lenn(list(filecandi))
            idx = int(arraycandi[jumlahline][0])+2
        if baris2 == "":
            idx = 0

        print("Jin berhasil membangun total " + str(countjinpembangun) + " candi.")
        
        for i in range (jumlahbaris):
            if "jin_pembangun" in array[i]:
                usernamejin = array[i][0]
                with open("candi.csv", "a", newline="") as read:
                    read.writelines(f'\n{idx},{usernamejin},{pasir[i]},{batu[i]},{air[i]}')
            
                idx += 1
        
        with open("bahan_bangunan.csv", "w") as f:
            f.writelines("nama,deskripsi,jumlah")
            f.writelines(f'\npasir,deskripsi pasir,{selisihpasir}')
            f.writelines(f'\nbatu,deskripsi batu,{selisihbatu}')
            f.writelines(f'\nair,deskripsi air,{selisihair}')

# bikin kurangin bahan dari csv bahan