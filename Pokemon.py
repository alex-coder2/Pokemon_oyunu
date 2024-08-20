import random

bhasar = 50
bsgh = 100
bcan = 100

print("Pokemon oyununa hoş geldiniz")
isim = input("Kullanıcı adınızı giriniz: ")
print("Merhaba " + isim)
print("Pokemonunuzu seçiniz: ")
print("\nBaltazart(1)   Pikachu(2)    Squrtle(3)\nhasar:50       hasar:50      hasar:50\nS.G.H:100      S.G.H:100     S.G.H:100")
psecim = input()

if psecim == "1":
    print("Tebrikler, Baltazart'ı seçtiniz")
    poke = ["Baltazart"]
elif psecim == "2":
    print ("Tebrikler, Pikachu'yu seçtiniz")  
    poke = ["Pikachu"]
elif psecim == "3":
    print("Tebrikler, Squrtle'ı seçtiniz")
    poke = ["Squrtle"]   
     
while True:
    dusman = random.randint(1, 3)

    if dusman == 1:
        dcani = 100
        dhasari = 50
        print("Olamaz, bu bir Charmeleon!")
        print("Ne yapacaksın?")
        print("Saldır(1)  Kaç(2)")
        eylem = input()

        if eylem == "1":
            print("Charmeleon'a saldırdın!")
            print("Charmeleon'un canı: " + str(dcani - bhasar))
            print("Charmeleon saldırdı")
            print("Senin canın: " + str(bcan - dhasari))
            print("Sıra sende ne yapacaksın?")
            print("Saldır(1)  Kaç(2)")
            eylem2 = input()

            if eylem2 == "1":
                print("Tekrar saldırdın!")
                print("Charmeleon öldü, Tebrikler!")
                print("Charmeleon'u yakaladın!")
                poke.append("Charmeleon")
                print("Pokemonlarınızı görmek ister misiniz? Evet(1) Hayır(2)")
                pgorme = input()

                if pgorme == "1":
                    print("Pokemonlarınız: " + str(poke))
                elif pgorme == "2":
                    print("Tamam")

            elif eylem2 == "2":
                print("Saldırıdan kaçtın!")

        elif eylem == "2":
            print("Saldırıdan kaçtın!")
          
    elif dusman == 2:
        dcani = 100
        dhasari = 50
        print("Olamaz, bu bir Snorlax!")
        print("Ne yapacaksın?")
        print("Saldır(1)  Kaç(2)")
        eylem = input()

        if eylem == "1":
            print("Snorlax'a saldırdın!")
            print("Snorlax'ın canı: " + str(dcani - bhasar))
            print("Snorlax saldırdı")
            print("Senin canın: " + str(bcan - dhasari))
            print("Sıra sende ne yapacaksın?")
            print("Saldır(1)  Kaç(2)")
            eylem2 = input()

            if eylem2 == "1":
                print("Tekrar saldırdın!")
                print("Snorlax öldü, Tebrikler!")
                print("Snorlax'ı yakaladın!")
                poke.append("Snorlax")
                print("Pokemonlarınızı görmek ister misiniz? Evet(1) Hayır(2)")
                pgorme = input()

                if pgorme == "1":
                    print("Pokemonlarınız: " + str(poke))
                elif pgorme == "2":
                    print("Tamam")

            elif eylem2 == "2":
                print("Saldırıdan kaçtın!")

        elif eylem == "2":
            print("Saldırıdan kaçtın!")       
          
    elif dusman == 3:
        dcani = 100
        dhasari = 50
        print("Olamaz, bu bir Gengar!")
        print("Ne yapacaksın?")
        print("Saldır(1)  Kaç(2)")
        eylem = input()
         
        if eylem == "1":
            print("Gengar'a saldırdın!")
            print("Gengar'ın canı: " + str(dcani - bhasar))
            print("Gengar saldırdı")
            print("Senin canın: " + str(bcan - dhasari))
            print("Sıra sende ne yapacaksın?")
            print("Saldır(1)  Kaç(2)")
            eylem2 = input()

            if eylem2 == "1":
                print("Tekrar saldırdın!")
                print("Gengar öldü, Tebrikler!")
                print("Gengar'ı yakaladın!")
                poke.append("Gengar")
                print("Pokemonlarınızı görmek ister misiniz? Evet(1) Hayır(2)")
                pgorme = input()

                if pgorme == "1":
                    print("Pokemonlarınız: " + str(poke))
                elif pgorme == "2":
                    print("Tamam")

            elif eylem2 == "2":
                print("Saldırıdan kaçtın!")

        elif eylem == "2":
            print("Saldırıdan kaçtın!")