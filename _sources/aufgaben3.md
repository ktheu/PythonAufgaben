
# Aufgaben 3

<!-- #1 #str  -->
```
'''
Aufgabe 3.1
Setze s1 auf 'Rom'
Setze s2 auf 'Paris'
Setze a auf das 5-mal hintereinandergepappte s1
Setze b auf das 3-mal hintereinandergepappte s2
Pappe a dann b dann a zusammen und weise das Ergebnis der Variablen c zu
Gib c aus

Erwartete Ausgabe:
RomRomRomRomRomParisParisParisRomRomRomRomRom

'''
# your code
```


<!-- #1 #modulo   -->
```
'''
Aufgabe 3.2:
Lies eine Zahl x ein
Falls x durch 2 teilbar: Gib aus '2 ist Teiler'
Falls x durch 3 teilbar: Gib aus '3 ist Teiler'
Falls x durch 5 teilbar: Gib aus '5 ist Teiler'
Falls x durch 7 teilbar: Gib aus '7 ist Teiler'
Falls x durch 11 teilbar: Gib aus '11 ist Teiler'

Beispieldialog:

Bitte eine Zahl eingeben: 3432
2 ist Teiler
3 ist Teiler
11 ist Teiler

Bitte eine Zahl eingeben: 480480
2 ist Teiler
3 ist Teiler
5 ist Teiler
7 ist Teiler
11 ist Teiler
''' 

# your code
```


<!-- #1 #modulo #schleife -->
```
'''
Aufgabe 3.3
Das Programm liest eine Zahl ein und gibt 
dann die Teiler zurück. Beispieldialoge:
 
Bitte eine Zahl eingeben: 12
1 ist Teiler von 12
2 ist Teiler von 12
3 ist Teiler von 12
4 ist Teiler von 12
6 ist Teiler von 12
12 ist Teiler von 12

Bitte eine Zahl eingeben: 23
1 ist Teiler von 23
23 ist Teiler von 23
'''
# your code  
```


<!-- #2 #str #schleife  -->
```
'''
Aufgabe 3.4
Lies eine ganze Zahl k > 2 ein.
Gib ein k x k Quadrat mit '#'-Rändern aus.

Beispieldialoge:

Bitte eine ganze Zahl größer als 2 eingeben: 3
###
# #
###

Bitte eine Zahl eingeben: 5
#####
#   #
#   #
#   #
#####

Bitte eine ganze Zahl größer als 2 eingeben: 6
######
#    #
#    #
#    #
#    #
######
'''
# your code
```


<!-- #2 #range   -->
```
'''
Aufgabe 3.5
Lies in einer Zeile zwei ganze Zahlen a, b ein und ermittle die Summe aller
Zahlen k zwischen a und b, also a <= k <= b. Beispieldialoge:

Bitte zwei ganze Zahlen a, b eingeben mit a <= b: 0 3
Die Summe aller ganzen Zahlen zwischen 0 und 3 ist 6

Bitte zwei ganze Zahlen a, b eingeben mit a <= b: 1 100
Die Summe aller ganzen Zahlen zwischen 1 und 100 ist 5050

Bitte zwei ganze Zahlen a, b eingeben mit a <= b: -5 5
Die Summe aller ganzen Zahlen zwischen -5 und 5 ist 0

'''
# your code
```


<!-- #2 #range  -->
```
''' 
Aufgabe 3.6
Lies eine ganze Zahl k > 0 ein und gib die 
Multiplikationstabelle aus. Beispieldialoge:

Bitte eine positive ganze Zahl eingeben: 17
1 mal 17 ist 17
2 mal 17 ist 34
3 mal 17 ist 51
4 mal 17 ist 68
5 mal 17 ist 85
6 mal 17 ist 102
7 mal 17 ist 119
8 mal 17 ist 136
9 mal 17 ist 153
10 mal 17 ist 170

Bitte eine positive ganze Zahl eingeben: 23
1 mal 23 ist 23
2 mal 23 ist 46
3 mal 23 ist 69
4 mal 23 ist 92
5 mal 23 ist 115
6 mal 23 ist 138
7 mal 23 ist 161
8 mal 23 ist 184
9 mal 23 ist 207
10 mal 23 ist 230
''' 
# your code
```


<!-- #1 #str #count  -->
```
'''
Aufgabe 3.7:
Lies einen String s ein. Dann lies ein einzelnes Zeichen c ein. 
Gib aus, wieviel mal das Zeichen c im String s vorkommt.
 
Beispieldialoge:

Bitte einen String eingeben: Hallo
Bitte ein Zeichen eingeben: a
1

Bitte einen String eingeben: Tralala
Bitte ein Zeichen eingeben: a
3
'''
# your code
```

<!-- #1 #str   -->
```
'''
Aufgabe 3.8:
Lies einen String s ein.
Gib die Anzahl der Zeichen aus, bei denen das nachfolgende Zeichen das Gleiche ist.
 
Beispieldialoge:

Bitte einen String eingeben: abcdefg
0

Bitte einen String eingeben: aaabb
3

Bitte einen String eingeben: abbadff
2
'''
# your code
```

<!-- #1 #str   -->
```
'''
Aufgabe 3.9:
Lies eine String s ein. 
Gib nacheinander Zeichen mit ihren Nachfolgern aus (Teilstrings der Länge 2)

Beispieldialoge:

Bitte einen String eingeben: Habicht
Ha ab bi ic ch ht 

Bitte einen String eingeben: Informatik
In nf fo or rm ma at ti ik 

'''
# your code 
```

