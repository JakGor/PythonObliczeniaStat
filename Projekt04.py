# -*- coding: utf-8 -*-

import tkinter
from Funkcje import *


import matplotlib.pyplot as plt

##########################################

def czytaj(d):
    s_wartosci=e_wartosci.get()
    a= s_wartosci.split(",")
    for j in  a:
        if is_number(j)== True :
             d.append(float(j))
    return d
##########################################
def czytaj_liczebnosc(tmp):
    s_liczebnosc=e_liczebnosc.get()
    c= s_liczebnosc.split(",")
    for j in  c:
        if is_number(j)== True :
             tmp.append(float(j))
    return tmp
##########################################
def licz_srednia():
    lista=[]
    suma=0
    czytaj(lista)
    dlugosc=len(lista)
    for i in lista:
        suma= suma + i

    srednia = suma/dlugosc
    l.config(text=srednia)
    lwynik.config(text="Średnia to : ")
    return srednia
##########################################
def licz_srednia_wazona():


    lista=[]
    suma=0
    czytaj(lista)
    s_liczebnosc=e_liczebnosc.get()
    c= s_liczebnosc.split(",")

    lista_liczebnosc=[]
    liczebnosc=0
    j=0
    for j in  c:
        if is_number(j)== True :
             lista_liczebnosc.append(float(j))

    for i in lista_liczebnosc:
        liczebnosc= liczebnosc + i
    j=0
    for i in lista:
        suma= i*lista_liczebnosc[j] + suma
        j+=1

    srednia_wazona = suma/liczebnosc
    l.config(text=srednia_wazona)
    lwynik.config(text="Średnia ważona to : ")

    return srednia_wazona
##########################################
def licz_sredna_geometryczna():
    lista = []
    lista_liczebnosc = []
    czytaj(lista)
    czytaj_liczebnosc(lista_liczebnosc)
    liczebnosc = 0
    for i in lista_liczebnosc:
        liczebnosc += i
    iloczyn = 1
    k = 0
    for j in lista:
        iloczyn *= j ** lista_liczebnosc[k]
        k += 1

    srednia = iloczyn ** (1/liczebnosc)
    l.config(text=srednia)
    lwynik.config(text="Średnia geometryczna to : ")
    return srednia
##########################################
def licz_sredna_harmoniczna():
    lista = []
    lista_liczebnosc = []
    czytaj(lista)
    czytaj_liczebnosc(lista_liczebnosc)
    liczebnosc = 0
    for i in lista_liczebnosc:
        liczebnosc += i
    suma = 0
    k = 0
    for j in lista:
        suma += (1/j)*lista_liczebnosc[k]
        k += 1

    srednia = liczebnosc/suma
    l.config(text=srednia)
    lwynik.config(text="Średnia harmoniczna to : ")
    return srednia
##########################################
def licz_dominanta():
    lista = []
    lista_liczebnosc = []
    czytaj(lista)
    czytaj_liczebnosc(lista_liczebnosc)
    maks = lista_liczebnosc[0]
    maxindx = 0
    i = 1
    if i < len(lista):
        while (i < len(lista)):
            if lista_liczebnosc[int(i)] > maks:
                maks = lista_liczebnosc[int(i)]
                maxindx = i

            i += 1

    dominanta = lista[maxindx]
    l.config(text=dominanta)
    lwynik.config(text="Dominanta to : ")
    return dominanta
##########################################
def sortowanie(lista,lista_liczebnosc):
    czytaj(lista)
    czytaj_liczebnosc(lista_liczebnosc)

    j = 0
    while j < (len(lista) - 1):
        i = 0
        while i < (len(lista) - 1):
            if lista[i] > lista[i + 1]:
                a = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = a

                a = lista_liczebnosc[i]
                lista_liczebnosc[i] = lista_liczebnosc[i + 1]
                lista_liczebnosc[i + 1] = a
            i += 1
        j +=1
    return lista, lista_liczebnosc
