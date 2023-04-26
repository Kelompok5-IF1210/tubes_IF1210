import argparse
import os
from Type import effective

# PRIMITIF
# len matrix
def mtx_len(matrix:list, mark:list) -> int:
    iterate=-1
    while True:
        if matrix[iterate+1]==mark:
            break
        else:
            iterate+=1
    return iterate+1

# len of array in a determined matrix
def det_arr_len(var:str) -> int:
    if var=="users":
        return 3
    elif var=="candi":
        return 5
    elif var=="bahan_bangunan":
        return 3
    
# find index from an array
def find_idx(search:str, mtx:list[list], idx:int) -> int:
    # asumsi pasti ada
    # idx: bagian array dalam matrix
    for i in range (mtx_len(mtx,"MARK")):
        if mtx[i][idx]==search:
            return i

# recursive
# mencari ID yang kosong
def find_ID(candi:effective, current:int) -> int:
    for i in range (candi.NEff):
        if candi.mtx[i][0]==str(current):
            return find_ID(candi,current+1)
    return current

# recursive
# menghapus salah satu anggota lalu menggeser array
def del_mtx(mtx:list, idx:int, length:int) -> list:
    if idx<=length:
        mtx[idx]=mtx[idx+1]
        return del_mtx(mtx,idx+1,length)
    else:
        return mtx
    
# recursive
# menyisipkan candi sesuai ID agar tetap berurut
def sisip_mtx(sisip:list, mtx:list, idx:int, length:int) -> list:
    if length>=idx:
        mtx[length+1]=mtx[length]
        return sisip_mtx(sisip,mtx,idx,length-1)
    else: 
        mtx[length+1]=sisip
        return mtx

# read csv
def read_csv(path_csv:str) -> tuple[list,int]:
    file = open(path_csv,'r')
    # count line
    count=0

    for line in file:
        # header
        if count==0:
            count+=1

            # determine len arr needed to store the string
            count_delimiter=0
            for char in line:
                if char==";":
                    count_delimiter+=1
            # initialization of mtx
            mtx=[["" for i in range (count_delimiter+1)] for i in range (200)]
            mtx_idx=count-1

        # not header
        else:
            str_temp=""
            arr_temp=["" for i in range (count_delimiter+1)]
            # indexing for arr_temp
            arr_idx=0
            mtx_idx=count-1

            for char in range (len(line)):
                if line[char]==";" or line[char]=="\n":
                    arr_temp[arr_idx]=str_temp
                    arr_idx+=1
                    str_temp=""
                else:
                    str_temp+=line[char]

            mtx[mtx_idx]=arr_temp
            count+=1
        
    # csv hanya berisi header: mtx_idx=0
    # asumsi csv diakhiri newline
    if mtx[mtx_idx-1]==["" for i in range (count_delimiter+1)]:
        mtx_idx-=1
    
    mtx[mtx_idx+1]=["MARK" for i in range(count_delimiter+1)]
    
    return (mtx, mtx_idx+1)

def trans_bahan(bahan:effective) -> list[list]:
    # bahan.mtx: [nama,deskripsi,jumlah]
    # nama -> pasir -> batu -> air

    # inisialisasi return matriks
    bahan_bangunan=[["" for i in range (3)] for i in range (3)]

    # load dalam keadaan kosong
    if bahan.mtx[0]==["MARK","MARK","MARK"]:
        bahan_bangunan[0]=["pasir", "adalah pasir", "0"]
        bahan_bangunan[1]=["batu", "adalah batu", "0"]
        bahan_bangunan[2]=["air", "adalah air", "0"]
    else:
        bahan_bangunan[0]=bahan.mtx[0]
        bahan_bangunan[1]=bahan.mtx[1]
        bahan_bangunan[2]=bahan.mtx[2]
    return bahan_bangunan

'''___________________________________________________BREAKDOWN___________________________________________________'''

# F01
def login(users:effective, user_now:str, role_now: str) -> tuple[str,str,bool]:
    # login status
    if role_now=="": 
        belumlogin=True
    else: 
        belumlogin=False
    
    if (belumlogin):
        username = input("Username: ")
        password = input("Password: ")

        user_ada = False
        pw_ada = False

        # mtx_user: [username, password, role]
        mtx_user=users.mtx
        len_user=users.NEff

        # find username in matrix
        for i in range (len_user):
            if (mtx_user[i][0] == (username)):
                user_ada = True

        # confirm password
        if user_ada == True:
            for i in range (len_user):
                if (mtx_user[i][1] == (password)):
                    pw_ada = True
                    index = i
        else: # not(user_ada)
            print("Username tidak terdaftar!")

        # after searching and confirming
        if (user_ada == True) and (pw_ada == True):
            print("Selamat datang, " + username + "!")
            print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")

            belumlogin = False
            role_now = mtx_user[index][2]
            user_now = username

        elif (user_ada == True) and (pw_ada == False):
            print("Password salah!")
        
    elif (belumlogin == False):
        print("Login gagal!")
        print("Anda telah login dengan username " + user_now + ", silahkan lakukan “logout” sebelum melakukan login kembali.")  

    return (user_now, role_now, not(belumlogin))