<!-- #1 #str   -->
```
'''
Aufgabe 3.10:
Lies eine String s ein. 
Gib nacheinander die vorne beginnenden Teilstrings aus.

Beispieldialoge:

Bitte einen String eingeben: Habicht
H
Ha
Hab
Habi
Habic
Habich
Habicht

'''
# your code 
```


<!-- #1 #str   -->
```
'''
Aufgabe 3.11:
Lies eine String s ein. 
Gib nacheinander die hinten endenden Teilstrings aus.

Beispieldialoge:

Bitte einen String eingeben: Habicht
Habicht
abicht
bicht
icht
cht
ht
t

'''
# your code 
```

<!-- #1 #str #contains  -->
```
'''
Aufgabe 3.12:
Lies eine String s ein und einen weiteren String s0 ein. 
Wenn s0 in s vorkommt, gib 'YES' aus, ansonsten 'NO'.

Nutze eine for-Schleife und slicing, keine eingebauten Funktionen.

Beispieldialoge:

Bitte einen String eingeben: Habicht
Bitte einen weiteren String eingeben: ich
YES

Bitte einen String eingeben: Hallo
Bitte einen weiteren String eingeben: lol
NO

Bitte einen String eingeben: Hallo
Bitte einen weiteren String eingeben: llo
YES

'''
# your code
```

<!-- #1 #str   -->
```
'''
Aufgabe 3.13:
Lies eine Folge von mindestend 2 Zahlen ein.
Erzeuge dann eine Liste mit den Summen zweier aufeinanderfolgender Zahlen.
Wenn die Liste weniger als 2 Elemente enthält, gib aus: 'zu kurz'

Beispieldialoge:

Bitte eine Folge von Zahlen eingeben: 1 2 3
[3, 5]

Bitte eine Folge von Zahlen eingeben: 3 3 3 4 4 4 
[6, 6, 7, 8, 8]

Bitte eine Folge von Zahlen eingeben: 7
zu kurz

'''
# your code
```

<!-- #1 #list #slice   -->
```
'''
Aufgabe 3.14:
Lies eine Folge von Zahlen ein
Gib alle Teillisten aus, die mit 3 beginnen und bis zum Ende gehen.

Beispieldialoge:

Bitte eine Folge von Zahlen eingeben: 3 4 5 3 1 2 3 3 
[3, 4, 5, 3, 1, 2, 3, 3]
[3, 1, 2, 3, 3]
[3, 3]
[3]

'''
# your code
```

<!-- #1 #str #list #split  -->
```
'''
Aufgabe 3.15:
Lies einen String s ein
Lies ein Trennzeichen c ein.
Gib die Liste a aus, die die Bestandteile von s enthält, wenn man c als Trennzeichen nutzt

Beispieldialoge:

Bitte einen String eingeben: Habicht
Bitte ein Trennzeichen eingeben: c
['Habi', 'ht']

Bitte einen String eingeben: hola-hula-hup
Bitte ein Trennzeichen eingeben: -
['hola', 'hula', 'hup']

'''
#your code
```


<!-- #1 #str #replace   -->
```
'''
Aufgabe 3.16:
Lies einen Satz mit mehreren Worten ein, die durch Leerzeichen getrennt sind
Gib den Satz aus mit einem '+' zwischen den Worten.

Beispieldialoge:

Bitte einen Satz eingeben: Heute ist ein schöner Tag
Heute+ist+ein+schöner+Tag

Bitte einen Satz eingeben: Da ist nicht viel.
Da+ist+nicht+viel.

'''
#your code
```



<!-- #1 #str #replace  -->
```
'''
Aufgabe 3.17:
Lies einen Satz mit mehreren Worten ein, die durch Leerzeichen getrennt sind
Gib den Satz ohne Leerzeichen aus. 

Beispieldialoge:

Bitte einen Satz eingeben: Heute ist ein schöner Tag
HeuteisteinschönerTag

Bitte einen Satz eingeben: Da ist nicht viel.
Daistnichtviel.

'''
#your code
```



<!-- #1 #str #list  -->
```
'''
Aufgabe 3.18:
Gib in einer Zeile ein ganze Zahl ein.
Gib die Liste mit den Ziffern aus.

Beispieldialoge:

Bitte eine Zahl eingeben: 123456789
[1, 2, 3, 4, 5, 6, 7, 8, 9]

Bitte eine Zahl eingeben: 2313450023
[2, 3, 1, 3, 4, 5, 0, 0, 2, 3]

'''
#your code
```


<!-- #2 #str #list  -->
```
'''
Aufgabe 19:
Gib in einer Zeile eine positive ganze Zahl ein.
Gib die Quersumme der Zahl aus.

Beispieldialoge:

Bitte eine Zahl eingeben: 124
7

Bitte eine Zahl eingeben: 1234567
28

'''
#your code
```


<!-- #2 #str #schleife  -->
```
'''
Aufgabe 3.20:
Lies positive ganze Zahl n ein.
Gib die Summe aller ihrer geraden Ziffern aus.
Nutze eine for-Schleife ohne Index.

Beispieldialoge:

Bitte eine Zahl eingeben: 243
6

Bitte eine Zahl eingeben: 135775
0

Bitte eine Zahl eingeben: 12345678
20
'''
#your code
```

 






