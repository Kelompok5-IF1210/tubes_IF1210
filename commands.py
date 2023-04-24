import argparse
import os
from Type import effective

# PRIMITIF
# len matrix
def mtx_len(matrix, mark) -> int:
    iterate=-1
    while True:
        if matrix[iterate+1]==mark:
            break
        else:
            iterate+=1
    return iterate

# len of array in a determined matrix
def det_arr_len(var:str) -> int:
    if var=="users":
        return 3
    elif var=="candi":
        return 5
    elif var=="bahan_bangunan":
        return 3

# read csv
def read_csv(path_csv:str) -> tuple:
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
        
    # antisipasi csv hanya berisi header
    # antisipasi csv diakhiri newline
    if mtx_idx!=0 and mtx[mtx_idx-1]==["" for i in range (count_delimiter+1)]:
        mtx_idx-=1
    
    mtx[mtx_idx+1]=["MARK" for i in range(count_delimiter+1)]
    
    return (mtx, mtx_idx+1)

'''___________________________________________________BREAKDOWN___________________________________________________'''

# F01
def login(users:effective, user_now:str, role_now: str):
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