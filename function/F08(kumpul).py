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

def batch_kumpul():
    jin_data = csv_to_array("usnm.csv")
    jumlah_jin = lenn(jin_data)

    # Cek jumlah Jin Pengumpul
    count = 0
    for i in range (jumlah_jin):
        if jin_data[i][2] == "jin pengumpul":
            count += 1

    if count == 0:
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu")

    else:
        bahan_bangunan = csv_to_array("bahan_bangunan.csv")

        for i in range (count):
            bahan_bangunan[0][2] = int(bahan_bangunan[0][2]) - random.randint(1,5)
            bahan_bangunan[1][2] = int(bahan_bangunan[1][2]) - random.randint(1,5)
            bahan_bangunan[2][2] = int(bahan_bangunan[2][2]) - random.randint(1,5)

        print(f"Mengerahkan {count} jin untuk mengumpulkan bahan. Jin menemukan total {bahan_bangunan[0][2]} pasir, {bahan_bangunan[1][2]} batu, dan {bahan_bangunan[2][2]} air.")

