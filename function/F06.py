from Type import effective as eff
from commands import random_number, find_ID, sisip_mtx

def bangun(user:eff,candi:eff,bahan:list[list], username:str, role:str) -> tuple[eff,eff,list[list]]:
    # update bahan, update NEff candi, cari ID terkecil candi, geser MARK candi, masukkan candi

    Bangun_candi = False
    # cek role
    if role=="jin_pembangun":
        Bangun_candi = True

    if Bangun_candi == True :
        Butuh_pasir = random_number(1,5)
        Butuh_batu = random_number(1,5)
        Butuh_air = random_number(1,5)
            
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
                sisa=100-(banyak_candi+1)

                # cari ID terkecil
                ID_candi=find_ID(candi, 1)

                # candi.mtx: [id,pembuat,pasir,batu,air]
                # sisipkan candi
                candi=sisip_mtx([str(ID_candi), username, str(Butuh_pasir), str(Butuh_batu), str(Butuh_air)],candi,ID_candi-1,candi.NEff)

            print ("Candi berhasil dibangun.")
            print (f"Sisa candi yang perlu di bangun: {sisa}.")

        else : 
            print("Bahan bangunan tidak mencukupi.")
            print ("Candi tidak bisa dibangun.")

    else :
        print("Role anda tidak memiliki akses membangun candi.")
    
    return (user, candi, bahan)
