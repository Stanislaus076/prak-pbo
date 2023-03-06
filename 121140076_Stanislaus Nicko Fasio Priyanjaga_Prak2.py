class Orang:
    def __init__(self, nama, nim, kelas_pbo_siakad, jumlah_sks):
        self.nama = nama
        self.nim = nim
        self.kelas_pbo_siakad = kelas_pbo_siakad
        self.jumlah_sks = jumlah_sks

    def panggilmahasiswa(self):
        print("Orang ini bernama", self.nama, "dengan nim" , self.nim, "dari kelas", self.kelas_pbo_siakad, "serta jumlah sksnya", self.jumlah_sks)

ini_objek = Orang("Nicko", 121140076, "RB", 12)

ini_objek.panggilmahasiswa()

