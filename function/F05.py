
# FUNGSI BUATAN
# len
def lenn(str):
    count = 0
    for i in str:
        count += 1
    return count
# append
def appendx(listlama, ygmauditambah):
    listbaru = [None] * (lenn(listlama) + 1)

    for i in range(lenn(listlama)):
        listbaru[i] = listlama[i]

    listbaru[lenn(listlama)] = ygmauditambah

    return listbaru
# split
def splitx(str, mark):
    listbaru = []
    temp = 0

    for i in range(lenn(str)):
        if str[i] == mark:
            listbaru = appendx(listbaru,(str[temp:i]))
            temp = i + 1

    listbaru = appendx(listbaru,(str[temp:]))

    return listbaru


fileBukaan = open('user.csv','r')

# PARSER BUATAN (ARRAY)
# divider untuk memisah per word
finArry = []

for line in fileBukaan:

    tempStr = ""
    
    for i in line:

        if i == ";" or i == "\n":
            finArry = appendx (finArry,tempStr)
            tempStr = ""

        else:
            tempStr += i

# MAIN DEF
def ubahJin(role,nama,newArry):
    if role == "bandung_bondowoso":
            
        x = False
        
        # JIN SEARCHER
        for i in range(9,len(newArry),3):
            if nama == newArry[i]:
                x = True
        if x == True:
            for i in range (9,len(newArry),3):
                if nama == newArry[i]:
                    
                    # ROLE CHANGE
                    inputSalah = True
                    while inputSalah: 
                        
                        confirm = input("Apakah anda ingin mengubah role jin terserbut? (y/n): ")
                        if confirm == "y":
                            inputSalah = False
                            if newArry[i+2] == "Pembangun":
                                newArry[i+2] = "Pengumpul"
                            elif newArry[i+2] == "Pengumpul" :
                                newArry[i+2] = "Pembangun"

                        elif confirm == "n":
                            inputSalah = False
                    
    # APABILA USER MENGDECLINE
        else:
            print("Tidak ada jin dengan username tersebut.")
        # OUTPUT
        return newArry
    else:
        return newArry

# yg dipanggil di main 
def f05(arrayUser):
    nama = str(input("Masukkan username jin : "))
    finArry = ubahJin(nama,arrayUser)
    
    return finArry

      
            
        
          
            

