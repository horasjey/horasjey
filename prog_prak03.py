import sqlite3
koneksi = sqlite3.connect('test.db')
print('Database test.db berhasil dibuka!')
ulangi = 'y'
while (ulangi == 'y'):
    print('No Pegawai?', end='')
    no_preg=input()
    print('Nama?', end='')
    name=input()
    print('Tanggal Lahir?', end='')
    tanggal_lahir = input()
    print('Alamat? ', end='')
    alamat = input()
    print('Gaji?', end='')
    gaji=float(input())
    sql = "INSERT INTO perusahan VALUES (?, ?, ?, ?, ?);"
    koneksi.execute(sql, (no_preg,name,tanggal_lahir,alamat,gaji))
    print('Ulangi (y/t)? ', end='')
    ulangi=input()
koneksi.commit()
print(koneksi.total_changes,'rekaman berhasil dibuat!')
koneksi.close()
