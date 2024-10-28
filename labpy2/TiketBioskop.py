def hitung_harga_tiket():
    # Harga tiket
    harga_reguler = 50000
    harga_vip = 100000
    diskon_member = 0.20
    
    # Input dari pengguna
    tipe_tiket = input("Masukkan tipe tiket (reguler/vip): ").strip().lower()
    member = input("Apakah Anda memiliki kartu member? (ya/tidak): ").strip().lower()

    # Menentukan harga berdasarkan tipe tiket
    if tipe_tiket == "reguler":
        harga_tiket = harga_reguler
    elif tipe_tiket == "vip":
        harga_tiket = harga_vip
    else:
        print("Tipe tiket tidak valid.")
        return

    # Menghitung total harga menggunakan operator ternary
    total_harga = harga_tiket * (1 - diskon_member) if member == "ya" else harga_tiket

    # Menampilkan hasil
    print(f"Total harga yang harus dibayar: Rp{total_harga:.2f}")

# Menjalankan fungsi
hitung_harga_tiket()