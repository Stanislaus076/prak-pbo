print("========== Praktikum PBO Minggu ke-4 ==========")
print("======                                   ======")
print("===                                         ===")
print("")

class Komputer:
    def __init__(self, nama, jenis, harga, merk):
        self.nama = nama
        self.jenis = jenis
        self.harga = harga
        self.merk = merk

class Processor(Komputer):
    def __init__(self, merk, nama, harga, jumlah_core, kecepatan_processor):
        super().__init__(nama, 'Processor', harga, merk)
        self.jumlah_core = jumlah_core
        self.kecepatan_processor = kecepatan_processor

class RAM(Komputer):
    def __init__(self, merk, nama, harga, capacity):
        super().__init__(nama, 'RAM', harga, merk)
        self.capacity = capacity

class HDD(Komputer):
    def __init__(self, merk, nama, harga, capacity, rpm):
        super().__init__(nama, 'SATA', harga, merk)
        self.capacity = capacity
        self.rpm = rpm

class VGA(Komputer):
    def __init__(self, merk, nama, harga, capacity):
        super().__init__(nama, 'VGA', harga, merk)
        self.capacity = capacity

class PSU(Komputer):
    def __init__(self, merk, nama, harga, daya):
        super().__init__(nama, 'PSU', harga, merk)
        self.daya = daya

# contoh penggunaan
p1 = Processor('Intel', 'Core i7 7740X', 4350000, 4, '4.3GHz')
ram1 = RAM('V-Gen', 'DDR4 SODimm PC19200/2400MHz', 328000, '4GB')
hdd1 = HDD('Seagate', 'HDD 2.5 inch', 295000, '500GB', 7200)
vga1 = VGA('Asus', 'VGA GTX 1050', 250000, '2GB')
psu1 = PSU('Corsair', 'Corsair V550', 250000, '500W')

p2 = Processor('AMD', 'Ryzen 5 3600', 250000, 4, '4.3GHz')
ram2 = RAM('G.SKILL', 'DDR4 2400MHz', 328000, '4GB')
hdd2 = HDD('Seagate', 'HDD 2.5 inch', 295000, '1000GB', 7200)
vga2 = VGA('Asus', '1060Ti', 250000, '8GB')
psu2 = PSU('Corsair', 'Corsair V550', 250000, '500W')

rakit = [[p1, ram1, hdd1, vga1, psu1], [p2, ram2, hdd2, vga2, psu2]]

# menampilkan data
for idx, komputer in enumerate(rakit):
    print(f"Komputer {idx+1}")
    for komponen in komputer:
        print(f"{komponen.jenis} {komponen.nama} produksi {komponen.merk}")
    print("\n")

