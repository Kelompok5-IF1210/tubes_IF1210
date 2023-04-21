# Akses Roro Jonggrang
def ayamBerkokok():
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

    # Count the number of rows
    count = 0
    for i in matriks:
        count += 1

    Totcan = count - 1
    Call = input("Kukuruyuk ")
    if Call == "Kukuruyuk":
        if Totcan != 100:
            print("Jumlah Candi : ", Totcan)
            print("Selamat, Roro Jonggrang memenangkan permainan")
            print("Bandung Bondowoso marah")
            print("Roro Jonggrang dikutuk menjadi candi")
            exit
        else:
            print("Jumlah Candi : ", Totcan)
            print("Yah, Bandung Bondowoso memenangkan permainan")
            exit

ayamBerkokok()