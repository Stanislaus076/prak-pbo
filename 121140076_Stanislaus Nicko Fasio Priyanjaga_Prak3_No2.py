print("========== Praktikum PBO RB Minggu ke-3 ==========")
print("======                                      ======")
print("===                                            ===")
print("")

class AkunBank:
    list_pelanggan = []
    
    def __init__(self, no_pelanggan, nama_pelanggan, jumlah_saldo):
        self.__no_pelanggan = no_pelanggan
        self.__nama_pelanggan = nama_pelanggan
        self.__jumlah_saldo = jumlah_saldo
        self.list_pelanggan.append(self)
        
    def lihat_menu(self):
        print("Selamat datang di bank ITERA")
        print("Hai", self.__nama_pelanggan, "apa yang ingin anda lakukan?")
        print("1. Lihat saldo")
        print("2. Tarik tunai")
        print("3. Transfer saldo")
        print("4. Keluar")
    
    def lihat_saldo(self):
        print(self.__nama_pelanggan, "memiliki saldo Rp", self.__jumlah_saldo)
    
    def tarik_tunai(self):
        nominal = int(input("Masukkan jumlah nominal yang ingin Anda tarik: "))
        if nominal > self.__jumlah_saldo:
            print("Saldo Anda tidak cukup!")
        else:
            self.__jumlah_saldo -= nominal
            print("Saldo berhasil ditarik!")
    
    def transfer(self):
        nominal = int(input("Masukkan nominal yang ingin Anda transfer: "))
        no_rek_tujuan = int(input("Masukkan nomor rekening tujuan: "))
        for pelanggan in self.list_pelanggan:
            if pelanggan.__no_pelanggan == no_rek_tujuan:
                pelanggan.__jumlah_saldo += nominal
                self.__jumlah_saldo -= nominal
                print(f"Transfer Rp {nominal} ke {pelanggan.__nama_pelanggan} sukses!")
                return
        print("No rekening tujuan tidak dikenal! Kembali ke menu utama.")
        
Akun1 = AkunBank(1211, "Priyanjaga", 340000)
Akun2 = AkunBank(4007, "Stanislaus", 570000)
Akun3 = AkunBank(6121, "Nicko", 37000000)

Akun1.lihat_menu()

nomor_input = int(input("Masukkan nomor input: "))
while nomor_input != 4:
    if nomor_input == 1:
        Akun1.lihat_saldo()
        print("")
    elif nomor_input == 2:
        Akun1.tarik_tunai()
        print("")
    elif nomor_input == 3:
        Akun1.transfer()
        print("")
    Akun1.lihat_menu()
    nomor_input = int(input("Masukkan nomor input: "))

print("")
