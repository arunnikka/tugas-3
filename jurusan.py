from datetime import datetime

nama = input("Nama: ")
tempatLahir = input("Tempat Lahir: ")
Tanggallahir = input("Tanggal lahir (format: DD/MM/YYYY): ")
tahun_lahir = int(Tanggallahir.split("/")[-1])
jenis_kelamin = input("Jenis Kelamin (Perempuan/Laki-Laki): ")
nilai_mtk = float(input("Masukkan nilai MTK: "))
nilai_inggris = float(input("Masukkan nilai Inggris: "))
nilai_indonesia = float(input("Masukkan nilai Indonesia: "))

# Hitung rata-rata nilai
rataNilai = (nilai_mtk + nilai_inggris + nilai_indonesia) / 3

# Menentukan jurusan
jurusan = ""
if rataNilai >= 80 and jenis_kelamin.lower() == "laki-laki":
    jurusan = "Teknik Informatika"
elif rataNilai >= 80 and jenis_kelamin.lower() == "perempuan":
    jurusan = "Sistem Informasi"
else:
    jurusan = "DKV"

# Validasi umur
umur = datetime.now().year - tahun_lahir
if umur > 25:
    print("Maaf, Anda tidak memenuhi syarat pendaftaran")
else:
    print(f"Selamat, {nama}, Anda diterima di jurusan {jurusan}")