##########################################
##########################################
def licz_mediana():
    lista = []
    lista_liczebnosc = []
    sortowanie(lista,lista_liczebnosc)
    mediana=0
    liczebnosc = 0
    for i in lista_liczebnosc:
        liczebnosc += i
    if (liczebnosc % 2) == 1: # je�eli liczba element�w jest nieparzysta
        indx = 0
        suma = 0
        for k in lista_liczebnosc: #przechodzimy przez kolejne warto�ci liczebno�ci
            suma += k #dodajemy je do sumy
            if ((liczebnosc+1)/2 <= suma): # je�eli jest ona wi�ksza od po�owy wszystkich warto�ci ( lub r�wna) to oznacza to,�e w tym przedziale liczebno�ci znajduje si� mediana
                mediana = lista[indx] # indx jest r�wny numerowi przedzia�owi liczebno�ci w kt�rym si� znajdujemy. Mediana ma warto�� cechy, kt�rej liczebno�� ma nr r�wny indx
                break
            indx +=1 #je�eli nie, to zwi�kszamy indeks
    else:
        indx = 0
        suma = 0
        x1=0
        x2=0
        for j in lista_liczebnosc:
            suma += j
            if ((liczebnosc)/2 <= suma):
                x1 = lista[indx]
                break
            indx +=1
        indx = 0
        suma = 0
        for m in lista_liczebnosc:
            suma += m
            if ((liczebnosc + 1) / 2 <= suma):
                x2 = lista[indx]
                break
            indx += 1
        mediana = (x1 + x2) / 2


    l.config(text=mediana)
    lwynik.config(text="Mediana to : ")
    return mediana

##########################################
def licz_skosnosc():
    me = licz_mediana()
    srednia = licz_srednia_wazona()
    odchyleniestd = licz_odchylenie_standardowe()

    skosnosc = 3*((srednia - me)/odchyleniestd)

    l.config(text=skosnosc)
    lwynik.config(text="Skośność wynosi : ")
    return skosnosc
##########################################
def licz_wariancja():
    lista = []
    lista_liczebnosc = []
    czytaj(lista)
    czytaj_liczebnosc(lista_liczebnosc)
    srednia = licz_srednia_wazona()
    liczebnosc = 0
    for i in lista_liczebnosc:
        liczebnosc += i
    suma = 0
    i = 0
    while i < len(lista):
        suma += ((lista[i] - srednia)**2)*lista_liczebnosc[i]
        i += 1

    wariancja = (suma/liczebnosc)
    l.config(text = wariancja)
    lwynik.config(text="Wariancja wynosi : ")
    return wariancja
##########################################
def licz_odchylenie_standardowe():
    wariancja = licz_wariancja()
    odchylenie = wariancja**(0.5)
    l.config(text = odchylenie)
    lwynik.config(text="Odchylenie standardowe wynosi : ")
    return odchylenie
##########################################
def licz_odchylenie_przecietne():
    lista = []
    lista_liczebnosc = []
    czytaj(lista)
    czytaj_liczebnosc(lista_liczebnosc)
    srednia = licz_srednia_wazona()
    liczebnosc = 0
    for i in lista_liczebnosc:
        liczebnosc += i
    suma = 0
    i = 0
    while i < len(lista):
        if (lista[i] - srednia) < 0:
            suma += ((lista[i] - srednia)*(-1))*lista_liczebnosc[i]
            i += 1
        else:
            suma += ((lista[i] - srednia)) * lista_liczebnosc[i]
            i += 1

    odchylenie = (suma/liczebnosc)
    l.config(text = odchylenie)
    lwynik.config(text="Odchylenie przeciętne wynosi : ")
    return odchylenie
