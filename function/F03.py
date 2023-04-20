# Bandung Bondowoso memiliki wewenang memanggil jin dari dunia lain. 
# Bandung Bondowoso bisa memilih jenis jin yang ingin dipanggil. 
# Jin harus bisa login untuk melakukan tugasnya sehingga Bondowoso harus 
# memilih username yang unik dan password untuk jin tersebut. 
# Jumlah maksimal jin yang bisa di–summon adalah 100.

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
            if char == ';' and not dlmtandapetik:
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

# len
def lenn(str):
    count = 0
    for i in str:
        count += 1
    return count

# append
def appendx(listlama, ygmauditambah):
    listbaru = [None] * (lenn(listlama) + 1)
    
    for i in range(lenn(listlama)):
        listbaru[i] = listlama[i]
    
    listbaru[lenn(listlama)] = ygmauditambah
    
    return listbaru

# split
def splitx(str, mark):
    listbaru = []
    temp = 0

    for i in range(lenn(str)):
        if str[i] == mark:
            listbaru = appendx(listbaru,(str[temp:i]))
            temp = i + 1  

    listbaru = appendx(listbaru,(str[temp:]))

    return listbaru

user = csv_to_array("usnm.csv")

# algoritma utama
print("Jenis jin yang dapat dipanggil: ")
print("(1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
print("(2) Pembangun - Bertugas membangun candi")
print("")

jenisjin = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))

if (jenisjin == 1) or (jenisjin == 2):
    if jenisjin == 1:
        kategorijin = "jin_pengumpul"
        print("")
        print("Memilih jin “Pengumpul”")
        print("")
    elif jenisjin == 2:
        kategorijin = "jin_pembangun"
        print("")
        print("Memilih jin “Pembangun”")
        print("")

    jumlahbaris = lenn(user)

    usernamejin = input("Masukkan username jin: ")
    adajin = False
    for i in range (jumlahbaris):
        for j in range (3):
            if usernamejin in user[i]:
                        adajin = True

    if adajin == True:
        print("")
        print("Username " + usernamejin + " sudah diambil!")
    else:
        passwordjin = input("Masukkan password jin: ")
        while (lenn(passwordjin) < 5) or (lenn(passwordjin) > 25):
            print("")
            print("Password panjangnya harus 5-25 karakter!")
            passwordjin = input("Masukkan password jin: ")
        else:
            userbaru = [usernamejin, passwordjin, kategorijin]
            user = appendx(user, userbaru)

            print("")
            print("Mengumpulkan sesajen...")
            print("Menyerahkan sesajen...")
            print("Membacakan mantra...")
            print("")
            print("Jin " + usernamejin + " berhasil dipanggil!")

else:
    print("Tidak ada jenis jin bernomor " + "“" + str(jenisjin) + "”!")
