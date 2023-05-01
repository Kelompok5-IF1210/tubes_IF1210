from commands import read_csv, trans_bahan, load, login, logout, summonjin, hapusjin, ubahjin, bangun, kumpul, batchkumpul, batchbangun, laporanjin, laporancandi, hancurkancandi, ayamberkokok, save, help, keluar
from Type import effective as eff

# MAIN PROGRAM
# F13
path=load()

# if load() success
users=eff(read_csv(path+"/user.csv")[0], read_csv(path+"/user.csv")[1])
candi=eff(read_csv(path+"/candi.csv")[0], read_csv(path+"/candi.csv")[1])
bahan_bangunan=trans_bahan(eff(read_csv(path+"/bahan_bangunan.csv")[0], read_csv(path+"/bahan_bangunan.csv")[1]))

# status
(username, role, isLoggedIn)=('','',False)

while True:
    menu=input(">>> ")
    
    if menu=="login":
        # F01
        (username, role, isLoggedIn)=login(users, username, role)

    elif menu=="logout":
        # F02
        (username, role, isLoggedIn)=logout(username, role, isLoggedIn)

    elif menu=="summonjin":
        # F03
        users=summonjin(role, users)
                
    elif menu=="hapusjin":
        # F04
        (users, candi)=hapusjin(role, users, candi)

    elif menu=="ubahjin":
        # F05
        users=ubahjin(role, users)

    elif menu=="bangun":
        # F06
        (users, candi, bahan_bangunan)=bangun(users, candi, bahan_bangunan, username, role)

    elif menu=="kumpul":
        # F07
        bahan_bangunan=kumpul(role,bahan_bangunan)

    elif menu=="batchkumpul":
        # F08
        bahan_bangunan=batchkumpul(role, users, bahan_bangunan)

    elif menu=="batchbangun":
        # F08
        (candi, bahan_bangunan)=batchbangun(role, users, candi, bahan_bangunan)

    elif menu=="laporanjin":
        # F09
        laporanjin(role, users, candi, bahan_bangunan)

    elif menu=="laporancandi":
        # F10
        laporancandi(role, candi)

    elif menu=="hancurkancandi":
        # F11
        candi=hancurkancandi(role, candi)

    elif menu=="ayamberkokok":
        # F12
        ayamberkokok(role, candi)

    elif menu=="save":
        # F14
        save(users, candi, bahan_bangunan)

    elif menu=="help":
        # F15
        help(role)

    elif menu=="exit":
        # F16
        keluar(users, candi, bahan_bangunan)
