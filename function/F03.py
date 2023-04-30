from Type import effective as eff

def summonjin(role:str, users:eff) -> eff:
    if role!="bandung_bondowoso":
            print("Eits, kamu bukan Bandung Bondowoso!")

    else: # role=="bandung_bondowoso"
        if (users.NEff)-2==100:
            print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
        
        else:
            # role=="bandung_bondowoso" and jumlah_jin<100
            print("Jenis jin yang dapat dipanggil: ")
            print("(1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
            print("(2) Pembangun - Bertugas membangun candi")
            print("")

            jenisjin = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))

            # jenisjin validation loop
            while not((jenisjin == 1) or (jenisjin == 2)):
                print("Tidak ada jenis jin bernomor " + "“" + str(jenisjin) + "”!")
                jenisjin = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))

            if (jenisjin == 1) or (jenisjin == 2):
                # assign role
                if jenisjin == 1:
                    kategorijin = "jin_pengumpul"
                    print("")
                    print("Memilih jin “Pengumpul”")
                    print("")
                elif jenisjin == 2:
                    kategorijin = "jin_pembangun"
                    print("")
                    print("Memilih jin “Pembangun”")
                    print("")

                # mtx_user: [username, password, role]
                mtx_user=users.mtx
                len_user=users.NEff

                usernamejin = input("Masukkan username jin: ")
                adajin = False

                # usernamejin validation loop
                # check overlapping username
                for i in range (len_user):
                    if usernamejin in mtx_user[i][0]:
                                adajin = True

                while (adajin == True):
                    print("")
                    print("Username " + usernamejin + " sudah diambil!")
                    usernamejin = input("Masukkan username jin: ")

                    # re-check overlapping username
                    adajin = False
                    for i in range (len_user):
                        if usernamejin in mtx_user[i][0]:
                                    adajin = True

                if (adajin==False):
                    passwordjin = input("Masukkan password jin: ")

                    # len passwordjin validation loop
                    while (len(passwordjin) < 5) or (len(passwordjin) > 25):
                        print("")
                        print("Password panjangnya harus 5-25 karakter!")
                        passwordjin = input("Masukkan password jin: ")

                    if (5<=len(passwordjin)<=25):
                        print("")
                        print("Mengumpulkan sesajen...")
                        print("Menyerahkan sesajen...")
                        print("Membacakan mantra...")
                        print("")
                        print("Jin " + usernamejin + " berhasil dipanggil!")

            # users.mtx=[username,password,role]
            # asumsi tidak ada matrix yang kosong di tengah karena hapusjin() akan menggeser urutan setelah menghapus
            # menggeser MARK
            users.mtx[(users.NEff)+1]=users.mtx[(users.NEff)]
                
                # menyisipkan jin baru
            users.mtx[(users.NEff)]=[usernamejin, passwordjin, kategorijin]
                
            # memperbarui user efektif
            users.NEff+=1       

    return users