# F02
def logout(username:str, role:str, isLoggedIn:bool) -> tuple[str,str,bool]:
    if (isLoggedIn==True):
        isLoggedIn = False
        username=""
        role=""
        print("Berhasil logout")
    else:
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
    
    return (username, role, isLoggedIn)

# F03
def summonjin(role:str, users:effective) -> effective:
    # Bandung Bondowoso memiliki wewenang memanggil jin dari dunia lain. 
    # Bandung Bondowoso bisa memilih jenis jin yang ingin dipanggil. 
    # Jin harus bisa login untuk melakukan tugasnya sehingga Bondowoso harus 
    # memilih username yang unik dan password untuk jin tersebut. 
    # Jumlah maksimal jin yang bisa di–summon adalah 100.

    # ALGORITMA
    if role!="bandung_bondowoso":
            print("Eits, kamu bukan Bandung Bondowoso!")

    else: # role=="bandung_bondowoso"
        if (users.NEff)-2==100:
            print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
        
        else:
            # role=="bandung_bondowoso" and jumlah_jin<100
            print("Jenis jin yang dapat dipanggil: ")
            print("(1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
            print("(2) Pembangun - Bertugas membangun candi")
            print("")

            jenisjin = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))

            # jenisjin validation loop
            while not(jenisjin == 1) or (jenisjin == 2):
                print("Tidak ada jenis jin bernomor " + "“" + str(jenisjin) + "”!")
                jenisjin = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))

            if (jenisjin == 1) or (jenisjin == 2):
                # assign role
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

                # mtx_user: [username, password, role]
                mtx_user=users.mtx
                len_user=users.NEff

                usernamejin = input("Masukkan username jin: ")
                adajin = False

                # usernamejin validation loop
                # check overlapping username
                for i in range (len_user):
                    if usernamejin in mtx_user[i][0]:
                                adajin = True

                while (adajin == True):
                    print("")
                    print("Username " + usernamejin + " sudah diambil!")
                    usernamejin = input("Masukkan username jin: ")

                    # re-check overlapping username
                    adajin = False
                    for i in range (len_user):
                        if usernamejin in mtx_user[i][0]:
                                    adajin = True

                if (adajin==False):
                    passwordjin = input("Masukkan password jin: ")

                    # len passwordjin validation loop
                    while (len(passwordjin) < 5) or (len(passwordjin) > 25):
                        print("")
                        print("Password panjangnya harus 5-25 karakter!")
                        passwordjin = input("Masukkan password jin: ")

                    if (5<=len(passwordjin)<=25):
                        print("")
                        print("Mengumpulkan sesajen...")
                        print("Menyerahkan sesajen...")
                        print("Membacakan mantra...")
                        print("")
                        print("Jin " + usernamejin + " berhasil dipanggil!")

            # users.mtx=[username,password,role]
            # asumsi tidak ada matrix yang kosong di tengah karena hapusjin() akan menggeser urutan setelah menghapus
            # menggeser MARK
            users.mtx[(users.NEff)+1]=users.mtx[(users.NEff)]
                
                # menyisipkan jin baru
            users.mtx[(users.NEff)]=[usernamejin, passwordjin, kategorijin]
                
            # memperbarui user efektif
            users.NEff+=1       

    return users

