import sqlite3

# Koneksi ke database
conn = sqlite3.connect('seminar.db')
cursor = conn.cursor()

# Buat tabel jika belum ada
cursor.execute("""
CREATE TABLE IF NOT EXISTS pendaftaran (
    nim TEXT PRIMARY KEY,
    nama TEXT,
    judul TEXT,
    tanggal TEXT
)
""")

# Fungsi untuk mendaftar
def daftar_seminar(nim, nama, judul, tanggal):
    try:
        cursor.execute("INSERT INTO pendaftaran VALUES (?, ?, ?, ?)", 
                       (nim, nama, judul, tanggal))
        conn.commit()
        print("Pendaftaran berhasil!")
    except sqlite3.IntegrityError:
        print("NIM sudah terdaftar.")

# Fungsi untuk melihat daftar pendaftar
def lihat_pendaftar():
    cursor.execute("SELECT * FROM pendaftaran")
    data = cursor.fetchall()
    if data:
        print("Daftar Pendaftar:")
        for row in data:
            print(f"NIM: {row[0]}, Nama: {row[1]}, Judul: {row[2]}, Tanggal: {row[3]}")
    else:
        print("Belum ada pendaftar.")

# Contoh penggunaan
while True:
    print("\nMenu:")
    print("1. Daftar Seminar")
    print("2. Lihat Daftar Pendaftar")
    print("3. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == '1':
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan Nama: ")
        judul = input("Masukkan Judul: ")
        tanggal = input("Masukkan Tanggal: ")
        daftar_seminar(nim, nama, judul, tanggal)
    elif pilihan == '2':
        lihat_pendaftar()
    elif pilihan == '3':
        print("Keluar...")
        break
    else:
        print("Pilihan tidak valid.")

conn.close()
