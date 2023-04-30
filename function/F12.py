from Type import effective as eff

def ayamberkokok(role:str, candi:eff) -> None:
    if role!="roro_jonggrang":
        print("Kamu tidak punya akses ke fitur ini")
    else:
        Totcan = (candi.NEff)
        if Totcan != 100:
            print("Kukuruyuk.. Kukuruyuk..")
            print("Jumlah Candi: " + str(Totcan))
            print("Selamat, Roro Jonggrang memenangkan permainan!")
            print("*Bandung Bondowoso marah*")
            print("Roro Jonggrang dikutuk menjadi candi.")
            exit()
        else:
            print("Kukuruyuk.. Kukuruyuk..")
            print("Jumlah Candi: " + str(Totcan))
            print("Yah, Bandung Bondowoso memenangkan permainan!")
            exit()
