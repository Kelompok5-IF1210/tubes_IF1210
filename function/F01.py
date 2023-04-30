from Type import effective as eff

def login(users:eff, user_now:str, role_now: str) -> tuple[str,str,bool]:
    # login status
    if role_now=="": 
        belumlogin=True
    else: 
        belumlogin=False
    
    if (belumlogin):
        username = input("Username: ")
        password = input("Password: ")

        user_ada = False
        pw_ada = False

        # mtx_user: [username, password, role]
        mtx_user=users.mtx
        len_user=users.NEff

        # find username in matrix
        for i in range (len_user):
            if (mtx_user[i][0] == (username)):
                user_ada = True

        # confirm password
        if user_ada == True:
            for i in range (len_user):
                if (mtx_user[i][1] == (password)):
                    pw_ada = True
                    index = i
        else: # not(user_ada)
            print("Username tidak terdaftar!")

        # after searching and confirming
        if (user_ada == True) and (pw_ada == True):
            print("Selamat datang, " + username + "!")
            print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")

            belumlogin = False
            role_now = mtx_user[index][2]
            user_now = username

        elif (user_ada == True) and (pw_ada == False):
            print("Password salah!")
        
    elif (belumlogin == False):
        print("Login gagal!")
        print("Anda telah login dengan username " + user_now + ", silahkan lakukan “logout” sebelum melakukan login kembali.")  

    return (user_now, role_now, not(belumlogin))
