username = "informatika"
password = "12345678"
count = 0

while count < 3:
    data_username = input("Username anda : ")
    data_password = input("Password anda : ")

    if data_username == username and data_password == password:
        print ("Berhasil login")
        break
    else:
        print ("Username atau password salah, coba lagi")
        count += 1

    if count == 3:
        print ("Akun anda telah diblokir")
    
