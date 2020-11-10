#program membuat mesin penjual minuman otomatis

#Untuk Harga saya rekayasa sendiri
#Mesin ini direkayasa dapat memberi kembalian

#pilih jenis minuman
def Menampilkan_daftar_jenis_minuman():
    print(41 * "-")
    print("2009106005_Dwi Ageng Rohmatullah_")
    print("program membuat mesin penjual minuman otomatis")
    print(10 * "-","Pilih Jenis Minuman",10 * "-")
    print(41 * "=")
    print("[1] Minuman Soda")
    print("[2] Minuman Kopi")
    print("[3] Minuman Teh")
    print("[0] Keluar")
    print(41 * "=")

    pilih = str(input("masukkan pilihan (0/1/2/3) : "))

    if (pilih == "1"):
        Minuman_Soda()
    elif (pilih == "2"):
        Minuman_Kopi()
    elif (pilih == "3"):
        Minuman_Teh()
    elif (pilih == "0"):
        Membeli_lagi()
    
#Minuman Soda
def Minuman_Soda():
    Soda = ["1. Coca Cola","2. Sprite","3. Strawberry Fanta","4. Grape Fanta","5. Tebs"]
    print("Pilih Minuman")
    print(Soda[0])
    print(Soda[1])
    print(Soda[2])
    print(Soda[3])
    print(Soda[4])
    print("0. Keluar")
    
    pilih = str(input("Masukkan Pilihan (0/1/2/3/4/5) : "))

    if (pilih == "1"):
        Coca_Cola()
    elif (pilih == "2"):
        Sprite()
    elif (pilih == "3"):
        Strawberry_Fanta()
    elif (pilih == "4"):
        Grape_Fanta()
    elif (pilih == "5"):
        Tebs()
    elif (pilih == "0"):
        Membeli_lagi()
    else:
        print("Minuman Tidak Tersedia")
        Kembali_ke_awal()

#Minuman Kopi
def Minuman_Kopi():
    Kopi = ["1. Nescafe Black","2. Good day","3. ABC EXO Milk Coffee","4. Delmonte Mocha Latte"]
    print("Pilih Minuman")
    print(Kopi[0])
    print(Kopi[1])
    print(Kopi[2])
    print(Kopi[3])
    print("0. Keluar")

    pilih = str(input("Masukkan Pilihan (0/1/2/3/4) : "))

    if (pilih == "1"):
        Nescafe_Black()
    elif (pilih == "2"):
        Good_Day()
    elif (pilih == "3"):
        ABC_EXO_Milk_Coffee()
    elif (pilih == "4"):
        Delmonte_Mocha_Latte()
    elif (pilih == "0"):
        Membeli_lagi()
    else :
        print("Minuman Tidak Tersedia")
        Kembali_ke_awal()

#Minuman Teh
def Minuman_Teh():
    Teh = ["1. Frestea","2. Teh Pucuk harum","3. Ichi Ocha","4. Teh Javana","5. NU Green Tea"]
    print("Pilih Minuman")
    print(Teh[0])
    print(Teh[1])
    print(Teh[2])
    print(Teh[3])
    print(Teh[4])
    print("0. Keluar")

    pilih = str(input("Masukkan Pilihan (0/1/2/3/4/5) : "))

    if (pilih == "1"):
        Frestea()
    elif (pilih == "2"):
        Teh_Pucuk_Harum()
    elif (pilih == "3"):
        Ichi_Ocha()
    elif (pilih == "4"):
        Teh_Javana()
    elif (pilih == "5"):
        NU_Green_Tea()
    elif (pilih == "0"):
        Membeli_lagi()
    else:
        print("Minuman Tidak Tersedia")
        Kembali_ke_awal()

#ingin membeli lagi
def Membeli_lagi():
    pilih = str(input("Ingin Membeli lagi (1)Ya (2)Tidak : "))
    if (pilih == "1"):
        Kembali_ke_awal()
    elif (pilih == "2"):
        print("Terimakasih Telah Menggunakan Mesin Penjual Ini")
        input("Tekan Enter untuk keluar")
        exit

# Kembali ke awal
def Kembali_ke_awal():
    input("Tekan Enter untuk kembali...")
    Menampilkan_daftar_jenis_minuman()

#Coca Cola
def Coca_Cola():
    HargaCC = 12000
    U = int(input("Masukkan Uang Anda : "))
    if (U >= HargaCC):
        print("Kembalian Anda = Rp.",U - HargaCC)
        print("pembelian berhasil")
        Membeli_lagi()
    else :
        print("Uang Anda Tidak Mencukupi")
        Kembali_ke_awal()

#Sprite
def Sprite():
    HargaS = 10000
    U = int(input("Masukkan Uang Anda : "))
    if (U >= HargaS):
        print("Kembalian Anda = Rp.",U - HargaS)
        print("Pembelian berhasil")
        Membeli_lagi()
    else :
        print("Uang Anda Tidak Mencukupi")
        Kembali_ke_awal()

