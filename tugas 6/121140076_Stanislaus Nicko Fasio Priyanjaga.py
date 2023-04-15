from abc import ABC, abstractmethod
from datetime import datetime

class AkunBank(ABC):
    def __init__(self, nama, tahun_daftar, saldo):
        self.nama = nama
        self.tahun_daftar = tahun_daftar
        self.saldo = saldo
        
    def lihat_saldo(self):
        print(f"Saldo {self.nama}: {self.saldo}")
    
    @abstractmethod
    def transfer_saldo(self, jumlah):
        pass
    
    @abstractmethod
    def lihat_suku_bunga(self):
        pass
        
class AkunGold(AkunBank):
    def transfer_saldo(self, jumlah):
        biaya_admin = 0
        usia_akun = datetime.now().year - self.tahun_daftar
        if usia_akun >= 3 and jumlah > 100000:
            biaya_admin = 0
        elif usia_akun < 3 and jumlah > 100000:
            biaya_admin = 2000
        
        self.saldo -= jumlah + biaya_admin
        print(f"Transfer sebesar {jumlah} berhasil dilakukan dengan biaya administrasi sebesar {biaya_admin}")
    
    def lihat_suku_bunga(self):
        usia_akun = datetime.now().year - self.tahun_daftar
        if usia_akun >= 3 and self.saldo >= 1000000000:
            bunga = 0.01
        elif usia_akun < 3 and self.saldo >= 1000000000:
            bunga = 0.02
        else:
            bunga = 0.03
            
        print(f"Suku bunga akun {self.nama} adalah {bunga}")
        

class AkunSilver(AkunBank):
    def transfer_saldo(self, jumlah):
        biaya_admin = 0
        usia_akun = datetime.now().year - self.tahun_daftar
        if usia_akun >= 3 and jumlah > 100000:
            biaya_admin = 2000
        elif usia_akun < 3 and jumlah > 100000:
            biaya_admin = 5000
        
        self.saldo -= jumlah + biaya_admin
        print(f"Transfer sebesar {jumlah} berhasil dilakukan dengan biaya administrasi sebesar {biaya_admin}")
    
    def lihat_suku_bunga(self):
        usia_akun = datetime.now().year - self.tahun_daftar
        if usia_akun >= 3 and self.saldo >= 10000000:
            bunga = 0.01
        elif usia_akun < 3 and self.saldo >= 10000000:
            bunga = 0.02
        else:
            bunga = 0.03
            
        print(f"Suku bunga akun {self.nama} adalah {bunga}")


# Membuat objek akun gold dan silver
akun1 = AkunGold("Akun Gold", 2015, 1500000000)
akun2 = AkunSilver("Akun Silver", 2020, 5000000)

# Transfer saldo ke akun gold
akun1.transfer_saldo(50000000)
akun1.lihat_saldo()

# Transfer saldo ke akun silver
akun2.transfer_saldo(150000)
akun2.lihat_saldo()


