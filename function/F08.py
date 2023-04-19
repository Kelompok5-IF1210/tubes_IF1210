def batch_kumpul():
    global bahan_bangunan

    pasir = bahan_bangunan [0][2]
    batu = bahan_bangunan [1][2]
    air = bahan_bangunan [2][2]
    for i in range(length(jin)):
        pasir += random.randint(1,5)
        batu += random.randint(1,5)
        air += random.randint(1,5)

    bahan_bangunan = [["Pasir", "Adalah pasir", pasir],
                    ["Batu", "Adalah batu", batu],
                    ["Air", "Adalah air", air]]
    return bahan_bangunan