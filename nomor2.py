def create_phone_number(x):
    # var x1 menampung isi dari join sekaligus hasil looping dari
    # dari varx yang di ubah menjadi string
    x1 = ''.join([str(i) for i in x])
    # lalu langsung di ambil perslice sesuai dengan perintah
    return ("(" + str(x1[0:3] + ")" + " " + str(x1[3:6]) + "-" + str(x1[6:10])))

print(create_phone_number([1,2,3,4,5,6,7,8,9,0]))