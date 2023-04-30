from Type import effective as eff
from commands import random_number, find_ID, sisip_mtx

# batch bangun
def batchbangun(role:str, user:eff, candi:eff, bahan:list[list]) -> tuple[eff, list[list]]:
    if role!="bandung_bondowoso":
        print("Kamu tidak memiliki akses ke fitur ini")
    else:
        jumlahbaris = user.NEff

        # cari jumlah bahan yang dibutuhkan untuk batch bangun
        countjinpembangun = 0
        for i in range (jumlahbaris):
            if ((user.mtx[i][2]) == ("jin_pembangun")):
                    countjinpembangun += 1

        if countjinpembangun == 0:
            print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
        else:
            sumpasir = 0
            sumbatu = 0
            sumair = 0

            stockpasir = int(bahan[0][2])
            stockbatu = int(bahan[1][2])
            stockair = int(bahan[2][2])

            # placeholder bahan yang dibutuhkan
            pasir = [0 for i in range (jumlahbaris)]
            batu = [0 for i in range (jumlahbaris)]
            air = [0 for i in range (jumlahbaris)]

            for i in range (jumlahbaris):
                if ((user.mtx[i][2]) == ("jin_pembangun")):
                    usernamejin = user.mtx[i][0]

                    pasir[i] = random_number(1,5)
                    batu[i] = random_number(1,5)
                    air[i] = random_number(1,5)

                    sumpasir += pasir[i]
                    sumbatu += batu[i]
                    sumair += air[i]

            print("Mengerahkan " + str(countjinpembangun) + 
                " jin untuk membangun candi dengan total bahan " + str(sumpasir) + " pasir, " 
                + str(sumbatu) + " batu, dan " + str(sumair) + " air.")

            selisihpasir = stockpasir-sumpasir
            selisihbatu = stockbatu-sumbatu
            selisihair = stockair-sumair

            if (selisihpasir < 0) and (selisihbatu < 0) and (selisihair < 0):
                print("Bangun gagal. Kurang " + str(sumpasir-stockpasir) + " pasir, " + str(sumbatu-stockbatu) + " batu, dan " 
                    + str(sumair-stockair) + " air.")
            elif (selisihpasir < 0) and (selisihbatu < 0):
                print("Bangun gagal. Kurang " + str(sumpasir-stockpasir) + " pasir dan " + str(sumbatu-stockbatu) + " batu.")
            elif (selisihpasir < 0) and (selisihair < 0):
                print("Bangun gagal. Kurang " + str(sumpasir-stockpasir) + " pasir dan " + str(sumair-stockair) + " air.")
            elif (selisihbatu < 0) and (selisihair < 0):
                print("Bangun gagal. Kurang " + str(sumbatu-stockbatu) + " batu dan " + str(sumair-stockair) + " air.")
            elif (selisihpasir < 0):
                print("Bangun gagal. Kurang " + str(sumpasir-stockpasir) + " pasir.")
            elif (selisihbatu < 0):
                print("Bangun gagal. Kurang " + str(sumbatu-stockbatu) + " batu.")
            elif (selisihair < 0):
                print("Bangun gagal. Kurang " + str(sumair-stockair) + " air.")
            else:
                print("Jin berhasil membangun total " + str(countjinpembangun) + " candi.")
                
                for i in range (jumlahbaris):
                    if ((user.mtx[i][2]) == ("jin_pembangun")):
                        usernamejin = user.mtx[i][0]
                        generate_ID = find_ID(candi,1)

                        # sisip
                        candi = sisip_mtx([str(generate_ID), usernamejin, str(pasir[i]), str(batu[i]), str(air[i])], candi, generate_ID-1, candi.NEff)
                
                bahan[0][2] = selisihpasir
                bahan[1][2] = selisihbatu
                bahan[2][2] = selisihair

    return (candi, bahan)
