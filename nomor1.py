def Hashtag(x):
    # dengan menggunakan fungsi title bisa
    # mengubah string menjadi huruf besar pad awal kata
    b = x.title()
    # mengganti spasi dengan string kosong
    c = b.replace(' ','')
    # menambahkan pagar pada variabel c di depan kata
    return ('#'+c)
print(Hashtag('Hello World'))