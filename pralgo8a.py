# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:10:03 2023

@author: user
"""
def rekursif(angka):
    if angka > 1:
        jumlahan= int(input(f"masukkan bilangan ke-{angka}: " ))
        angka = angka -1
        return jumlahan + rekursif(angka)
    else:
        return int(input(f"masukkan bilangan ke-{angka}: " ))
        
masukkan = int(input("masukkan jumlah: "))

if masukkan <1:
    print("hasil penjumlahan: 0")
else:
    hasil = rekursif(masukkan)
    print(f"hasil penjumlahan: {hasil}")