##########################################
def licz_wspolczynnik_asymetrii():
    lista = []
    lista_liczebnosc = []
    czytaj(lista)
    czytaj_liczebnosc(lista_liczebnosc)
    liczebnosc = 0
    for i in lista_liczebnosc:
        liczebnosc += i

    odchylenie_std =licz_odchylenie_standardowe()
    srednia = licz_srednia_wazona()

    suma = 0
    j = 0
    for i in lista:
        suma += ((i - srednia)**3) * lista_liczebnosc[j]
        j += 1

    wspolczynnik_asymetrii = (suma/liczebnosc) / (odchylenie_std**3)
    l.config(text = wspolczynnik_asymetrii)
    lwynik.config(text="Współczynnik asymetrii wynosi : ")
    return wspolczynnik_asymetrii
##########################################
def licz_typ_asymetrii():
    me = licz_mediana()
    dominanta = licz_dominanta()

    asymetria = me - dominanta
    if asymetria > 0:
        string = "Asymetria prawostronna"
    elif asymetria < 0:
        string = "Asymetria lewostronna"
    else:
        string = "Brak asymetrii"

    l.config(text = string)
    lwynik.config(text="Typ asymetrii to : ")
    return string
##########################################
def licz_kurtoza():
    lista = []
    lista_liczebnosc = []
    czytaj(lista)
    czytaj_liczebnosc(lista_liczebnosc)
    liczebnosc = 0
    for i in lista_liczebnosc:
        liczebnosc += i

    odchylenie_std =licz_odchylenie_standardowe()
    srednia = licz_srednia_wazona()

    suma = 0
    j = 0
    for i in lista:
        suma += ((i - srednia)**4) * lista_liczebnosc[j]
        j += 1

    kurtoza = (suma/liczebnosc) / (odchylenie_std**4) - 3
    l.config(text = kurtoza)
    lwynik.config(text="Kurtoza wynosi : ")
    return kurtoza
###################################
def rysuj_h(): #rysowanie histogramu

    lista = []
    lista_liczebnosc = []
    sortowanie(lista,lista_liczebnosc) #trzeba posortowac dane
    dane =[] #dane to lista z danymi do histogrsmu. zawiera wypisane pojedynczo wszystkie wprowadzone argumenty ( np. 1 o liczebności 2 to 1,1
    j=0
    for i in lista: # ta pętla uzupełnia dane. idziemy po kolei przez listę z danymi
        ilosc=lista_liczebnosc[j] # ilosści przypisujemy wartość liczebności danego argumentu
        j+=1
        while True:
            dane.append(i) #dodajemy do listy argument, aż nie skończy sięjego liczebność ( czyli 3 o liczebności 4 dodamy 4 razy)
            ilosc-=1
            if (ilosc<= 0):
                break
        if j==len(lista)-1:
            break # ze względu na specyfikę histogramu, nie wczytujemy wszystkich wartości ( potrzebujemy przedziałów). brak tej linijki powodował fałszywe wyniki

    zakres=[] # zakres to oś histogramu. kolejne wartości tej listy stanowią kolejne wartości na przedziałce osi OX
    for i in lista:
        zakres.append(i) # dodajemy do niego jedynie wartosci argumentów

    plt.hist(dane,bins=zakres ) #funkcja tworząca histogram. DAne w slupkach pochodzą z listy dane, a podziałka to bins
    plt.show() # "pokazuje" nasz wykres
