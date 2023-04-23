import random
import argparse # import argparse module
import os

# len
def lenn(string):
    count = 0
    for i in string:
        count += 1
    return count

# append
def appendx(listlama, ygmauditambah):
    listbaru = [None] * (lenn(listlama) + 1)
    
    for i in range(lenn(listlama)):
        listbaru[i] = listlama[i]
    
    listbaru[lenn(listlama)] = ygmauditambah
    
    return listbaru

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

### CSV
user = csv_to_array("user.csv")
candi = csv_to_array("candi.csv")
bahan = csv_to_array("bahan_bangunan.csv")

##### F01 :: LOGIN
def login():
    global user
    belumlogin = True

    command = input(">>> ")
    while (command != "login"):
        print("Anda belum login, silahkan melakukan login terlebih dahulu.")
        command = input(">>> ")
    
    while (belumlogin):
        username = input("Username: ")
        password = input("Password: ")

        def lenn(string):
            count = 0
            for i in string:
                count += 1
            return count

        jumlahbaris = lenn(user)

        adauser = False
        ps_ada = False
        role = []

        # cek username

        for i in range (jumlahbaris):
            for j in range (3):
                if (user[i][j] == (username)):
                    adauser = True

        if adauser == True:
            for i in range (jumlahbaris):
                for j in range (3):
                    if (user[i][j] == (password)):
                        ps_ada = True
                        index = i
        else:
            print("Username tidak terdaftar!")
            role = []
            login()

        if (adauser == True) and (ps_ada == True):
            print("Selamat datang, " + username + "!")
            print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
            belumlogin = False
            role = user[index][2]
            command = input(">>> ")
        elif (adauser == True) and (ps_ada == False):
            print("Password salah!")
            login()
        
        if (belumlogin == False) and (command == "login"):
            print("Login gagal!")
            print("Anda telah login dengan username " + username + ", silahkan lakukan “logout” sebelum melakukan login kembali.")
            command = input()
        else:
            login()

    return user, role

##### F02 :: LOGOUT
def logout (belumlogin):
    global adauser
    global ps_ada
    global role
    if (belumlogin == False):
        belumlogin = True
        adauser = False
        ps_ada = False
        role = []
        print("Berhasil logout")
    else:
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")

##### F03 :: SUMMON JIN

def summonjin ():
    global user

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
                if (user[i][j] == (usernamejin)):
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
    
    return user

##### F04 :: HILANGKAN JIN
def hapusjin():
    global user
    global candi
    hapus_jin = False
    Nama_jin = input("Masukkan username jin: ")
    for i in range (lenn(user)):
        for j in range (3):
            if Nama_jin == user[i][j]: # ngecek nama jin yang mau hapus tuh ada di matriks atau engga
                hapus_jin = True
                x = i
                break
    count = 0
    x = 0
    if hapus_jin == True :
        for y in range (x, lenn(user)-1): # untuk ngapus jin dari matriks jin
            for j in range (3):
                user[y][j] = user[y+1][j]
        for i in range (lenn(candi)): # untuk ngecek ada berapa candi yang dibangun oleh jin yang mau dihapus
            if Nama_jin == candi[i][1]:
                count +=1
        while count != 0 : # ngeloop sampe semua candi kehapus
            count -= 1
            for i in range (lenn(candi)): # ngegeser matriks
                if Nama_jin == candi[i][1]:
                    x = i
                    for y in range (x, lenn(candi)-1):
                        for j in range (4):
                            candi[y][j] = candi[y+1][j]

        print ("Jin telah berhasil dihapus dari alam gaib.")
    else:
        print("Tidak ada jin dengan username tersebut.")

    return user, candi

    ## masih harus di cek ulang

##### F05 :: UBAH TIPE JIN

