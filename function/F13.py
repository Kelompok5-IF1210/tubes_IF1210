# F13    
def load():    
    import argparse # import argparse module
    import os
    
    parser=argparse.ArgumentParser() # create class
    parser.add_argument("folder_name", nargs='?', help='specify your game data location') # add argument to the parser
    # nargs='?' -- minimal zero argument given (to enable zero argument case) 
    args=parser.parse_args() # command line argument

    folder_name=args.folder_name # use parameter in the code
    if folder_name==None:
        print("\nTidak ada nama folder yang diberikan!\n")
        print("Usage: python main.py <nama_folder>")
        exit()
    elif os.path.isdir(folder_name) or os.path.isdir("save/"+folder_name):
        # asumsikan:
        # - seluruh file penyimpanan dalam suatu folder dijamin ada
        # - memiliki nama yang fixed
        # - memiliki format yang sesuai dengan struktur data eksternal.

        print("\nLoading...\n")
        # menjalankan prosedur load data

        print("Selamat datang di program \"Manajerial Candi\"")
        print("Silakan masukkan username Anda")
        
        if os.path.isdir(folder_name): path=folder_name
        else: path="save/"+folder_name
        return path
    else:
        print("\nFolder \""+folder_name+"\" tidak ditemukan.")
        exit() # boleh (untuk keluar dari program)
