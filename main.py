print("Jaki posiłek chcesz zjeść?\n")
print("1-Śniadanie\n2-Obiad\n3-Kolacje\n")

wybor = input("Wybierz liczbę od 1 do 3: ")
wyborInt = int(wybor)
if wyborInt == 1 :
    print("Jest ok")
    from moduly import  sniadanie 
elif wyborInt == 2:  
    print("Obiad") 
elif wyborInt == 3:
    print("Kolacja")     
else:
     print("Podaj właściwą wartość!")

