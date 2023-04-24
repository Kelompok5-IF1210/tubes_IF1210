from commands import csv_to_array, load, help

# initiate array
users=[None for i in range (1000)]
candi=[None for i in range (1000)]
bahan_bangunan=[None for i in range (1000)]

# MAIN PROGRAM
# F13
path=load()

# if load() success
users=csv_to_array(path+"/user.csv")
candi=csv_to_array(path+"/candi.csv")
bahan_bangunan=csv_to_array(path+"/bahan_bangunan.csv")

# (24-04): (temporarily) assume array good to go

# status
(username,role,isLoggedIn)=('','',False)

while True:
    menu=input(">>> ")
    
    if menu=="login":
        # F01
        pass
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