# F04
def hapusjin(role:str, jin:effective, candi:effective) -> tuple[effective,effective]:
    if role!="bandung_bondowoso":
        print("Eits, kamu bukan Bandung Bondowoso!")
    else:   
        hapus_jin = False
        Nama_jin = input("Masukkan username jin: ")

        # jin.mtx: [username,password,role]
        for i in range (jin.NEff):
                # ngecek nama jin yang mau hapus tuh ada di matriks atau engga
                if Nama_jin == jin.mtx[i][0] and (jin.mtx[i][2]=="jin_pembangun" or jin.mtx[i][2]=="jin_pengumpul"): 
                    hapus_jin = True
                    x = i
                    break

        if hapus_jin == True :
            for i in range (x, jin.NEff+1): # untuk ngapus jin dari matriks jin
                    jin.mtx[i] = jin.mtx[i+1] 
                    # menggeser jin ke kiri mulai dari matriks yang dihapus
                    # hingga satu indeks setelah MARK
            jin.NEff-=1 # update NEff user

            # candi.mtx: [id,pembuat,pasir,batu,air]
            count = 0
            for i in range (candi.NEff): # untuk ngecek ada berapa candi yang dibangun oleh jin yang mau dihapus
                if Nama_jin == candi.mtx[i][1]:
                    count +=1

            while count != 0 : # ngeloop sampe semua candi kehapus
                count -= 1
                for i in range (candi.NEff): 
                    if Nama_jin == candi.mtx[i][1]:
                        x = i
                        for j in range (x, candi.NEff+1): # ngegeser matriks candi
                            candi.mtx[j] = candi.mtx[j+1]
                        candi.NEff-=1 # update NEff candi

            print ("Jin telah berhasil dihapus dari alam gaib.")

        else: # hapus_jin==False
            print("Tidak ada jin dengan username tersebut.")

    return (jin, candi)

# F05
def ubahjin(role:str, user:effective) -> effective:
    if role!="bandung_bondowoso":
        print("Kamu tidak memiliki akses ke fitur ini!")
    else:
        nama = str(input("Masukkan username jin : "))  
    
        x = False
        # JIN SEARCHER
        for i in range (2, user.NEff):
            if nama == user.mtx[i][0]:
                x = True
    
        if x == True:
            for i in range (2,user.NEff):
                if nama == user.mtx[i][0]:
                    # ROLE CHANGE
                    inputSalah = True
                    while inputSalah: 
                        confirm = input("Apakah anda ingin mengubah role jin terserbut? (y/n): ")
                        
                        if confirm == "y":
                            inputSalah = False
                            if user.mtx[i][2] == "jin_pembangun":
                                user.mtx[i][2] = "jin_pengumpul"
                            elif user.mtx[i][2] == "jin_pengumpul" :
                                user.mtx[i][2] = "jin_pembangun"
                            print("Jin berhasil diubah")
                        
                        # APABILA USER MENGDECLINE
                        elif confirm == "n":
                            inputSalah = False
                            print("Jin tidak jadi diubah")

        else: # x==False
            print("Tidak ada jin dengan username tersebut.")

    # OUTPUT
    return user

# F06
def bangun(user:effective,candi:effective,bahan:list[list], username:str, role:str) -> tuple[effective,effective,list[list]]:
    import random
    # update bahan, update NEff candi, cari ID terkecil candi, geser MARK candi, masukkan candi

    Bangun_candi = False
    # cek role
    if role=="jin_pembangun":
        Bangun_candi = True

    if Bangun_candi == True :
        Butuh_pasir = random.randint(1,5)
        Butuh_batu = random.randint(1,5)
        Butuh_air = random.randint(1,5)
            
        # cek persediaan
        # bahan: [nama,deskripsi,jumlah]
        # nama -> pasir -> batu -> air
        if Butuh_pasir <= int(bahan[0][2]) and Butuh_batu <= int(bahan[1][2]) and Butuh_air <= int(bahan[2][2]):
            # update bahan
            bahan[0][2] = int(bahan[0][2]) - Butuh_pasir 
            bahan[1][2] = int(bahan[1][2]) - Butuh_batu
            bahan[2][2] = int(bahan[2][2]) - Butuh_air

            banyak_candi = candi.NEff
            if banyak_candi==100:
                sisa=0
            else:
                # update NEff candi
                candi.NEff+=1
                sisa=100-(banyak_candi+1)

                # cari ID terkecil
                ID_candi=find_ID(candi, 1)

                # candi.mtx: [id,pembuat,pasir,batu,air]
                # sisipkan candi
                candi.mtx=sisip_mtx([ID_candi, username, Butuh_pasir, Butuh_batu, Butuh_air],candi.mtx,ID_candi-1,candi.NEff)

            print ("Candi berhasil dibangun.")
            print (f"Sisa candi yang perlu di bangun : {sisa}.")

        else : 
            print("Bahan bangunan tidak mencukupi")
            print ("Candi tidak bisa dibangun.")

    else :
        print("Role anda tidak memiliki akses membangun candi.")
    
    return (user, candi, bahan)

