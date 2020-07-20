def sort_odd_even(x):
    # menggunakan fungsi sort yang di iterasi dari varibel x dan memasukan
    # hasil ke variabel num
    ganjil = sorted([num for num in x if num % 2 != 0])
    # mengambil angka yang tidak habis di bagi 2
    print('ini adalah angka',ganjil)
    # menyiapkan list kosong untuk hasil loop
    hasil = []
    for num in x:
        # karena looping pertama nilai ganjil
        # maka langsung mengappen dari var odd ke hasil
        # yang mana hasilnya adalah bilangan 1
        if num % 2 == 0:
            hasil.append(num)
        else:
            # jika hasil tidak habis di bagi 2
            # maka di tambah ke var hasil
            hasil.append(ganjil[0])
            # ganjil pop untuk menghapus angka 0
            ganjil.pop(0)
    return hasil

print(sort_odd_even([5,3,2,8,1,4]))