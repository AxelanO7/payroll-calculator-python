nama = input("Masukkan nama karyawan: ")
golongan = int(input("Masukkan golongan (1/2/3): "))
status = input("Status pernikahan (TM/M/J/D): ")

gaji_pokok = 0
if golongan == 1:
    gaji_pokok = 2500000
if golongan == 2:
    gaji_pokok = 3000000
if golongan == 3:
    gaji_pokok = 5000000
else:
    print("Golongan tidak valid")

tunjangan = 0

if status != ("M"):
    tunjangan = 0
elif status == ("J"):    
    tunjangan = 0
elif status == ("D"):
    tunjangan = 0
elif status == ("TM"):
    tunjangan = 0
else:
    tunjangan = 0.1 * gaji_pokok


# if status == ("M"):
#     tunjangan = 0.1 * gaji_pokok
# elif status == ("J"):
#     tunjangan = 0
# elif status == ("D"):
#     tunjangan = 0
# elif status == ("TM"):
#     tunjangan = 0
# else:
#     tunjangan = 0

total_gaji = gaji_pokok + tunjangan

print("Data Karyawan")
print("Nama: ", nama)
print("Golongan: ", golongan)
print("Status Pernikahan: ", status)
print("Gaji Pokok: ", gaji_pokok)
print("Tunjangan: ", tunjangan)
print("Total Gaji: ", total_gaji)