# fonksiyonlar------------------------------------------------


krediler = ["Hızlı Kredi","Maaşını Halkbank'tan Alanlara Özel Kredi","Mutlu Emekli İhtiyaç Kredisi"]

# alias
def kredileriListele():
    for kredi in krediler:
            print("<option>" + kredi + "<option>")


kredileriListele()
kredileriListele();
kredileriListele();
kredileriListele();
kredileriListele();
kredileriListele();
kredileriListele();


# çift sayı---------------------------------------------------

def sayilarEnBuyuk():
    sayilar=[]

    for i in range(10):
        i=int(input("sayi giriniz:"))
        sayilar.append(i)

        print(sayilar)
    enbuyukdegisken=max(sayilar)
    print(enbuyukdegisken)


sayilarEnBuyuk()


# fibonacci---------------------------------------------------

def fibonacciListesi():
    fibonacciList=[]
    a=1
    b=0
    toplam=0
    for i in range(20):
        toplam=a+b
    a=b
    b=toplam
    fibonacciList.append(toplam)
    print(fibonacciList)


fibonacciListesi()


# mükemmel sayi-----------------------------------------------

def mukemmelSayi():
    sayi=int(input("Sayı Giriniz: "))
    toplam=0
    for i in range(1,sayi):
        if sayi%i==0:
            toplam += i
        if toplam==sayi:
            print("Bu mükemmel sayıdır")
        else:
            print("Mükemmel sayı değildir")


mukemmelSayi()