#########################################
def rysuj_l(): # rysowanie krzywej lorenza
    lista = []
    lista_liczebnosc = []
    czytaj(lista)
    czytaj_liczebnosc(lista_liczebnosc)
    suma_liczebnosc = 0
    for i in lista_liczebnosc:
        suma_liczebnosc += i #potrzebujemy sumy ilości(częstości)...
    dlugosc = len(lista)
    lista_fundusz = []
    j = 0
    while j < dlugosc:
        lista_fundusz.append(lista[j] * lista_liczebnosc[j]) #liczymy WI (Ni*X), czyli wartość cechy
        j += 1

    suma_fundusz = 0
    for k in lista_fundusz:
        suma_fundusz += k #...oraz sumy wartości(X*częstości)

    lista_czestotliwosc_ilosci = []
    j = 0
    while j < dlugosc:
        lista_czestotliwosc_ilosci.append(lista_liczebnosc[j] / suma_liczebnosc)
        j += 1 #liczymy stosunki częstości do sumy

    lista_czestotliwosc_funduszu = []
    j = 0
    while j < dlugosc:
        lista_czestotliwosc_funduszu.append(lista_fundusz[j] / suma_fundusz)
        j += 1 #oraz stosunki częstość * wartość do sumy

    lista_skumulowane_ilosci = []
    j = 0
    kumulacja_ilosci = 0
    lista_skumulowane_ilosci.append(kumulacja_ilosci) #dopisujemy zero aby zacząć od pkt (0,0)
    while j < dlugosc :
        kumulacja_ilosci += lista_czestotliwosc_ilosci[j] #liczymy wartość skumulowaną...
        lista_skumulowane_ilosci.append(kumulacja_ilosci) #...i dopisujemy ją do listy
        j += 1

    lista_skumulowany_fundusz = []
    j = 0

    kumulacja_fundusz = 0
    lista_skumulowany_fundusz.append(kumulacja_fundusz) #dopisujemy zero aby zacząć od pkt (0,0)
    while j < dlugosc :
        kumulacja_fundusz += lista_czestotliwosc_funduszu[j] #analogicznie jak wyżej
        lista_skumulowany_fundusz.append(kumulacja_fundusz)
        j += 1
#lista_skumulowany_fundusz zawiera nasze skumulowane wartości (oś OY), a lista_skumulowane_ilosci - skumulowaną częstość (Oś OX)
    plt.plot(lista_skumulowane_ilosci,lista_skumulowany_fundusz) #rysujemy (plot) wykres (najpierw oś OX, potem OY)
    plt.show() # i wyświetlamy go

####################################
def licz_ginni(): # funkcja liczaca ginniego!!!!
    lista = []
    lista_liczebnosc = []
    sortowanie(lista,lista_liczebnosc)
    #czytaj(lista)
    #czytaj_liczebnosc(lista_liczebnosc)
    suma_liczebnosc = 0
    for i in lista_liczebnosc:
        suma_liczebnosc += i
    dlugosc = len(lista)
    lista_fundusz = []
    j = 0
    while j < dlugosc:
        lista_fundusz.append(lista[j] * lista_liczebnosc[j])
        j += 1

    suma_fundusz = 0
    for k in lista_fundusz:
        suma_fundusz += k

    lista_czestotliwosc_ilosci = []
    j = 0
    while j < dlugosc:
        lista_czestotliwosc_ilosci.append(lista_liczebnosc[j] / suma_liczebnosc)
        j += 1

    lista_czestotliwosc_funduszu = []
    j = 0
    while j < dlugosc:
        lista_czestotliwosc_funduszu.append(lista_fundusz[j] / suma_fundusz)
        j += 1

    lista_skumulowane_ilosci = []
    j = 0
    kumulacja_ilosci = 0
    while j < dlugosc:
        kumulacja_ilosci += lista_czestotliwosc_ilosci[j]
        lista_skumulowane_ilosci.append(kumulacja_ilosci)
        j += 1

    lista_skumulowany_fundusz = []
    j = 0
    kumulacja_fundusz = 0
    while j < dlugosc:
        kumulacja_fundusz += lista_czestotliwosc_funduszu[j]
        lista_skumulowany_fundusz.append(kumulacja_fundusz)
        j += 1
    j = 0
    lista_pola = []
    lista_pola.append(0.5*lista_skumulowane_ilosci[j]*lista_skumulowany_fundusz[j])
    while j < dlugosc - 1:
        lista_pola.append((lista_skumulowany_fundusz[j] + lista_skumulowany_fundusz[j + 1]) * (lista_skumulowane_ilosci[j + 1] - lista_skumulowane_ilosci[j]) * 0.5)
        j+= 1
    tmp_suma = 0
    for m in lista_pola:
        tmp_suma += m
    ginni = (0.5 - tmp_suma)*2

    l.config(text = ginni)
    lwynik.config(text="Współczynnik Ginni'ego wynosi : ")
    return ginni
