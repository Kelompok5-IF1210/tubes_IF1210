# F14
import os
from tubes_IF1210.Type import effective

def save(user:effective, candi:effective, bahan:list[list]):
    folder=input("Masukkan nama folder : ")
    # asumsi folder hanya berisi satu nama folder (not folder in folder)

    if not(os.path.isdir("save")):
        os.mkdir("save")

    if not(os.path.isdir("save/"+folder)):
        os.mkdir("save/"+folder)

    # write user to csv
    f=open("save/"+folder+"/user.csv", "w")
    # header
    f.write("username;password;role\n")
    # body
    for i in range (user.NEff):
        line=f"{user.mtx[i][0]};{user.mtx[i][1]};{user.mtx[i][2]}\n"
        f.write(line)
    f.close()

    # write candi to csv
    f=open("save/"+folder+"/candi.csv", "w")
    # header
    f.write("id;pembuat;pasir;batu;air\n")
    # body
    for i in range (candi.NEff):
        line=f"{candi.mtx[i][0]};{candi.mtx[i][1]};{candi.mtx[i][2]};{candi.mtx[i][3]};{candi.mtx[i][4]}\n"
        f.write(line)
    f.close()

    # write bahan to csv
    f=open("save/"+folder+"/bahan_bangunan.csv", "w")
    # header
    f.write("nama;deskripsi;jumlah\n")
    # load otomatis menambah 3 line bahan
    f.write("pasir;merekatkan batu;"+str(bahan[0][2])+"\n")
    f.write("batu;membentuk candi;"+str(bahan[1][2])+"\n")
    f.write("air;dicampur dengan pasir untuk menjadi perekat;"+str(bahan[2][2])+"\n")
    f.close()