# F11
def hancurkancandi(role:str, candi:effective) -> effective:
    if role!="roro_jonggrang":
        print("Kamu tidak memiliki akses fitur ini!")
    else:
        id = int(input("Masukkan ID Candi: "))

        Cekcandi = False
        Cekpanjang = candi.NEff

        for i in range (Cekpanjang):
            if candi.mtx[i][0] == str(id):
                Cekcandi = True
                break
        
        if Cekcandi == False:
            print("Tidak ada candi dengan ID tersebut")
        else:
            Se7 = input(f"Apakah anda yakin ingin menghancurkan candi ID: {id} (Y/N)? ")
            if Se7 == "Y":
                for i in range (candi.NEff): 
                    if candi.mtx[i][0] == id:
                        candi.mtx = del_mtx(candi.mtx,i,candi.NEff) # geser candi
                        candi.NEff-=1 # update NEff candi
                print("Candi telah berhasil dihancurkan.")

            else:
                print("Candi tidak jadi dihancurkan.")

    return candi

# F12
def ayamberkokok(role:str, candi:effective) -> None:
    if role!="roro_jonggrang":
        print("Kamu tidak punya akses ke fitur ini")
    else:
        Totcan = (candi.NEff)
        if Totcan != 100:
            print("Kukuruyuk.. Kukuruyuk..")
            print("Jumlah Candi: " + str(Totcan))
            print("Selamat, Roro Jonggrang memenangkan permainan!")
            print("*Bandung Bondowoso marah*")
            print("Roro Jonggrang dikutuk menjadi candi.")
            exit()
        else:
            print("Kukuruyuk.. Kukuruyuk..")
            print("Jumlah Candi: " + str(Totcan))
            print("Yah, Bandung Bondowoso memenangkan permainan!")
            exit()

# F13
def load() -> str:   
    parser=argparse.ArgumentParser()
    parser.add_argument("folder_name", nargs='?', help='specify your game data location') 
    # add_argument() -- add argument to the parser
    # nargs='?' -- minimal zero argument given (to enable zero argument case) 
    args=parser.parse_args()

    # get the parameter
    folder_name=args.folder_name
    if folder_name==None:
        print("\nTidak ada nama folder yang diberikan!\n")
        print("Usage: python main.py <nama_folder>")
        exit()

    elif os.path.isdir(folder_name):
        # asumsikan:
        # - seluruh file penyimpanan dalam suatu folder dijamin ada
        # - memiliki nama yang fixed
        # - memiliki format yang sesuai dengan struktur data eksternal.

        # thus
        # from current directory
        # player will specify "save/folder_name" to get saved dataset
        # or "default" to get new game dataset

        print("\nLoading...\n")
        print("Selamat datang di program \"Manajerial Candi\"")
        # print("Silakan masukkan username Anda")
        
        if os.path.isdir(folder_name): return folder_name
        else: return "save/"+folder_name
    
    else:
        print("\nFolder \""+folder_name+"\" tidak ditemukan.")
        exit()

# F15
def help(role:str) -> None:
    print("=========== HELP ===========")
    if role=='':
        print("1. login")
        print("   Untuk masuk menggunakan akun")
        print("2. exit")
        print("   Untuk keluar dari program dan kembali ke terminal")
        print("3. save")
        print("   Untuk menyimpan data permainan")
    elif role=="bandung_bondowoso":
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
        print("   Untuk mengambil laporan kinerja jin")          
        print("8. laporancandi") 
        print("   Untuk mengetahui progress pembangunan candi")
        print("9. exit")
        print("   Untuk keluar dari program dan kembali ke terminal")       
        print("10. save")
        print("   Untuk menyimpan data permainan")
    elif role=="roro_jonggrang":
        print("1. logout") 
        print("   Untuk keluar dari akun yang digunakan sekarang") 
        print("2. hancurkancandi") 
        print("   Untuk menghancurkan candi yang tersedia ")
        print("3. ayamberkokok") 
        print("   Untuk menyelesaikan permainan")
        print("4. exit")
        print("   Untuk keluar dari program dan kembali ke terminal")
        print("5. save")
        print("   Untuk menyimpan data permainan")
    elif role=="jin_pengumpul":
        print("1. logout") 
        print("   Untuk keluar dari akun yang digunakan sekarang") 
        print("2. kumpul") 
        print("   Untuk mengumpulkan resource candi")
        print("3. exit")
        print("   Untuk keluar dari program dan kembali ke terminal")
        print("4. save")
        print("   Untuk menyimpan data permainan") 
    elif role=="jin_pembangun":
        print("1. logout") 
        print("   Untuk keluar dari akun yang digunakan sekarang") 
        print("2. bangun") 
        print("   Untuk membangun candi")
        print("3. exit")
        print("   Untuk keluar dari program dan kembali ke terminal")
        print("4. save")
        print("   Untuk menyimpan data permainan")