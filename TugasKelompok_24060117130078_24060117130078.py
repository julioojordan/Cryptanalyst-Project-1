# TUGAS KELOMPOK KRIPTOGRAFI
# ENKRIPSI MENGGUNAKAN PLAYFAIR
# DEKRIPSI DENGAN SUPER ENKRIPSI DAN SUBTITUSI

#JULIO ANDYAN JORDAN ARYANTO (24060117130078)
# M NURFAJAR IQBAL (24060117130076)

from array import *
from nltk import *

#CATATAN :
# ENKRIPSI PLAYFAIR MENGGUNAKAN KATA KUNCI "ATHEM"
# DEKRIPSI :
# a) dengan Super Enkripsi menggunakan subtitusi caesar cipher dengan kata kunci digeser sebesar 3 huruf ke kanan
# dan dilanjut menggunakan Transposisi -> dimana matrikx dari hasilnya selalu memiliki 4 kolom
# b) dengan subtitusi caesar cipher dengan kata kunci digeser sebesar 3 huruf ke kanan

#MULAI
# Inisialisasi

#Fungsi Dekripsi subtitusi Caesar Cipher
def SDekripsi(Kar):
    if Kar == 'D' :
        return 'A'
    elif Kar =='E':
        return 'B'
    elif Kar =='F':
        return 'C'
    elif Kar =='G':
        return 'D'
    elif Kar =='H':
        return 'E'
    elif Kar =='I':
        return 'F'
    elif Kar =='J':
        return 'G'
    elif Kar =='K':
        return 'H'
    elif Kar =='L':
        return 'I'
    elif Kar =='M':
        return 'J'
    elif Kar =='N':
        return 'K'
    elif Kar =='O':
        return 'L'
    elif Kar =='P':
        return 'M'
    elif Kar =='Q':
        return 'N'
    elif Kar =='R':
        return 'O'
    elif Kar =='S':
        return 'P'
    elif Kar =='T':
        return 'Q'
    elif Kar =='U':
        return 'R'
    elif Kar =='V':
        return 'S'
    elif Kar =='W':
        return 'T'
    elif Kar =='X':
        return 'U'
    elif Kar =='Y':
        return 'V'
    elif Kar =='Z':
        return 'W'
    elif Kar =='A':
        return 'X'
    elif Kar =='B':
        return 'Y'
    elif Kar =='C':
        return 'Z'
    else :
        return ''

#fungsi untuk mengecek apakah ada huruf yang sama pada plain teks
#def equal, digunakan untuk menambahan huruf dummy pada 2 huruf yang sama
def Equal(teks, D):
    k = 0
    for i in range(len(teks)):
        if (i+1)< len(teks):
            if teks[i] == teks[i+1]:
                k = k + 1
                teks.insert(i+1, D)
    if k != 0 :
        print ("Terdapat beberapa karakter berurutan yang sama")
        print ("Sehingga Plainteks diubah menjadi: ")
    else :
        print ("Plainteks :")

    print (teks)
    print ("=============================")
    return teks


# kunci untuk tabel playfair adalah ATHEM
TPlayfair = [
    ["A", "T", "H", "E", "M"],
    ["B", "C", "D", "F", "G"],
    ["I", "K", "L", "N", "O"],
    ["P", "Q", "R", "S", "U"],
    ["V", "W", "X", "Y", "Z"]
]

# karakter dummy D
D = "X"


#Realisasi

def begin():
    print ("=============================")

    print ("Apa yang ingin Dilakukan ?")
    print ("1. Enkripsi dengan Playfair")
    print ("2. Dekripsi dengan Super Enkripsi")
    print ("3. Dekripsi dengan Subtitusi Caesar Cipher")
    print ("=============================")

    pil = input("Masukan Pilihan Anda:")

    if pil == '1':
        Playfair()
    elif pil == '2':
        SuperEnkripsi()
    elif pil == '3':
        SubtitusiCaesarCipher()
    else :
        begin()
