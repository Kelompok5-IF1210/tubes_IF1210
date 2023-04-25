from commands import read_csv, trans_bahan, load, login, logout, summonjin, hapusjin, ubahjin, bangun, hancurkancandi, ayamberkokok, help
from Type import effective

# MAIN PROGRAM
# F13
path=load()

# if load() success
users=effective(read_csv(path+"/user.csv")[0], read_csv(path+"/user.csv")[1])
candi=effective(read_csv(path+"/candi.csv")[0], read_csv(path+"/candi.csv")[1])
bahan_bangunan=trans_bahan(effective(read_csv(path+"/bahan_bangunan.csv")[0], read_csv(path+"/bahan_bangunan.csv")[1]))

# status
(username, role, isLoggedIn)=('','',False)

while True:
    menu=input(">>> ")
    
    if menu=="login":
        # F01
        (username,role,isLoggedIn)=login(users, username, role)

    elif menu=="logout":
        # F02
        (username,role,isLoggedIn)=logout(username, role, isLoggedIn)

    elif menu=="summonjin":
        # F03
        if role!="bandung_bondowoso":
            print("Eits, kamu bukan Bandung Bondowoso!")

        else: # role=="bandung_bondowoso"
            if (users.NEff)-2==100:
                print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
            else:
                # users.mtx=[username,password,role]
                # asumsi tidak ada matrix yang kosong di tengah karena hapusjin() akan menggeser urutan setelah menghapus
                # menggeser MARK
                users.mtx[(users.NEff)+1]=users.mtx[(users.NEff)]
                
                # menyisipkan jin baru
                users.mtx[(users.NEff)]=summonjin(users)
                
                # memperbarui user efektif
                users.NEff+=1
                
    elif menu=="hapusjin":
        # F04
        if role!="bandung_bondowoso":
            print("Eits, kamu bukan Bandung Bondowoso!")
        else:
            (users,candi)=hapusjin(users,candi)

    elif menu=="ubahjin":
        # F05
        users=ubahjin(role,users)

    elif menu=="bangun":
        # F06
        (users,candi,bahan_bangunan)=bangun(users,candi,bahan_bangunan, username, role)

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
        candi=hancurkancandi(role, candi)

    elif menu=="ayamberkokok":
        # F12
        ayamberkokok(role, candi)

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
