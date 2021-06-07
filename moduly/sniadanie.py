print("Co byś chciał zjesc na śniadanie?\n")
print("1-Jecznica z trzech jajek na maśle (252kcl)\n2-Omlet z 2 jajek i z bananem (320kcl)\n3-Bułka przenna z masłem i wędliną (280kcl )\n")
wybor = input("Wybierz liczbę od 1 do 3: ")
wyborInt = int(wybor)
if wyborInt == 1 or wyborInt == 2 or wyborInt == 3:
    print("Jest ok")
else:
     print("Podaj właściwą wartość!")