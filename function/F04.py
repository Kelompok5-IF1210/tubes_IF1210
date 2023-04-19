def lenn(string):
    count = 0
    for i in string:
        count += 1
    return count

def hapusjin():
    global candi
    global jin
    hapus_jin = False
    Nama_jin = input("Masukkan username jin:" )
    for i in range (length(jin)):
        if Nama_jin == nama_jin[i]: #Ngecek nama jin yang mau hapus tuh ada di matriks atau engga
            hapus_jin = True
            x = i
            break
    count = 0
    if hapus_jin == True :
        for y in range (x, lenn(jin)-1): #Untuk ngapus jin dari matriks jin
            jin[y] = jin[y+1]
        for i in range (length(candi)): # Untuk ngecek ada berapa candi yang dibangun oleh jin yang mau dihapus
            if Nama_jin == candi[i][1]:
                count +=1
        while count != 0 : #Ngeloop sampe semua candi kehapus
            count -= 1
            for i in range (length(candi)): #Ngegeser matriks
                if Nama_jin == candi[i][1]:
                    x =i
                    for y in range (x, lenn(candi)-1):
                        candi[y]=candi [y+1]

                
        print ("Jin telah berhasil dihapus dari alam gaib")
    else:
        print("Tidak ada jin dengan username tersebut")