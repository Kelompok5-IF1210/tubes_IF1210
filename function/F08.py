import random

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

# ALGORITMA UTAMA
file = open("usnm.csv", 'r')
jumlah_data = lenn(list(file))

# Cek jumlah Jin Pengumpul
count = 0
for i in range (jumlah_data):
    if "jin_pengumpul" in array[i]:
        count += 1

if count == 0:
    print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu")

else:
    bahan_bangunan = csv_to_array("bahan_bangunan.csv")
    pasir = bahan_bangunan [0][2]
    batu = bahan_bangunan [1][2]
    air = bahan_bangunan [2][2]

    for i in range (count):
            pasir += random.randint(1,5)
            batu += random.randint(1,5)
            air += random.randint(1,5)

    print(f"Mengerahkan {count} jin untuk mengumpulkan bahan. Jin menemukan total {pasir} pasir, {batu} batu, dan {air} air.")