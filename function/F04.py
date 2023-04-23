def csv_to_array(filecsv):
    arraybaru = []
    with open(filecsv, 'r') as file:
        dlmtandapetik = False   # (cek dia di dalam "" or no)
        cell_data = '' 
        row_data = [] 
        for char in file.read():
            if char == ';' and not dlmtandapetik:
                if cell_data != '':
                    row_data += [cell_data]
                cell_data =""
            elif char == '\n' and not dlmtandapetik:
                if cell_data != '':
                    row_data += [cell_data]
                arraybaru += [row_data]
                row_data = []
                cell_data =""
            elif char == '"':
                dlmtandapetik = not dlmtandapetik
            else:
                cell_data += char
        if cell_data != '':
            row_data += [cell_data]
        if row_data != []:
            arraybaru += [row_data]
    return arraybaru
def lenn(string):
    count = 0
    for i in string:
        count += 1
    return count

def hapusjin():
    jin = [[" " for spek in range(3)] for jumlah in range(150)]
    candi = [[" " for spek in range(5)]for jumlah in range (1000)]
    jin_data = csv_to_array("usnm.csv")
    candi_data= csv_to_array("candi.csv")
    banyak_candi = lenn(candi_data) - 1
    banyak_jin = lenn(jin_data)

    for i in range (banyak_jin):
        jin[i][0] = jin_data[i][0]
        jin[i][1] = jin_data[i][1]
        jin[i][2] = jin_data[i][2]

    for i in range(banyak_candi) :
        candi[i][0] = candi_data[i+1][0]
        candi[i][1] = candi_data[i+1][1]
        candi[i][2] = candi_data[i+1][2]
        candi[i][3] = candi_data[i+1][3]
        candi[i][4] = candi_data[i+1][4]

    jin_hilang = input("Masukkan username jin:" )
    hapus_jin = False

    for i in range (lenn(jin)):
        if jin_hilang == jin[i][0]: #Ngecek nama jin yang mau hapus tuh ada di matriks atau engga
            hapus_jin = True
            x = i
            break

    count = 0
    if hapus_jin == True :
        for y in range (x, lenn(jin)-1): #Untuk ngapus jin dari matriks jin
            jin[y] = jin[y+1]
        for i in range (lenn(candi)): # Untuk ngecek ada berapa candi yang dibangun oleh jin yang mau dihapus
            if jin_hilang  == candi[i][1]:
                count +=1
        while count != 0 : #Ngeloop sampe semua candi kehapus
            count -= 1
            for i in range (lenn(candi)): #Ngegeser matriks
                if jin_hilang  == candi[i][1]:
                    x =i
                    for y in range (x, lenn(candi)-1):
                        candi[y]=candi [y+1]

                    
        print ("Jin telah berhasil dihapus dari alam gaib")
    else:
        print("Tidak ada jin dengan username tersebut")

    print(jin[:lenn(jin_data)])
    print(candi[:lenn(candi_data)])