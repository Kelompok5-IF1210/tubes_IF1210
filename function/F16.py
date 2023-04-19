# Prosedur ini digunakan untuk keluar dari permainan. Sebelum keluar dari program, 
# pemain akan diberikan opsi untuk melakukan prosedur save atau tidak. 
# Input dapat berupa huruf besar ataupun kecil. Input harus dipastikan valid. 
# Jika input tidak valid, prosedur akan menanyakan ulang hingga input menjadi valid.

def save():
    print("*otw ke function save*")

x = input()

if x == "exit":
    validasi = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")

    while not ((validasi == "y") or (validasi == "Y") or (validasi == "n") or (validasi == "N")):
        validasi = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    

if (validasi == "y") or (validasi == "Y"):
    save()
else:
    exit