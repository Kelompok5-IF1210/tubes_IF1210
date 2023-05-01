from Type import effective as eff
from commands import save

# F16
def keluar(user:eff, candi:eff, bahan:list[list]):
    validasi = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")

    while not ((validasi == "y") or (validasi == "Y") or (validasi == "n") or (validasi == "N")):
        validasi = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        
    if (validasi == "y") or (validasi == "Y"):
        save(user,candi,bahan)
        exit()
    else:
        exit()