##########################################
from tkinter import *
main=tkinter.Tk()
main.title("Program do statystyki opisowej i ekonomicznej")
main.configure(background="sky blue")
lpowitalny=tkinter.Label(main, text="Witaj w aplikacji do obliczeń statystycznych", bg = "sky blue",fg = "navy", font=("Helvetica", 24))
l=tkinter.Label(main, text="Tutaj pojawi sie wynik", bg = "sky blue",font=("Helvetica", 16))
lwynik=tkinter.Label(main, text="Nazwa wyniku", font=("Helvetica", 16), bg = "steel blue")
b=tkinter.Button(main, text="Zakończ",command=koniec, bg="deep sky blue",fg = "snow", font=("Helvetica", 15))
e_wartosci=tkinter.Entry(main)
l2 = tkinter.Label(main,text="Po lewej wpisz wartości", bg = "dark turquoise", fg = "snow", font=("Helvetica", 16))
l3 = tkinter.Label(main,text="Po lewej wpisz liczebności", bg = "turquoise", fg= "snow", font=("Helvetica", 16))
e_liczebnosc=tkinter.Entry(main)
###########################
menu = Menu(main)
main.config(menu=menu)
##############################
smenu = Menu(menu)
menu.add_cascade(label="Miary polozenia", menu=smenu)
smenu.add_command(label="Zwykła średnia arytmetyczna", command=licz_srednia)
smenu.add_command(label="Średnia arytmetyczna ważona",command=licz_srednia_wazona)
smenu.add_command(label="Średnia geometryczna",command=licz_sredna_geometryczna)
smenu.add_command(label="Średnia harmoniczna",command=licz_sredna_harmoniczna)
smenu.add_separator()
smenu.add_command(label="Mediana",command=licz_mediana)
smenu.add_command(label="Dominanta",command=licz_dominanta)
######################
wmenu = Menu(menu)
menu.add_cascade(label="Miary rozproszenia", menu=wmenu)
wmenu.add_command(label="Wariancja",command=licz_wariancja)
wmenu.add_command(label="Odchylenie przeciętne",command=licz_odchylenie_przecietne)
wmenu.add_command(label="Odchylenie standardowe",command=licz_odchylenie_standardowe)
#####################
smenu = Menu(menu)
menu.add_cascade(label="Miary skośności", menu=smenu)
smenu.add_command(label="Skosność",command=licz_skosnosc)
smenu.add_command(label="Współczynnik asymetrii",command=licz_wspolczynnik_asymetrii)
smenu.add_command(label="Typ asymetrii",command=licz_typ_asymetrii)
######################
kmenu = Menu(menu)
menu.add_cascade(label="Miary koncentracji", menu=kmenu)
kmenu.add_command(label="Kurtoza",command=licz_kurtoza)
kmenu.add_command(label="Współczynnik Ginni'ego ",command= licz_ginni)
kmenu.add_separator()
kmenu.add_command(label="Krzywa Lorenza",command= rysuj_l)
kmenu.add_command(label="Histogram",command= rysuj_h)
#####################################
lpowitalny.grid(row=0, column =1, columnspan= 4, sticky = W+E)
e_wartosci.grid(row =1, column =1,columnspan =2, sticky=W+E)
l2.grid(row = 1,column = 3, sticky=W+E)
e_liczebnosc.grid(row = 2, column = 1,columnspan =2, sticky=W+E)
l3.grid(row = 2, column=3, sticky = W+E)
lwynik.grid(row=3, column=1, columnspan=2, sticky=W+E)
l.grid(row = 3, column =3)
b.grid(row = 1, column = 4,columnspan=2,rowspan=2, sticky =N+S+W+ E)
main.mainloop()
##########################################
#objaśnienie składni
#label - wyświetla dane, entry - służy do wprowadzania, menu - to nasze kasakdowe menu, command - jaką funkcję coś uruchamia,
#columnspan/rowspan - ile zajmuje kolumn/wierszy, sticky - do których krawędzi ma przylegać, bg - kolor widgetu, fg - kolor czcionki
