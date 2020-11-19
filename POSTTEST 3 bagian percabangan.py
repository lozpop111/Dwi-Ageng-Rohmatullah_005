#Sule memiliki toko kue dimana 1 kue keju seharga 6000 dan 1 kue coklat seharga 3500.
#Setiap hari Sule hanya memproduksi 25 kue keju dan 35 kue coklat. Untuk meramaikan tokonya Sule memberikan sebuah promo. Yaitu:
#- Jika membeli 5 kue coklat hingga 20 mendapat diskon 7%.
#- Jika membeli 21 kue coklat hingga 35 mendapat diskon 12%.
#- Jika membeli 4 kue keju hingga 15 mendapat diskon 10%
#- Jika membeli 16 kue keju hingga 25 mendapat diskon 15%
import os
import time

def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def Toko_kue_Si_Sule():
    Clear()
    print(10*"-","Toko Kue Si Sule",10*"-")
    print("Silahkan pilih","=")
    print("1. Kasir")
    print("2. Persediaan")
    print("3. Rekapan")
    print("0. Exit")
    print("=======================")
    pilih_menu = input("Pilih menu> ")

    if (pilih_menu == "1"):
        kasir()
    elif (pilih_menu == "2"):
        Persediaan()
    elif (pilih_menu == "3"):
        rekapan()
    elif (pilih_menu == "0"):
        exit
    else:
        print("Menu tidak ada")
        kembali_ke_menu()

def kembali_ke_menu():
    print("\n")
    input("Tekan Enter untuk kembali...")
    Toko_kue_Si_Sule()


def beli_kue_coklat(Coklat):
    Persediaan_kue[0] -= Coklat
    if 1 <= int(Coklat) <= 4:
        normal_coklat(Coklat)
    elif 5 <= int(Coklat) <= 20:
        diskon_7(Coklat)
    elif 21 <= int(Coklat) <= 35:
        diskon_12(Coklat)
    elif int(Coklat) == 0:
        Tidak_membeli(Coklat)
    else:
        print("Maaf kue coklat yang tersedia hanya 35 kue perhari")
        kembali_ke_menu()

def beli_kue_keju(Keju):
    Persediaan_kue[1] -= Keju
    if 1 <= int(Keju) <= 3:
        normal_keju(Keju)
    elif 4 <= int(Keju) <= 15:
        diskon_10(Keju)
    elif 16 <= int(Keju) <= 25:
        diskon_15(Keju)
    elif int(Keju) == 0:
        Tidak_membeli(Keju)
    else:
        print("Maaf kue keju yang tersedia hanya 25 kue perhari")
        kembali_ke_menu()

#Buat kue coklat
def normal_coklat(Coklat):
    bayar = int(Coklat) * 3500
    harga.insert(0,bayar)
    print("Harga kue coklat adalah: Rp.", bayar)
def diskon_7(Coklat):
    print("Diskon untuk kue coklat sebesar 7%")
    diskon = (int(Coklat) * 3500 * 7 / 100)
    bayar = int(Coklat) * 3500 - diskon
    harga.insert(0, bayar)
    print("Harga kue coklat adalah: Rp.", bayar)
def diskon_12(Coklat):
    print("Diskon untuk kue coklat sebesar 12%")
    diskon = (int(Coklat) * 3500 * 12 / 100)
    bayar = int(Coklat) * 3500 - diskon
    harga.insert(0, bayar)
    print("Harga kue coklat adalah: Rp.", bayar)
def Tidak_membeli(Coklat):
    bayar = int(Coklat) * 3500
    harga.insert(0, bayar)
    print("Tidak membeli kue")
def kelebihan_keju(Coklat):
    bayar = int(Coklat) * 6000 * 0
    harga.insert(1, bayar)
    print("Maaf kue coklat yang tersedia hanya 35 kue perhari")

#Buat kue keju
def normal_keju(Keju):
    bayar = int(Keju) * 6000
    harga.insert(1, bayar)
    print("Harga kue keju adalah: Rp.", bayar)
def diskon_10(Keju):
    print("Diskon untuk kue keju sebesar 10%")
    diskon = (int(Keju) * 6000 * 10 / 100)
    bayar = int(Keju) * 6000 - diskon
    harga.insert(1, bayar)
    print("Harga kue keju adalah: Rp.", bayar)
def diskon_15(Keju):
    print("Diskon untuk kue keju sebesar 15%")
    diskon = (int(Keju) * 6000 * 15 / 100)
    bayar = int(Keju) * 6000 - diskon
    harga.insert(1, bayar)
    print("Harga kue keju adalah: Rp.", bayar)
def Tidak_membeli(Keju):
    bayar = int(Keju) * 6000
    harga.insert(1, bayar)
    print("Tidak membeli kue")
def kelebihan_keju(Keju):
    bayar = int(Keju) * 6000 * 0
    harga.insert(1, bayar)
    print("Maaf kue keju yang tersedia hanya 25 kue perhari")

def login_akun_bang():
    print('=' * 20)
    print('halaman login')
    username = input('masukan username anda: ')
    password = input('masukan password: ')

    if username == 'sule' and password == 'duar':
        print('login berhasil...\n')
        print('-' * 15)
    else:
        print('silahkan coba lagi..')
        login_akun_bang()

def total_belanja(Coklat, Keju):
    total = harga[0] + harga[1]
    print("Total belanja anda adalah: Rp.",total)
    bayar = int(input("Uang yang diserahkan: "))
    if bayar >= total:
        kembalian = bayar - total
        print("kembalian anda: Rp.",kembalian)
        print("Terima kasih sudah membeli ditoko si sule")
        file_rekapan = open("Catatan.txt", "a")
        teks = "Kue coklat: {} | Kue keju: {} | Bayar: {}\n".format(Coklat, Keju, total)
        file_rekapan.write(teks)
        file_rekapan.close()
        kembali_ke_menu()
    elif bayar < total :
        print("Uang anda tidak mencukupi")
        kembali_ke_menu()

def kasir():
    Coklat = int(input("Jumlah Kue coklat yang dibeli : "))
    beli_kue_coklat(Coklat)
    print('=' * 20)
    Keju = int(input("Jumlah Kue keju yang dibeli : "))
    beli_kue_keju(Keju)
    print('=' * 20)
    total_belanja(Coklat, Keju)
    kembali_ke_menu()

def Persediaan():
    print("kue coklat yang tersedia: ", Persediaan_kue[0])
    print("kue keju yang tersedia: ", Persediaan_kue[1])
    kembali_ke_menu()

def rekapan():
    file_rekapan = open("Catatan.txt", "r")
    rekapan = file_rekapan.read()
    print(rekapan)
    file_rekapan.close()
    kembali_ke_menu()

login_akun_bang()
harga = []
Persediaan_kue = [35,25]
Toko_kue_Si_Sule()