##### F06 :: JIN PEMBANGUN
def bangun():
    global user
    global candi
    global bahan
    banyak_candi = lenn(candi) - 1
    idx_jin = lenn(user)

    Nama = user[idx_jin-1][0]
    Bangun_candi = False
    for i in range (1, lenn(user)):
        if Nama == user[i][0] and user[i][2] == "jin_pembangun":
            Bangun_candi = True
    if Bangun_candi == True :
        Butuh_pasir = random.randint(1,5)
        Butuh_batu = random.randint(1,5)
        Butuh_air = random.randint(1,5)
            
        if Butuh_pasir <= int(bahan[0][2]) and Butuh_batu <= int(bahan[1][2]) and Butuh_air <= int(bahan[2][2]):
            bahan[0][2] = int(bahan[0][2]) - Butuh_pasir 
            bahan[1][2] = int(bahan[1][2]) - Butuh_batu
            bahan[2][2] = int(bahan[2][2]) - Butuh_air
            x = banyak_candi
            for i in range (x, x+1):
                candi[i][0] = i
                candi[i][1] = Nama
                candi[i][2] = Butuh_pasir
                candi[i][3] = Butuh_batu
                candi[i][4] = Butuh_air
            sisa = 100 - lenn(candi)
            print ("Candi berhasil dibangun.")
            print (f"Sisa candi yang perlu di bangun : {sisa}.")
        else : 
            print ("Candi tidak bisa dibangun.")
    else :
        print("Role anda tidak memiliki akses membangun candi.")
    
    return user, candi, bahan

##### F07 :: JIN PENGUMPUL

##### F08 :: BATCH KUMPUL / BATCH BANGUN
def batchkumpul():
    global user
    global candi
    global bahan

    countjinpembangun = 0

    for i in range (lenn(user)):
        for j in range (3):
            if ((user[i][j]) == ("jin_pembangun")):
                countjinpembangun += 1

    if countjinpembangun == 0:
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")

    else:
        pasir = bahan[0][2]
        batu = bahan[1][2]
        air = bahan[2][2]

        for i in range (countjinpembangun):
            pasir += random.randint(1,5)
            batu += random.randint(1,5)
            air += random.randint(1,5)

        print(f"Mengerahkan {countjinpembangun} jin untuk mengumpulkan bahan. Jin menemukan total {pasir} pasir, {batu} batu, dan {air} air.")

        bahan[0][2] += pasir
        bahan[1][2] += batu
        bahan[2][2] += air

    return user, candi, bahan

def batchbangun():
    global user
    global candi
    global bahan

    jumlahbaris = lenn(user)

    # cari jumlah bahan yang dibutuhkan untuk batch bangun
    countjinpembangun = 0
    for i in range (jumlahbaris):
        for j in range (3):
            if ((user[i][j]) == ("jin_pembangun")):
                countjinpembangun += 1

    if countjinpembangun == 0:
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
    else:
        sumpasir = 0
        sumbatu = 0
        sumair = 0

        stockpasir = int(bahan[1][2])
        stockbatu = int(bahan[2][2])
        stockair = int(bahan[3][2])

        pasir = [0 for i in range (jumlahbaris)]
        batu = [0 for i in range (jumlahbaris)]
        air = [0 for i in range (jumlahbaris)]

        for i in range (jumlahbaris):
            for j in range (3):
                if user[i][j] == "jin_pembangun":
                    usernamejin = user[i][0]

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
            if lenn(candi) != 1:
                idx = lenn(candi)-1
            else:
                idx = 0

            print("Jin berhasil membangun total " + str(countjinpembangun) + " candi.")
            
            for i in range (jumlahbaris):
                for j in range (3):
                    if user[i][j] == "jin_pembangun":
                        usernamejin = user[i][0]
                        tambahan = [idx, usernamejin, pasir[i], batu[i], air[i]]
                        candi = appendx(candi, tambahan)
                    
                        idx += 1
            
            bahan[1][0], bahan[1][1], bahan[1][2] = "pasir", "merekatkan batu", selisihpasir
            bahan[2][0], bahan[2][1], bahan[2][2] = "batu", "membentuk candi", selisihbatu
            bahan[3][0], bahan[3][1], bahan[3][2] = "air", "dicampur dengan pasir untuk menjadi perekat", selisihair
    
    return user, candi, bahan

##### F09 :: AMBIL LAPORAN JIN

##### F10 :: AMBIL LAPORAN CANDI

##### F11 :: HANCURKAN CANDI
def hancurkanCandi():
    global user
    global candi
    global bahan

    id = int(input("Masukkan ID Candi: "))

    Cekcandi = False
    Cekpanjang = (len(candi))

    for i in range(Cekpanjang):
        if candi[i][0] == id:
            Cekcandi = True
            break
    
    if  Cekcandi == False:
        print("Tidak ada candi dengan ID tersebut")
    else:
        Se7 = input(f"Apakah anda yakin ingin menghancurkan candi ID: {id} (Y/N)? ")
        if Se7 == "Y":
            del candi[id]
            print("Candi telah berhasil dihancurkan.")

            return candi
        else:
            print("Candi tidak jadi dihancurkan.")

