def hancurkanCandi():
    import csv

    # Open the CSV file
    with open("candi.csv", 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',', quotechar='"')
        # Create an empty list to store the data
        matriks = []

        # Iterate over each row in the CSV file
        for row in reader:
            # Append the row to the list
            matriks.append(row)

    # Print the data
    print(matriks)

    id = int(input("Masukan ID Candi : "))
    Cekcandi = False
    Cekpanjang = (len(matriks))

    for i in range(Cekpanjang):
        if matriks[i][0] == id:
            Cekcandi = True
            break
    
    if  Cekcandi == True:
        print("Tidak ada candi dengan ID tersebut")
    else:
        print("Apakah anda yakin ingin menghancurkan candi ID:", id, "(Y/N)?")
        Se7 = input()
        if  Se7 == "Y":
            del matriks[id]
            print(matriks)
            print("Candi telah berhasil dihancurkan")
            return matriks
        else:
            print("Candi tidak jadi dihancurkan")

hancurkanCandi()