#Strawberry Fanta
def Strawberry_Fanta():
    HargaSF = 8500
    U = int(input("Masukkan Uang Anda : "))
    if (U >= HargaSF):
        print("Kembalian Anda = Rp.",U - HargaSF)
        print("Pembelian berhasil")
        Membeli_lagi()
    else :
        print("Uang Anda Tidak Mencukupi")
        Kembali_ke_awal()

#Grape Fanta
def Grape_Fanta():
    HargaGF = 8500
    U = int(input("Masukkan Uang Anda : "))
    if (U >= HargaGF):
        print("Kembalian Anda = Rp.",U - HargaGF)
        print("Pembelian berhasil")
        Membeli_lagi()
    else :
        print("Uang Anda Tidak Mencukupi")
        Kembali_ke_awal()

#Tebs
def Tebs():
    HargaT = 14000
    U = int(input("Masukkan Uang Anda : "))
    if (U >= HargaT):
        print("Kembalian Anda = Rp.",U - HargaT)
        print("Pembelian berhasil")
        Membeli_lagi()
    else :
        print("Uang Anda Tidak Mencukupi")
        Kembali_ke_awal()

#Nescafe Black
def Nescafe_Black():
    HargaNB = 10000
    U = int(input("Masukkan Uang Anda : "))
    if (U >= HargaNB):
        print("Kembalian Anda = Rp.",U - HargaNB)
        print("Pembelian berhasil")
        Membeli_lagi()
    else :
        print("Uang Anda Tidak Mencukupi")
        Kembali_ke_awal()

#Good Day
def Good_Day():
    HargaGD = 12500
    U = int(input("Masukkan Uang Anda : "))
    if (U >= HargaGD):
        print("Kembalian Anda = Rp.",U - HargaGD)
        print("Pembelian berhasil")
        Membeli_lagi()
    else :
        print("Uang Anda Tidak Mencukupi")
        Kembali_ke_awal()

#ABC EXO Milk Coffee
def ABC_EXO_Milk_Coffee():
    HargaAEMC = 9000
    U = int(input("Masukkan Uang Anda : "))
    if (U >= HargaAEMC):
        print("Kembalian Anda = Rp.",U - HargaAEMC)
        print("Pembelian berhasil")
        Membeli_lagi()
    else :
        print("Uang Anda Tidak Mencukupi")
        Kembali_ke_awal()

#Delmonte Mocha Latte
def Delmonte_Mocha_Latte():
    HargaDML = 15000
    U = int(input("Masukkan Uang Anda : "))
    if (U >= HargaDML ):
        print("Kembalian Anda = Rp.",U - HargaDML)
        print("Pembelian berhasil")
        Membeli_lagi()
    else :
        print("Uang Anda Tidak Mencukupi")
        Kembali_ke_awal()

#Frestea
def Frestea():
    HargaF = 7500
    U = int(input("Masukkan Uang Anda : "))
    if (U >= HargaF):
        print("Kembalian Anda = Rp.",U - HargaF)
        print("pembelian berhasil")
        Membeli_lagi()
    else :
        print("Uang Anda Tidak Mencukupi")
        Kembali_ke_awal()

#Teh Pucuk Harum
def Teh_Pucuk_Harum():
    HargaTPH = 7000
    U = int(input("Masukkan Uang Anda : "))
    if (U >= HargaTPH):
        print("Kembalian Anda = Rp.",U - HargaTPH)
        print("pembelian berhasil")
        Membeli_lagi()
    else :
        print("Uang Anda Tidak Mencukupi")
        Kembali_ke_awal()

#Ichi Ocha
def Ichi_Ocha():
    HargaIO = 8000
    U = int(input("Masukkan Uang Anda : "))
    if (U >= HargaIO):
        print("Kembalian Anda = Rp.",U - HargaIO)
        print("pembelian berhasil")
        Membeli_lagi()
    else :
        print("Uang Anda Tidak Mencukupi")
        Kembali_ke_awal()

#Teh Javana
def Teh_Javana():
    HargaTJ = 8750
    U = int(input("Masukkan Uang Anda : "))
    if (U >= HargaTJ):
        print("Kembalian Anda = Rp.",U - HargaTJ)
        print("pembelian berhasil")
        Membeli_lagi()
    else :
        print("Uang Anda Tidak Mencukupi")
        Kembali_ke_awal()

#NU Green Tea
def NU_Green_Tea():
    HargaNGT = 9000
    U = int(input("Masukkan Uang Anda : "))
    if (U >= HargaNGT):
        print("Kembalian Anda = Rp.",U - HargaNGT)
        print("pembelian berhasil")
        Membeli_lagi()
    else :
        print("Uang Anda Tidak Mencukupi")
        Kembali_ke_awal()

Menampilkan_daftar_jenis_minuman()