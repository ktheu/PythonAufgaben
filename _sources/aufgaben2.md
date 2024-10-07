
# Aufgaben 2

<!-- #1 #str   -->
```
'''
Aufgabe 2.1:
Lies einen String ein und gib seine Länge aus.

Beispieldialoge:

Bitte einen String eingeben: Hallo
5

Bitte einen String eingeben: Habicht
7

'''
# your code
```


<!-- #1 #str #index  -->
```
'''
Aufgabe 2.2:
Lies einen String s ein.
Gib einen String aus, der aus dem ersten und letzten Zeichen von s besteht.

Beispieldialoge:

Bitte einen String eingeben: Hallo
Ho

Bitte einen String eingeben: Habicht
Ht
'''
# your code
```

<!-- #1 #str #count  -->
```
''' 
Aufgabe 2.3:
Das Programm zählt die Anzahl der kleinen Buchstaben 'a' in einem String.

Beispieldialoge:

Bitte einen String eingeben:  Hallo
Anzahl kleine a: 1

Bitte einen String eingeben:  Tralala
Anzahl kleine a: 3

Bitte einen String eingeben:  HURRA
Anzahl kleine a: 0

'''
# your code
```

<!-- #1 #str #index #len  -->

```
'''
Aufgabe 2.4:
Lies eine String s ein. Wenn s länger als 10 Zeichen ist und mit dem Zeichen 'A' beginnt,
gib 'YES' aus, sonst 'NO'.

Beispieldialoge:

Bitte einen String eingeben: Afdasfasfdsaf
YES

Bitte einen String eingeben: Adam
NO

Bitte einen String eingeben: dfdfdfdfdfdfdfdfdf
NO
'''
# your code
```

<!-- #1 #str #len #index  -->

```
'''
Aufgabe 2.5:
Lies einen String s ein. Wenn die Länge von s größer als 2 ist und das letzte Zeichen 'a' oder 'o' ist
gib 'YES' aus, sonst 'NO'

Beispieldialoge:

Bitte einen String eingeben: Hallo
YES

Bitte einen String eingeben: Halli
NO

Bitte einen String eingeben: oo
NO
'''
# your code
```

<!-- #1 #list   -->

```
'''
Aufgabe 2.6:
Erstelle eine leere Liste a und gib sie mit print aus

Erwartete Ausgabe:
[]

'''
# your code
```

<!-- #1 #str   -->

```
'''
Aufgabe 2.7:
Erstelle eine Liste a mit den Zahlen 1,2,3 und gib sie aus.

Erwartete Ausgabe:
[1,2,3]
'''
# your code
```


<!-- #1 #str   -->

```
'''
Aufgabe 2.8:
Erstelle eine Liste a mit den Zeichen 'a', 'b', 'c' und gib sie aus.

Erwartete Ausgabe:
['a', 'b', 'c']
'''
# your code
```

<!-- #1 #str   -->

```
'''
Aufgabe 2.9:
Ändere die dritte Zahl in der gegebenen Liste zu einer 33 und gib die Liste aus.

Erwartete Ausgabe:
[5, 9, 33, 14, 5, 26]
'''
a = [5, 9, 2, 14, 5, 26]
# your code
```


<!-- #1 #str   -->

```
'''
Aufgabe 2.10:
Lies eine positive Zahl k ein und erstelle eine Liste mit Werten von 1 bis k und gib sie aus
Nutze dazu eine for-Schleife und append.

Beispieldialoge:

Bitte eine Zahl eingeben: 7
[1, 2, 3, 4, 5, 6, 7]

Bitte eine Zahl eingeben: 1
[1]
'''
# your code
```


<!-- #1 #str   -->

```
'''
Aufgabe 2.11:
Lies in einer Zeile zwei Zahlen x und k ein. Erzeuge eine Liste in der
x k-mal vorkommt.

Beispieldialoge:

Bitte zwei Zahlen eingeben: 3 7
[3, 3, 3, 3, 3, 3, 3]

Bitte zwei Zahlen eingeben: 7 3
[7, 7, 7]
'''
# your code
```

<!-- #1 #str   -->

```
'''
Aufgabe 2.12:
Lies eine Folge von drei Zahlen ein. Gib dann eine Liste aus mit jeweils 
dem Doppelten der eingegebenen Zahlen.

Beispieldialoge:

Bitte drei Zahlen eingeben: 1 2 3
[2, 4, 6]

Bitte drei Zahlen eingeben: 0 5 6  
[0, 10, 12]

'''
# your code
```


<!-- #1 #dict   -->

```
'''
Aufgabe 2.13:
Erstelle ein dict m1, dass den Ländern 'England', 'Frankreich' und 'Italien' ihre Hauptstädte zuordnet.

>>> m1['England']
'London'

>>> m1['Frankreich']
'Paris'

>>> m1['Italien']
'Rom'
'''
# your code
```

<!-- #1 #str   -->

```
'''
Aufgabe 2.14:
Erstelle ein dict m2, dass den Städten London, Paris und Rom ihre Länder zuordnet

>>> m2['London']
'England'

>>> m2['Paris']
'Frankreich'

>>> m2['Rom']
'Italien'
'''
# your code

```

<!-- #1 #str   -->

```
'''
Aufgabe 2.15:
Erstelle ein dict m3, dass jeder Zahl in Zeile 1, die Zahl zuordnet, die unter ihr steht.

Zeile1:   3  10  12  101  25  17
         19   4   1   -4  99  17

>>> m3[3]
19

>>> m3[101]
-4
'''
# your code
```

<!-- #1 #str   -->

```
'''
Aufgabe 2.16:

Lies zwei Strings ein, lies dann zwei Zahlen ein. 
Erstelle ein dict m, das den Strings jeweils die Zahlen zuordnet 
und gibt dann das dict aus.

Beispieldialog:

Bitte zwei Strings eingeben: Hallo Welt
Bitte zwei Zahlen eingeben: 5 12
{'Hallo': 5, 'Welt': 12}
'''
# your code
```


<!-- #1 #func   -->

```
'''    
Aufgabe 2.17

Erstelle eine Funktion func1, der eine Zahl k übergeben wird und 
die das Quadrat dieser Zahl zurückgibt.

>>> func1(4)
16

>>> func1(5)
25
'''
# your code
```


<!-- #1 #str   -->

```
'''    
Aufgabe 2.18

Erstelle eine Funktion func2, der zwei Zahlen übergeben werden und  
die das Doppelte der Summe der beiden Zahlen zurückgibt.

>>> func2(4, 3)
14

>>> func2(1, 5)
12
'''
# your code
```

<!-- #1 #func   -->

```
'''    
# Aufgabe 2.19

Erstelle eine Funktion func3, der zwei Zahlen übergeben werden und  
die das Dreifache der kleineren Zahl zurückgibt.

>>> func3(1, 5)
3

>>> func2(17, 4)
12
'''
# your code
```

<!-- #1 #func #list   -->

```
'''
Aufgabe 4
Erstelle eine Funktion func4, der eine Liste übergeben wird und die
True zurückgibt, wenn die Anzahl der Listenelemente gerade ist, sonst False.

>>> func4([1,2,3])
False

>>> func4(['a','b'])
True  
'''
# your code
```

<!-- #1 #func #list   -->

```
'''
Aufgabe 2.20
Erstelle eine Funktion func5, der eine nicht-leere Liste mit Zahlen übergeben wird und die 
die Summe der ersten und letzten Zahl der Liste zurückgibt.

>>> func5([1,2,3])
4

>>> func5([7,10,24,19,12,3])
10
'''
# your code

```


 