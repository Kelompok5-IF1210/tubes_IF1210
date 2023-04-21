# Fungsi logout
# Akses sama program utama
def logout(belumlogin):
    global adauser
    global ps_ada
    global role
    if (belumlogin == False):
        belumlogin = True
        adauser = False
        ps_ada = False
        role = []
        print("Berhasil logout")
    else:
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")