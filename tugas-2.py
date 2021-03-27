print ("Selamat Datang!\n")

daftar_kontak = []

def kontak():
    for kontak in daftar_kontak:
        print("Nama: {}" . format(kontak["nama"]))
        print("Telepon: {}" . format(kontak["telepon"]))

def tambah():
    count = int(input("Berapa Kontak: "))
    for i in range(count):
        kontak = {}
        nama_baru = input("Nama: ")
        telepon_baru = input("No. Telepon ")
        kontak["nama"] = nama_baru
        kontak["telepon"] = telepon_baru
        daftar_kontak.append(kontak)
        print("Kontak berhasil ditambahkan")

def keluar():
    print("Program selesai, sampai jumpa!")

menu = " "
while menu != "3":
    print(
        "---Menu---\n"
        "1. Daftar Kontak\n"
        "2. Tambah Kontak\n"
        "3. Keluar\n"
    )
    menu = input("Pilih Menu: ")

    if menu == "1":
        kontak()
    elif menu == "2":
        tambah()
    elif menu == "3":
        keluar()
    else:
        print("Menu tidak tersedia")