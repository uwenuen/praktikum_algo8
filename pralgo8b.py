# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 21:19:14 2023

@author: gwen
"""
def perpangkat(angka, pangkat):
    if angka == "":
        print("Program selesai!")
        return None
    elif pangkat == 0:
        return 1
    elif pangkat > 0:
        return angka * perpangkat(angka, pangkat - 1)
    else:
        return 1 / (angka * perpangkat(angka, -pangkat - 1))

def main():
    print("\nIni merupakan program pemangkatan negatif dan positif, tekan eneter untuk berhenti")
    angka = input("Masukkan angka: ")

    if angka == "":
        print("Program dihentikan.")
        return

    angka = float(angka)
    pangkat = int(input("Masukkan pangkat: "))

    hasil = perpangkat(angka, pangkat)
    if hasil is not None:
        print("Hasilnya adalah", hasil)
        main()
    
main()
    
