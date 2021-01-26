print("")
print("=== UAS Algoritma dan Pemrograman + Pr ===")
print("")
print("Diketahui:")
print("Waktu berangkat Budi = Pukul 05.00")
print("Waktu berangkat Yandi = Pukul 05.15")
print("Kecepatan Budi = 60 km/jam")
print("Kecepatan Yandi = 40 km/jam")
print("Jarak = 150 km")
print("Ditanya:")
print("Waktu berpapasan = ?")

jarak = 150
k1 = 60
k2 = 40
w1 = 05.00
w2 = 05.15
print("")
print("Mencari selisih waktu")
waktu = 315 - 300
print(str(waktu) + " menit")
waktu = 1/4
print("")
print("Mencari selisih jarak")
selisih_jarak = k1 * waktu
print(str(selisih_jarak) + " km")
print("Jadi selisih jarak antara Budi dan Yandi selama 15 menit adalah 15 km")
print("")
print("Mencari waktu berpapasan")
waktu_berpapasan = (jarak - selisih_jarak) / (k1 + k2)
print(str(waktu_berpapasan * 60) + " menit")
waktu_berpapasan = 01.21
print("Pukul berepa mereka berpapasan dapat dihitung dari keberangkatan orang kedua ditambah dengan waktu berpapasan")
print("")
waktu_berpapasan = w2 + waktu_berpapasan
print("Jam " + str(waktu_berpapasan) + " Menit")
print("")
print("Jadi mereka berdua akan berpapasan pada pukul 06.36")