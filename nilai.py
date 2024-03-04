#no 2
#input
nilai_mahasiswa = float(input("Masukan nilai :"))
def konversi(nilai):
    if nilai < 50:
        return 'E'
    elif nilai < 60 :
        return 'D'
    elif nilai < 70:
        return 'C'
    elif nilai < 80:
        return 'B'
    else:
        return 'A'
hasilKonversi = konversi(nilai_mahasiswa)
print("Nilai:",nilai_mahasiswa)
print("Konversi:",hasilKonversi)