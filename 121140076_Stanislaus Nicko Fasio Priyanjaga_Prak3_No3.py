print("========== Praktikum PBO Minggu ke-3 ==========")
print("=======                                 =======")
print("===                                         ===")
print("")

class Pasien:
    # atribut kelas
    jumlah_pasien = 0
    
    def __init__(self, nama, umur, penyakit):
        self.__nama = nama   # atribut private
        self._umur = umur    # atribut protected
        self.penyakit = penyakit   # atribut public
        Pasien.jumlah_pasien += 1  # menambah jumlah pasien sebanyak +1

    def get_nama(self):
        return self.__nama   # method untuk mengambil atribut private

    def set_umur(self, umur_baru):
        self._umur = umur_baru   # method untuk mengubah atribut protected

    def info_pasien(self):
        return f"{self.__nama}, {self._umur} tahun, menderita {self.penyakit}"


class RumahSakit:
    def __init__(self, nama_rumahsakit):
        self.nama_rumahsakit = nama_rumahsakit
        self.daftar_pasien = []

    def tambah_pasien(self, pasien):
        self.daftar_pasien.append(pasien)

    def info_rumahsakit(self):
        print("Rumah Sakit", self.nama_rumahsakit, "memiliki", Pasien.jumlah_pasien, "pasien:")
        for pasien in self.daftar_pasien:
            print("-", pasien.info_pasien())


# membuat objek pasien
pasien1 = Pasien("Stanislaus", 19, "Batuk")
pasien2 = Pasien("Nicko", 29, "Pilek")
pasien3 = Pasien("Fasio", 49, "Asam Lambung")

# mencetak informasi pasien
print(pasien1.info_pasien())
print(pasien2.info_pasien())
print(pasien3.info_pasien())

print("")

# mengubah umur pasien menggunakan method set_umur()
pasien1.set_umur(20)

# mengambil nama pasien menggunakan method get_nama()
nama_pasien2 = pasien2.get_nama()

# membuat objek rumah sakit dan menambahkan pasien
rumahsakit1 = RumahSakit("Umum Daerah ITERA")
rumahsakit1.tambah_pasien(pasien1)
rumahsakit1.tambah_pasien(pasien2)
rumahsakit1.tambah_pasien(pasien3)

# mencetak informasi rumah sakit dan daftar pasien
rumahsakit1.info_rumahsakit()
