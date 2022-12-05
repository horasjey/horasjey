# deklarasi nilai awal peubah
nomor1 =1 
namaSiswa = []
nTinggi = []
nBerat = []
nRata = []
nKet = []
ulangi ='y'
# repeat as many students
while (ulangi == 'y'):
    print('Nomor ke-', nomor1, sep='')
    print('-->Nama?', sep='', end='')
    nama=input()
    namaSiswa.append(nama)
    print('-->Nilai Tinggi M?', sep='', end='')
    tinggi= (input())
    nTinggi.append(tinggi)
    print('-->Nilai Berat Kg?', sep='', end='')
    berat=float (input()) 
    nBerat.append( float(berat))
    #rata=float((tinggi * tinggi) / berat)
    rata=int(berat / (float(tinggi) * float(tinggi)))
    nRata.append(rata)
    #nomor = nomor + 1
    nomor1 = nomor1 + 1
    print ('Ulangi (Y/T)?',sep='.end=')
    ulangi = input ()
# set ulang nomor ke 1 supaya bisa melakukan perulangan

def cek_keterangan (horas):
  if (float(horas) <= 18.5):
    return('Berat badan kurang')
  elif float(horas) >=18.5 and float(horas) <= 22.9:
    return('Berat badan normal')
  elif float(horas) >=23 and float(horas) <= 29.9:
    return('Berat badan berlebih')
  else:
    return('Obesitas')
#selamat_datang('30')
print('\nRekapitulasi Nilai Siswa')
#print(nomor)
print('+---+------------------------+-------+-------+------+-----------------------+')
print ("|{:<3}| {:<23}| {:>6}| {:>6}|{:>6}| {:<21} {:<10}".format('No','Nama Siswa','Berat','Tinggi','IMT','Keterangan','|'))
print('+---+------------------------+-------+-------+------+-----------------------+')
nomor = 1
ulang = nomor1 - 1
i = 0
#print(nomor1)
while (nomor <= ulang):
    print ("|{:<3}| {:<23}| {:>5}0| {:>5}0|{:>6}| {:<21} {:<10}" .format(nomor, namaSiswa[i], float(nTinggi[i]), float(nBerat[i]), nRata[i], cek_keterangan(nRata[i],),'|'))
    nomor = nomor +1
    i = i + 1
print('+---+------------------------+-------+-------+------+-----------------------+')
