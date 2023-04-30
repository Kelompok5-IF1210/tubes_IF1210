from Type import effective as eff

def hapusjin(role:str, jin:eff, candi:eff) -> tuple[eff,eff]:
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
