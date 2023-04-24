import argparse
import os

# primitive
# len string (sebenarnya ga di-ban)
def lenn(str):
    count = 0
    for i in str:
        count += 1
    return count

# len matrix
def length(matrix):
    # mark=[]
    iterate=-1
    while True:
        if matrix[iterate+1]==[]:
            break
        else:
            iterate+=1
    return iterate

# len array
def panjang(array):
    i=0
    while True:
        if array[i]!=None:
            i+=1
        else:
            return i
        
    

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

# read csv
def csv_to_array(file_csv:str) -> list:
    # array index 0 is header
    array_baru=[]
    with open(file_csv,'r') as file:
        # inisialisasi
        is_in_quote=False   # cek dalam tanda petik atau tidak
        cell_data=''        # simpan data untuk csv yang sedang diproses
        # untuk mengumpulkan karakter dari file sampai koma atau sampai ketemu jeda baris
        row_data=[]         # simpan data untuk baris yang sedang diproses
        # jika ada jeda baris, ditambahkan ke daftar array_csv
        for char in file.read():
            if char==';' and not(is_in_quote):
                if cell_data!='':
                    row_data+=[cell_data]
                cell_data=''
            elif char=='\n' and not(is_in_quote):
                if cell_data!='':
                    row_data+=[cell_data]
                array_baru+=[row_data]
                row_data=[]
                cell_data=''
            elif char=='"':
                is_in_quote=not(is_in_quote)
            else:
                cell_data+=char
        if cell_data!='':
            row_data+=[cell_data]
        if row_data!='':
            array_baru+=[row_data]
    file.close()
    return array_baru

'''___________________________________________________BREAKDOWN___________________________________________________'''

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
        
        if os.path.isdir(folder_name): path=folder_name
        else: path="save/"+folder_name
        return path
    
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
        print("   Untuk mengambil laporan knerja jin")          
        print("8. laporancandi") 
        print("   Untuk mengetahui progress pembangunan candi")       
        print("9. save")
        print("   Untuk menyimpan data permainan")
    elif role=="roro_jonggrang":
        print("1. logout") 
        print("   Untuk keluar dari akun yang digunakan sekarang") 
        print("2. hancurkancandi") 
        print("   Untuk menghancurkan candi yang tersedia ")
        print("3. ayamberkokok") 
        print("   Untuk menyelesaikan permainan")
        print("4. save")
        print("   Untuk menyimpan data permainan")
    elif role=="jin_pengumpul":
        print("1. logout") 
        print("   Untuk keluar dari akun yang digunakan sekarang") 
        print("2. kumpul") 
        print("   Untuk mengumpulkan resource candi")
        print("3. save")
        print("   Untuk menyimpan data permainan") 
    elif role=="jin_pembangun":
        print("1. logout") 
        print("   Untuk keluar dari akun yang digunakan sekarang") 
        print("2. bangun") 
        print("   Untuk membangun candi")
        print("3. save")
        print("   Untuk menyimpan data permainan")
