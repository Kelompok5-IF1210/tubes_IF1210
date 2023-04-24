from commands import read_csv, load, login, help
from Type import effective

# MAIN PROGRAM
# F13
path=load()

# if load() success
users=effective(read_csv(path+"/user.csv")[0], read_csv(path+"/user.csv")[1])
candi=effective(read_csv(path+"/candi.csv")[0], read_csv(path+"/candi.csv")[1])
bahan_bangunan=effective(read_csv(path+"/bahan_bangunan.csv")[0], read_csv(path+"/bahan_bangunan.csv")[1])

# status
(username, role, isLoggedIn)=('','',False)

while True:
    menu=input(">>> ")
    
    if menu=="login":
        # F01
        (username,role,isLoggedIn)=login(users, username, role)
    elif menu=="logout":
        # F02
        pass
    elif menu=="summonjin":
        # F03
        pass
    elif menu=="hapusjin":
        # F04
        pass
    elif menu=="ubahjin":
        # F05
        pass
    elif menu=="bangun":
        # F06
        pass
    elif menu=="kumpul":
        # F07
        pass
    elif menu=="batchkumpul":
        # F08
        pass
    elif menu=="batchbangun":
        # F08
        pass
    elif menu=="laporanjin":
        # F09
        pass
    elif menu=="laporancandi":
        # F10
        pass
    elif menu=="hancurkancandi":
        # F11
        pass
    elif menu=="ayamberkokok":
        # F12
        pass
    elif menu=="save":
        # F14
        pass
    elif menu=="help":
        # F15
        help(role)
    elif menu=="exit":
        # F16
        pass
    else:
        exit()
