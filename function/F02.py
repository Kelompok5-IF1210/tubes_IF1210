def logout(username:str, role:str, isLoggedIn:bool) -> tuple[str,str,bool]:
    if (isLoggedIn==True):
        isLoggedIn = False
        username=""
        role=""
        print("Berhasil logout")
    else:
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout.")
    
    return (username, role, isLoggedIn)
