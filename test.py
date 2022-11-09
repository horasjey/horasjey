#Tugas pak beno pertemuan ke-11
#Scrip by Horas Hajovan Siregar
#09/11/2022
BATU = 1
GUNTING = 2
KERTAS = 3

#Deklarasi peubah untuk nilai cacah
i = 0

# Impor fungsi pembuatan angka acak
import random
#Deklarasi peubah untuk sakor
skorKom = 0
skorAnda = 0
skorSeri = 0
#ulangi sampai pilihan 0

while (True):
  i = i + 1
  valid = False
  while (valid == False):
    print('Pilihan(1=Batu,2=GUNTING,3=Kertas,0=Keluar)?', sep='', end='')
    masukan = input()
    if (masukan.isdigit()) and (int(masukan) >= 0) and (int(masukan) <= 3):
      valid = True
    else:
      print('ERROR : masukkan angka 0-3!')
  anda = int(masukan)
  if (anda == 0):
    i = i - 1
    break
  elif (anda == BATU):
    print("Anda memilih BATU!")
  elif (anda == GUNTING):
    print("Anda memilih GUNTING!")
  else:
    print("Anda memilih KERTAS")
##jawaban komputer
  kom = random.randint(1, 3)
  if (kom == BATU):
    print('Kom memilih BATU!')
  elif (kom == GUNTING):
    print("Kom memilih GUNTING!")
  else:
    print("Kom memilih KERTAS")
  #Penentuan pemenang
  if (kom == BATU) and (anda == GUNTING):
    print('-->Kom menang!')
    skorKom = skorKom + 1
  elif (kom == BATU) and (anda == KERTAS):
    print('Anda Menang!')
    skorAnda = skorAnda + 1
  elif (kom == GUNTING) and (anda == KERTAS):
    print('Kom Menang!')
    skorKom = skorKom + 1
  elif (anda == BATU) and (kom == GUNTING):
    print('Anda Menang!')
    skorAnda = skorAnda + 1
  elif (anda == BATU) and (kom == KERTAS):
    print('Kom Menang!')
    skorKom = skorKom + 1
  elif (anda == GUNTING) and (kom == KERTAS):
    print('Anda Menang!')
    skorAnda = skorAnda + 1
  else:
    print("--> Anda Dan Kom seri!")
    skorSeri = skorSeri + 1

print('\nHasil Pertandingan')
print('---------------------')
print("Jumlah Pertandingan =", i)
print('---> Skor Anda=', skorAnda)
print('---> Skor Kom=', skorKom)
print('---> Skor Seri=', skorSeri)