#==============================
def Playfair():
    #List untuk hasil ekripsi
    TCipher = []

    #-----Tahap 1 -----
    Pteks = input("Masukan Plainteks : ")
    #mengubah semua inputan teks menjadi kapital
    Pteks = Pteks.upper()
    #menghilangkan spasi di Pteks
    Ateks = []
    for j in range(len(Pteks)):
        if Pteks[j] != ' ' :
            if Pteks[j] == 'J':
                Ateks.append('I')
            else:
                Ateks.append(Pteks[j])

    teks = Equal(Ateks, D)
    
    #mengecek apakah Ateks Ganjil
    if len(teks) % 2 != 0:
        teks.insert(len(teks)+1, D)
    #-----End Tahap 1 -----

    #----- Tahap 2 -----
    #Operasi bigram
    teks = bigrams(teks)
    BList1= [] #ini hasil dari fungsi bigram python
    BList = [] # ini adalah bigram  yang akan digunakan
    for grams in teks:
        BList1.append(grams)

    #BList diisi disini
    for i in range(len(BList1)):
        if i == 0 :
            BList.append(BList1[i])
        else : #i!=0
            if i % 2 == 0:
                BList.append(BList1[i])
    #-----End Tahap 2-----

    #----- Tahap 3-----
    #Mulai operasi Playfair
    for i in range(len(BList)):
        #inisialisasi baris kolom
        b = []
        k = []
        for j in range(2):
            P = BList[i][j]
            #perhitungan untuk mendapatkan indeks dari
            #Plainteks P pada TPlayfair
            for s in range(5):
                for p in range(5):
                    if TPlayfair[s][p] == P :
                        b.append(s)
                        k.append(p)
        #apabila dalam 1 kolom yang sama
        if k[0] == k[1] :
            b1 = b[0] + 1
            b2 = b[1] + 1
            if b1 == 5 :
                b1 = 0
            if b2 == 5:
                b2 =0
            k1 = k[0]
            k2 = k[1]
                
        #apabila dalam 1 baris yang sama
        elif b[0] == b[1] :
            b1 = b[0]
            b2 = b[1]
            k1 = k[0] + 1
            k2 = k[1] + 1
            if k1 == 5 :
                k1 = 0
            if k2 == 5:
                k2 =0
                
        #apabila posisi baris dan kolom beda
        else:
            k.reverse()
            b1 = b[0]
            b2 = b[1]
            k1 = k[0]
            k2 = k[1]
        #pada posisi ini sudah didapat index chiper
        #dari tabel Playfair
        #mulai mengambil nilai chipper dari TPlayfair
        #dan memasukan ke array TCipher
        TCipher.append(TPlayfair[b1][k1])
        TCipher.append(TPlayfair[b2][k2])

    #hasil enkripsi
    print ("Cipherteks yang didapatkan dari enkripsi Playfair adalah ="+" ".join(TCipher))
    begin()
#==============================

#==============================
def SuperEnkripsi():
    #List untuk hasil Dkripsi 
    Dteks1 = [] #hasil untuk dekripsi transposisi
    Dteks2 = [] #hasil untuk dekripsi caesar cipher

    teks = input("Masukan Cipher teks : ")
    #mengubah semua inputan teks menjadi kapital
    Cteks = teks.upper()
    #menghilangkan spasi di Cteks
    Ateks = []
    for j in range(len(Cteks)):
        if Cteks[j] != ' ' :
            Ateks.append(Cteks[j])
    print(Ateks)

    #----- Tahap 1 -----
    #melakukan dekripsi dengan Transposisi
    #asumsi :matriks transposisi harus 4 baris
    data_matrix = [[] for k in range(4)]
    JKolom = int(len(Ateks)/4)
    counter = 0
    for baris in range(len(data_matrix)):
        for kolom in range(JKolom):
            data_matrix[baris].append(Ateks[counter])
            counter = counter + 1
    #print (data_matrix)
    #print (len(data_matrix)) #baris 
    #print (len(data_matrix[0])) #kolom
    #----- END Tahap 1 -----

    #----- Tahap 2 -----
    #tranpose data_matrix untuk mendapatkan
    #hasil dekripsi dari transposisi
    temp_row = []
    tranpose_matrix = []

    for kolom in range(len(data_matrix[0])):
        for baris in range(len(data_matrix)):
            temp_row.append(data_matrix[baris][kolom])
        tranpose_matrix.append(temp_row)
        temp_row = []
    #print(tranpose_matrix)
    #----- END Tahap 2-----

    #----- Tahap 3 -----
    #memasukan hasil tranpose matriks ke Dteks1
    for baris in range(len(tranpose_matrix)):
        for kolom in range(len(tranpose_matrix[0])):
            Dteks1.append(tranpose_matrix[baris][kolom])
    #print(Dteks1)
    #----- END Tahap 3-----

    #----- Tahap 4 -----
    #melakukan dekripsi caesar cipher ke Dteks1
    #untuk mendapatkan Dteks 2/ Hasil Akhir
    for i in range(len(Dteks1)):
        Dteks2.append(SDekripsi(Dteks1[i]))
    #print(Dteks2)

    #----- END Tahap 4 -----
    print ("Plainteks yang didapatkan dari dekripsi Super Enkripsi adalah ="+" ".join(Dteks2))
    begin()
#==============================

#==============================    
def SubtitusiCaesarCipher():
    #List untuk Hasil Dekripsi
    Pteks = []

    teks = input("masukan cipher teks : ")
    #mengubah semua inputan teks menjadi kapital
    Cteks = teks.upper()
    #menghilangkan spasi di Cteks
    Ateks = []
    for j in range(len(Cteks)):
        if Cteks[j] != ' ' :
            Ateks.append(Cteks[j])
    print(Ateks)

    #mulai proses dekripsi
    for i in range(len(Ateks)):
        Pteks.append(SDekripsi(Ateks[i]))
    print ("Plainteks yang didapatkan dari dekripsi Caesar Cipher adalah ="+" ".join(Pteks))
    begin()
#==============================

#==============================
begin()




                
