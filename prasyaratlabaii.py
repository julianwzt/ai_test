def hitung_kembalian(total_belanja, pembayaran):
# Daftar pecahan uang
    pecahan_uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]
    kembalian = pembayaran - total_belanja
    hasil = {}

# Hitung jumlah setiap pecahan
    for pecahan in pecahan_uang:
        jumlah_pecahan = kembalian // pecahan
        kembalian -= jumlah_pecahan * pecahan
        hasil[pecahan] = jumlah_pecahan

    return hasil

# Input dari pengguna
total_belanja = int(input("Masukkan total belanja: "))
pembayaran = int(input("Masukkan jumlah pembayaran: "))

# Panggil fungsi dan tampilkan hasil
kembalian = hitung_kembalian(total_belanja, pembayaran)

print("Kembalian:")
for pecahan, jumlah in kembalian.items():
    if jumlah > 0:
        print(f"- {jumlah} lembar/koin {pecahan} rupiah")