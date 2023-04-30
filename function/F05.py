from Type import effective as eff

def ubahjin(role:str, user:eff) -> eff:
    if role!="bandung_bondowoso":
        print("Kamu tidak memiliki akses ke fitur ini!")
    else:
        nama = str(input("Masukkan username jin: "))  
    
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
                            print("Jin berhasil diubah.")
                        
                        # APABILA USER MENGDECLINE
                        elif confirm == "n":
                            inputSalah = False
                            print("Jin tidak jadi diubah.")

        else: # x==False
            print("Tidak ada jin dengan username tersebut.")

    # OUTPUT
    return user
