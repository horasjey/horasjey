# deklarasi nilai awal peubah
jumlahSiswa =6
nomor =1 
namaSiswa = []
nAgama = []
nIpa = [] 
nIps = []
nMatematika = []
nRata = []
# repeat as many students
while (nomor < jumlahSiswa ):
    print('Nomor ke-', nomor, sep='')
    print('-->Nama?', sep='', end='')
    nama=input()
    namaSiswa.append(nama)
    print('-->Nilai Agama?', sep='', end='')
    agama=int (input())
    nAgama.append(agama)
    print('-->Nilai Matematika?', sep='', end='')
    matematika=int (input()) 
    nMatematika.append(matematika)
    print('-->Nilai Ipa?', sep='', end='')
    ipa=int (input()) 
    nIpa.append(ipa)
    print('-->Nilai Ips?', sep='', end='')
    ips=int (input()) 
    nIps.append(ips)
    rata=int((agama + matematika + ipa + ips) / 4)
    nRata.append(rata)
    print('-->Nilai Rata-rata=', rata, sep='')
    nomor = nomor + 1
# set ulang nomor ke 1 supaya bisa melakukan perulangan
nomor = 1
i = 0

print('\nRekapitulasi Nilai Siswa')
print('---------------------------------------------------')
print(' No Nama Siswa                 Ipa Ips Aga Mat Rata')
while (nomor < jumlahSiswa):
    print ('%3d %-25s %3d %3d %3d %3d %3d' % (nomor, namaSiswa[i], nIpa[i], nIps[i], nAgama[i], nMatematika[i], nRata[i], ))
    nomor = nomor +1
    i = i + 1
print('---------------------------------------------------')
