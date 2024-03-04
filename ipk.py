#Mengambil input nilai mata kuliah
algoritma = float(input("Masukkan nilai Algoritma: "))
etika = float(input("Masukkan nilai Etika: "))
objec = float(input("Masukkan nilai Objec: "))
kalkulus = float(input("Masukkan nilai Kalkulus: "))
database = float(input("Masukkan nilai Database: "))
english = float(input("Masukkan nilai English: "))

def skorToBobot(skor):
    if skor >= 90:
        return 4
    elif skor >= 84:
        return 3.75
    elif skor >= 80:
        return 3.5
    elif skor >= 75:
        return 3.25
    elif skor >= 65:
        return 2.75
    elif skor >= 60:
        return 2.5
    elif skor >= 55:
        return 2.25
    elif skor >= 50:
        return 2
    elif skor >= 45:
        return 1.75
    elif skor >= 40:
        return 1.5
    elif skor >= 35:
        return 1.25
    elif skor >= 30:
        return 1
    else:
        return 0

nilai_kredit = 3

#Menghitung total bobot untuk setiap mata kuliah
total_algoritma = nilai_kredit * skorToBobot(algoritma)
total_etika = nilai_kredit * skorToBobot(etika)
total_objec = nilai_kredit * skorToBobot(objec)
total_kalkulus = nilai_kredit * skorToBobot(kalkulus)
total_database = nilai_kredit * skorToBobot(database)
total_english = nilai_kredit * skorToBobot(english)

#Menghitung total bobot keseluruhan
total_bobot = total_algoritma + total_etika + total_objec + total_kalkulus + total_database + total_english

#Mencetak IPK
total_sks = 18
ipk = total_bobot / total_sks
print(f"IPK Anda untuk semester ini adalah: {ipk:.2f}")
