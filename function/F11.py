from Type import effective as eff
from commands import del_mtx

def hancurkancandi(role:str, candi:eff) -> eff:
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
                for i in range (candi.NEff-1): 
                    if int(candi.mtx[i][0]) == id:
                        candi.mtx = del_mtx(candi.mtx,i,candi.NEff) # geser candi
                        candi.NEff-=1 # update NEff candi
                print("Candi telah berhasil dihancurkan.")

            else:
                print("Candi tidak jadi dihancurkan.")

    return candi
