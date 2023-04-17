# Bandung Bondowoso, Roro Jonggrang, dan para jin pekerja bisa melakukan 
# login ke dalam sistem. Pesan kesalahan mencakup kasus username tidak terdaftar 
# dan password yang salah. Pengguna tidak bisa menggunakan command login, setelah berhasil melakukan login.

# fungsi len
def lenn(string):
    count = 0
    for i in string:
        count += 1
    return count

# convert csv jd array

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

# fungsi login
def login():

    def lenn(string):
        count = 0
        for i in string:
            count += 1
        return count
    
    file = open("usnm.csv", 'r')

    jumlahbaris = lenn(list(file))

    username = input("Username: ")
    password = input("Password: ")

    # cek username

    ada = False
    ps_ada = False

    for i in range (jumlahbaris):
            if username in array[i]:
                ada = True

    if ada == True:
        for i in range (jumlahbaris):
            if password in array[i]:
                ps_ada = True
    else:
        print("Username tidak terdaftar!")
        x = input()

    if (ada == True) and (ps_ada == True):
        print("Selamat datang, " + username + "!")
        print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
        x = input()
    elif (ada == True) and (ps_ada == False):
        print("Password salah!")
        x = input()

    if (ada == True) and (ps_ada == True) and (x == "login"):
        print("Login gagal!")
        print("Anda telah login dengan username " + username + ", silahkan lakukan “logout” sebelum melakukan login kembali.")
        x = input()
    elif (ada == True) and (ps_ada == False) and (x == "login"):
        login()
    elif (ada == False) and (x == "login"):
        login()

# algoritma utama
login()