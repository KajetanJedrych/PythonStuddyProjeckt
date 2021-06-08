from moduly import sniadanie


print("Jaki posiłek chcesz zjeść?\n")
print("1-Śniadanie\n2-Obiad\n3-Kolacje\n")

wybor = input("Wybierz liczbę od 1 do 3: ")
wyborInt = int(wybor)
if wyborInt == 1 :
  print("Co byś chciał zjesc na śniadanie?\n")
  print("1-Jecznica z trzech jajek na maśle (252kcl)\n2-Omlet z 2 jajek i z bananem (320kcl)\n3-Bułka przenna z masłem i wędliną (280kcl )\n")
  wybor1 = input("Wybierz liczbę od 1 do 3: ")
  wyborSniadania = int(wybor1)
  if wyborSniadania == 1:
      print("wybrales jajecznice która ma 252 Kalorii zostało to zapisane w twoim menue!")
      x = sniadanie.sniadanie1(1)
      print(x)
elif wyborInt == 2:  
    print("Obiad") 
elif wyborInt == 3:
    print("Kolacja")     
else:
     print("Podaj właściwą wartość!")

