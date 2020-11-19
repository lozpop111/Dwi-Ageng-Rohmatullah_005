import os
import time

while True:
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        #NIM: 2009106005 + 10 = 15
        angka = int(input("Masukkan angka: "))
        n = 1
        s = 1
        while n <= angka:
            print (s)
            s += 1
            if s == 10:
                s -= 9
            n += 1
        break
    except ValueError:
        print("Ups! Itu bukan nomor yang valid. Coba lagi...")
        time.sleep(1.5)