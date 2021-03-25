count = 0
threshold = 3
user = "muhhendrah@gmail.com"
password = "123456"


while True:
    if count == threshold:
        print("Percobaan login melewati batas!")
        break
    user_name = input("Masukkan username anda: ")
    user_pass = input("Masukkan password anda: ")
    count += 1
    if user_name == user and user_pass == password:
        print("Login berhasil!")
        break
    else:
        print("Username dan Password salah!\nCoba lagi!")