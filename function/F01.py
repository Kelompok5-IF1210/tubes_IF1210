# Bandung Bondowoso, Roro Jonggrang, dan para jin pekerja bisa melakukan 
# login ke dalam sistem. Pesan kesalahan mencakup kasus username tidak terdaftar 
# dan password yang salah. Pengguna tidak bisa menggunakan command login, setelah berhasil melakukan login.

def login():
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

    user = csv_to_array("usnm.csv")
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

    return role

login()
