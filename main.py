from moduly import sniadanie
from moduly import obiad
from moduly import kolacja
import os
menue = {}
posilki = [""]
end = 0
licznik=0
kalorie = 0
while end != 1: 
  print("-"*40)
  print("Jaki posiłek chcesz zjeść?")
  print("-"*40 + "\n")
  print("1-Śniadanie\n2-Obiad\n3-Kolacje\n")
  print("4-Zakończ program")
  print("-"*40)
  menue[licznik]=(posilki[-1])
  wybor = input("Wybierz liczbę od 1 do 4: " +"\n \n \n")
  wyborInt = int(wybor)
  if wyborInt == 1 :
    print("-"*40)    
    print("Co byś chciał zjesc na śniadanie?\n")
    print("-"*40)
    print("1-Jecznica z trzech jajek na maśle (252kcl)\n2-Omlet z 2 jajek i z bananem (320kcl)\n3-Bułka przenna z masłem i wędliną (280kcl )\n")
    wybor1 = input("Wybierz liczbę od 1 do 3: ")
    print("-"*40)
    licznik = licznik+ 1
    wyborSniadania = int(wybor1)
    if wyborSniadania == 1:
      print("wybrales jajecznice która ma 252kcl zostało to zapisane w twoim menue!\n")
      kalorie = sniadanie.sniadanie1(1) + kalorie
      posilki.append("Jecznica z trzech jajek na maśle (252kcl) ")
    elif wyborSniadania ==2:
       print("Wybrales omlet z dwóch jajek i bananem który ma 320kcl zostało to zapisane w twoim menue!\n")
       kalorie = sniadanie.sniadanie1(2) +kalorie
       posilki.append("Omlet z 2 jajek i z bananem (320kcl)")
    elif wyborSniadania ==3:
        print("Wybrales Bułkę przenną z masłem i wędliną która ma 280kcl zostało to zapisane w twoim menue!\n")
        kalorie = sniadanie.sniadanie1(3) +kalorie
        posilki.append("Bułka przenna z masłem i wędliną (280kcl )")   

  elif wyborInt == 2:  
     print("-"*40)
     print("Co byś chciał zjesc na obiad?\n")
     print("-"*40)
     print("1-Pieczona pierś z Kurczaka z ryżem (520kcl)\n2-Makaron ryżowy z wieprzowiną w sosie słodko kwaśnym (640kcl)")
     print("3-Mc-royoal+Frytki+kola(1134kcl )\n")
     wybor2 = input("Wybierz liczbę od 1 do 3: ")
     print("-"*40)
     licznik = licznik+ 1
     wyborObiad = int(wybor2)
     if wyborObiad == 1:
      print("wybrales pierś z kurczaka z ryżem która ma 2520 Kalorii zostało to zapisane w twoim menue!\n")
      kalorie = obiad.obiad1(1) +kalorie
      posilki.append("Pieczona pierś z Kurczaka z ryżem (520kcl)")
     elif wyborObiad ==2:
       print("Wybrales makaron ryżowy z wieprzowiną który ma 320kcl zostało to zapisane w twoim menue!\n")
       kalorie = obiad.obiad1(2) +kalorie
       posilki.append("Makaron ryżowy z wieprzowiną w sosie słodko kwaśnym (640kcl)")
     elif wyborObiad ==3:
        print("Wybrales zestaw z mc Donalad'a która ma 1134kcl zostało to zapisane w twoim menue!\n")
        kalorie = obiad.obiad1(3) +kalorie
        posilki.append("3-Mc-royoal+Frytki+kola(1134kcl)")
  elif wyborInt == 3:
    print("-"*40)
    print("Co byś chciał zjesc na kolację?\n")
    print("-"*40)
    print("1-serek wiejski z rzodkiewką i kromką chleba przennego (265kcl)\n2-Twaróg na słodko z miodem i orzechami(540kcl)")
    print("3-Kebab z lokalnej kebabowni(670kcl )\n")
    wybor3 = input("Wybierz liczbę od 1 do 3: ")
    print("-"*40)
    licznik = licznik+ 1
    wyborKolacja = int(wybor3)
    if wyborKolacja == 1:
      print("wybrales serek wiejski z rzodkiewką i kromką chleba który ma 265kcl zostało to zapisane w twoim menue!\n")
      kalorie = kolacja.kolacja1(1) + kalorie
      posilki.append("serek wiejski z rzodkiewką i kromką chleba przennego (265kcl)")
    elif wyborKolacja ==2:
       print("Wybrales Twaróg z miodem i orzechami który ma 540kcl zostało to zapisane w twoim menue!\n")
       kalorie = kolacja.kolacja1(2) + kalorie
       posilki.append("Twaróg na słodko z miodem i orzechami(540kcl)")
    elif wyborKolacja ==3:
        print("Wybrales Kebaba 670kcl zostało to zapisane w twoim menue!\n")
        kalorie= kolacja.kolacja1(3) + kalorie
        posilki.append("Kebab z lokalnej kebabowni(670kcl )")
  elif wyborInt ==4:
    print(menue) 
    str1= "liczba kalori którą dzisaj zjadłes to: {0} ".format(kalorie)
    end = 1
    if os.path.isfile('menue.txt'):
          os.remove("menue.txt")
          plik = open("menue.txt", 'w')
          plik.write(str(menue) + "\n")
          plik.write(str(str1))
          plik.close()
    else:      
          plik = open("menue.txt", 'w')
          plik.write(str(menue) + "\n")
          plik.write(str(str1))
          plik.close()
  else:
     print("Podaj właściwą wartość!")

