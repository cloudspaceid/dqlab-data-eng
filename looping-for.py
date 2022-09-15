list_tagihan = [50000, 75000, -150000, 125000, 300000, -50000, 200000]
total_tagihan = 0
for tagihan in list_tagihan: # untuk setiap tagihan dalam list_tagihan
    total_tagihan += tagihan # tambahkan tagihan ke total_tagihan
print(total_tagihan)

# Looping For Part-2
print ("Looping for part-2")

list_tagihan = [50000, 75000, -150000, 125000, 300000, -50000, 200000]

# For loops with break
print("For loops with break")
total_tagihan_break = 0
for tagihan in list_tagihan:
    if tagihan < 0 :
        print("Terdapat angka minus dalam tagihan, perhitungan dihentikan!")
        break
    total_tagihan_break += tagihan
print("Total tagihan %d." % total_tagihan_break)
print()

# For loops with continue
print("For loops with continue")
total_tagihan_continue = 0
for tagihan in list_tagihan:
    if tagihan < 0:
        print("Terdapat angka minus dalam tagihan, tagihan %d dilewati!" % tagihan)
        continue
    total_tagihan_continue += tagihan
print("Total tagihan %d." % total_tagihan_continue)

# Python for loops – Part 3
list_daerah = ['Malang', 'Palembang', 'Medan']
list_buah = ['Apel', 'Duku', 'Jeruk']
for nama_daerah in list_daerah:
    for nama_buah in list_buah:
        print(nama_buah+" "+nama_daerah)

# Tugas Praktek
list_cash_flow = [2500000, 5000000, -1000000, -2500000, 5000000, 10000000, -5000000, 7500000, 10000000, -1500000, 25000000, -2500000]
total_pengeluaran, total_pemasukan = 0, 0
for dana in list_cash_flow:
    if dana > 0:
        total_pemasukan += dana
    else:
        total_pengeluaran += dana
total_pengeluaran *= -1
print(total_pengeluaran)
print(total_pemasukan)