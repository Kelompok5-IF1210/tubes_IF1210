import argparse
import os
from Type import effective as eff

# recursive
# len matrix with mark
def mtx_len(matrix:list, mark:list, iterate:int) -> int:
    # {menghitung panjang anggota array efektif dalam sebuah array yang diakhiri mark rekursif dengan basis anggota matriks adalah mark, dan kondisi pengulangan selama anggota matriks tidak sama dengan mark}
    
    # KAMUS LOKAL

    # ALGORITMA
    # pada pemanggilan pertama fungsi, 
    # constant iterate: int = 0

    if matrix[iterate]==mark:
        return iterate
    else:
        return mtx_len(matrix,mark,iterate+1)

# read csv
def read_csv(path_csv:str) -> tuple[list,int]:
    # {membaca setiap line pada csv dan memasukkan data mulai dari data pertama (header tidak termasuk) ke array, lalu menyimpan NEff array}

    # KAMUS LOKAL
    # file = SEQFILE of 
        # (*) char of line: str
        # (1) mark
    # count, count_delimiter, mtx_idx: int
    # str_temp: str
    # mtx: array [0..count_delimiter-1] of array [0..104] of str

    # function mtx_len (matrix: array of array of , mark:str iterate: int) -> int
    # {menghitung panjang anggota array efektif dalam sebuah array yang diakhiri mark
    # rekursif dengan basis anggota matriks adalah mark, dan kondisi pengulangan selama anggota matriks tidak sama dengan mark}

    # ALGORITMA
    # asumsi: csv selalui diakhiri newline
    file = open(path_csv,'r')
    # count line
    count=0

    # looping every line in file
    for line in file:
        # header
        if count==0:
            count+=1

            # determine how many columns there are in a file
            count_delimiter=0
            for char in line:
                if char==";":
                    count_delimiter+=1
            # initialization of mtx
            mtx=[["" for i in range (count_delimiter+1)] for i in range (105)]
            mtx_idx=count-1

        # not header
        else:
            str_temp=""
            # array to store per line
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
   
    return (mtx, mtx_len(mtx,["MARK" for i in range (count_delimiter+1)], 0))

def trans_bahan(bahan:eff) -> list[list]:
    # bahan.mtx: [nama,deskripsi,jumlah]
    # nama -> pasir -> batu -> air

    # inisialisasi return matriks
    bahan_bangunan=[["" for i in range (3)] for i in range (3)]

    # load dalam keadaan kosong
    if bahan.mtx[0]==["MARK","MARK","MARK"]:
        bahan_bangunan[0]=["pasir", "merekatkan batu", "0"]
        bahan_bangunan[1]=["batu", "membentuk candi", "0"]
        bahan_bangunan[2]=["air", "dicampur dengan pasir untuk menjadi perekat", "0"]
    else:
        bahan_bangunan[0]=bahan.mtx[0]
        bahan_bangunan[1]=bahan.mtx[1]
        bahan_bangunan[2]=bahan.mtx[2]
    return bahan_bangunan

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