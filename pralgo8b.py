# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 21:19:14 2023

@author: gwen
"""
def perpangkat(angka, pangkat):
    if angka == 'z':
        print("program selesai!")
        return None
    elif pangkat == 0:
        return 1
    elif pangkat > 0:
        return angka * perpangkat(angka, pangkat -1)
    else:
        return 1 / (angka * perpangkat(angka, -pangkat - 1))
    
def main():
    print("ini merupakan program pemangkatan negatif dan positif, tekan Z untuk berhenti")
    angka = int(input("masukkan angka: "))
    
    if angka == 'z':
        print("program dihentikan!")
        return
    pangkat = int(input("masukkan pangkat: "))
    hasil = perpangkat(angka, pangkat)
    if hasil is not None:
        print("hasilnya adalah ", hasil)
        main()

    
main()
    