##### F12 :: AYAM BERKOKOK
# akses Roro Jonggrang
def ayamBerkokok():
    global user
    global candi
    global bahan
    
    Totcan = (lenn(candi)) - 1
    if Totcan != 100:
        print("Kukuruyuk.. Kukuruyuk..")
        print("Jumlah Candi: " + str(Totcan))
        print("Selamat, Roro Jonggrang memenangkan permainan!")
        print("*Bandung Bondowoso marah*")
        print("Roro Jonggrang dikutuk menjadi candi.")
        exit
    else:
        print("Kukuruyuk.. Kukuruyuk..")
        print("Jumlah Candi: " + str(Totcan))
        print("Yah, Bandung Bondowoso memenangkan permainan!")
        exit

##### F13 :: LOAD
def load():
    parser=argparse.ArgumentParser() # create class
    parser.add_argument("folder_name", nargs='?', help='specify your game data location') # add argument to the parser
    # nargs='?' -- minimal zero argument given (to enable zero argument case) 
    args=parser.parse_args() # command line argument

    folder_name=args.folder_name # use parameter in the code
    if folder_name==None:
        print("\nTidak ada nama folder yang diberikan!\n")
        print("Usage: python main.py <nama_folder>")
        exit()
    elif os.path.isdir(folder_name) or os.path.isdir("save/"+folder_name):
        # asumsikan:
        # - seluruh file penyimpanan dalam suatu folder dijamin ada
        # - memiliki nama yang fixed
        # - memiliki format yang sesuai dengan struktur data eksternal.

        print("\nLoading...\n")
        # menjalankan prosedur load data

        print("Selamat datang di program \"Manajerial Candi\"")
        print("Silakan masukkan username Anda")
        
        if os.path.isdir(folder_name): path=folder_name
        else: path="save/"+folder_name
        return path
    else:
        print("\nFolder \""+folder_name+"\" tidak ditemukan.")
        exit() # boleh (untuk keluar dari program)

##### F14 :: SAVE
def save():
    pass

##### F15 :: HELP
def help(role):
    print("=========== HELP ===========")
    if role == None:
        print("1. login")
        print("   Untuk masuk menggunakan akun")
        print("2. exit")
        print("   Untuk keluar dari program dan kembali ke terminal")
        print("3. save")
        print("   Untuk menyimpan data permainan")
    elif role == "bandung_bondowoso":
        print("1. logout") 
        print("   Untuk keluar dari akun yang digunakan sekarang") 
        print("2. summonjin") 
        print("   Untuk memanggil jin") 
        print("3. hapusjin") 
        print("   Untuk menghapus jin")
        print("4. ubahjin") 
        print("   Untuk mengubah tipe jin")
        print("5. batchkumpul") 
        print("   Untuk mengerahkan semua jin pengumpul mengumpulkan bahan")
        print("6. batchbangun") 
        print("   Untuk mengerahkan semua jin pembangun membangun candi")
        print("7. laporanjin") 
        print("   Untuk mengambil laporan knerja jin")          
        print("8. laporancandi") 
        print("   Untuk mengetahui progress pembangunan candi")       
        print("9. save")
        print("   Untuk menyimpan data permainan")
    elif role == "roro_jonggrang":
        print("1. logout") 
        print("   Untuk keluar dari akun yang digunakan sekarang") 
        print("2. hancurkancandi") 
        print("   Untuk menghancurkan candi yang tersedia")
        print("3. ayamberkokok") 
        print("   Untuk menyelesaikan permainan")
        print("4. save")
        print("   Untuk menyimpan data permainan")
    elif role == "jin_pengumpul":
        print("1. logout") 
        print("   Untuk keluar dari akun yang digunakan sekarang") 
        print("2. kumpul") 
        print("   Untuk mengumpulkan resource candi")
        print("3. save")
        print("   Untuk menyimpan data permainan") 
    elif role == "jin_pembangun":
        print("1. logout") 
        print("   Untuk keluar dari akun yang digunakan sekarang") 
        print("2. bangun") 
        print("   Untuk membangun candi")
        print("3. save")
        print("   Untuk menyimpan data permainan")

##### F16 :: EXIT
def keluar():
    validasi = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")

    while not ((validasi == "y") or (validasi == "Y") or (validasi == "n") or (validasi == "N")):
        validasi = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        
    if (validasi == "y") or (validasi == "Y"):
        save()
    else:
        exit

### ALGORITMA PROGRAM UTAMA
command = input(">>> ")
if command == "login":
    login()
if command == "logout":
    logout()