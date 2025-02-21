# Python-Schnipsel


## Jupyter Notebooks

```
Strg + Enter - Ausführen der Zelle und Sprung zur nächsten Zelle  
Shift + Enter - Ausführen der Zelle ohne Sprung in die nächste Zelle 
Neue Zelle: Click auf + oberhalb des Hauptarbeitsbereichs  
Zelle löschen: Mit dem Cursor neben die Zelle klicken, dann zweimal Taste D  
In einer Code Zelle: Tab-rechts - Kontexthilfe
```

```
Tab-rechts - Kontexthilfe 
s = 'Hallo'
s. +  Tab-rechts  - alle möglichen Methoden      
```

```
# %%-Anweisungen (magic commands) immer am Beginn einer Zelle
%%writefile input.txt  - schreibt Inhalt der Zelle in Datei
%%time             - gibt Laufzeit für Zelle aus
```

## Kommentare

```
# Einzeiliger Kommentar
'''
Mehrzeiliger
Kommentar
'''
```

## Variablen und Zuweisungen
Die wichtigsten einfachen Datentypen sind: int, float, str, bool.

```
k = 5        # Zuweisungen eines int (ganze Zahl)
x = 2.6      # Zuweisung eines float (Dezimalzahl)
s = 'Hallo'  # Zuweisung eines Strings mit einfachen
s1 = "Welt"  #    oder doppelten Hochkommata
b = True     # True/False sind boolesche Werte (Wahrheitswerte)
y = None     # Die Variable wird definiert, bekommt aber keinen Wert zugewiesen
```

Kurzformen für spezielle Zuweisungen
```
x += 1       # statt x = x + 1
x *= 2       # statt x = x * 2
             # analog - / // %
```

```
x = None            # es wurde noch kein Wert zugewiesen
x = float('inf')    # Unendlich 
x = -float('inf')   # Minus Unendlich
```

```
x = 0b1001   # eine Zahl in binärer Schreibweise zuweisen
x = 0o17     # eine Zahl in oktaler Schreibweise zuweisen
x = 0xe2     # eine Zahl in hexadezimaler Schreibeweise zuweisen
```
 

## Ausgabe

```
print(a)                 # einen Wert ausgeben
print(a, b)              # zwei Werte ausgeben mit Leerzeichen getrennt
print(a, end=' ')        # nach der Ausgabe keine neue Zeile, sondern ein Leerzeichen 
print(a, b, sep='-')     # zwischen den Werten kein Leerzeichen, sondern ein '-'.
``` 

## f-Strings
```
x = 40
print(f'Der Wert von x ist {x}.')
print(f'{x = }')           # x = 40
print(f'{x} zum Quadrat ist {x**2}.')

print(f'{a/11=:.2f}')          # a/11=3.64
print(f'{a} binär = {a:0b}')   # 40 binär = 101000
print(f'{a} binär = {a:08b}')  # 40 binär = 00101000
```

## Eingabe
```
s = input('Bitte einen String eingeben')                
x = int(input('Bitte eine Zahl eingeben'))

a, b = input('Bitte zwei Zahlen eingeben').split()    # Eingaben mit Leerzeichen getrennt
a = int(a)                                            # String in int umwandeln
b = int(b)
```

## Bedingungen
```
# Vergleichsoperatoren: <  <=  >  >=  ==  !=
if a > 10:
    print('A')
elif a > 5:
    print('B')
else:
    print('C')
```

```
if a % 2 == 0:       # ist a gerade Zahl?
    ...
if a % b == 0:       # ist b ein Teiler von a?
    ...
```

```
if x is None:        # wurde x noch kein Wert zugewiesen?
    ...
if x is not None:    # wurde x schon ein Wert zugewiesen?
    ...
```

## Arithmetische Operatoren
```
+ - * /      # plus, minus, mal, geteilt
//           # ganzzahlige Division
%            # Modulo (Rest bei der ganzzahligen Division)
**           # Exponentiation
```

## Boolesche Operatoren
```
a and b      # True wenn a und b True sind
a or  b      # True wenn mindestens einer von beiden True ist
not a        # dreht den Wahrheitswert um
```

## Eingebaute Funktionen
```
min(a), max(a), sum(a)    # Minimum, Maximum, Summe einer Liste a mit Zahlen
abs(x)                    # Betrag einer Zahl x
round(5.76543, 2)         # Auf 2 Stellen hinterm Komma runden
ord(c)                    # ASCII bzw. Unicode-Codepoint eines Zeichens c
chr(x)                    # Zeichen einer ASCII-Zahl x oder Unicode-Codepoints
list(s)                   # Wandelt einen Objekt (falls möglich) in eine Liste um
int(x), float(x)          # Wandelt ein Objekt (falls möglich) in ein int/float um
```


## Schleifen  

```
# for-Schleifen mit range
for i in range(5):        # 0,1,2,3,4
    ...
for i in range(2,5):      # 2,3,4
    ...
for i in range(1,10,2):   # 1,3,5,7,9
    ...
for i in range(5,-1,-1):  # 5,4,3,2,1,0
    ...

```

```
# Schleifen mit Strings
s = 'Habicht'
for i in range(len(s)):             # durch die Zeichen eines Strings mit dem Index laufen.
    print(s[i])

s = 'Habicht'
for c in s:                         # durch die Zeichen eines Strings laufen
    print(c)
```

```
# Schleifen mit Listen
a = [4,2,10,6]
for i in range(len(a)):             # durch die Elemente der Liste mit dem Index laufen.
    print(a[i])

for x in a:                         # lesend! durch die Elemente der Liste laufen
    print(x)                        # die Elemente können mit dieser Schleife nicht verändert werden.
```
```
# while-Schleife
while x < 10:             # solange x kleiner 10 ...
    ....
 
while s:                  # solange String s nicht leer ist ...
    ....

while a:                  # solange in der Liste a noch Elemente sind ...
    ....

while True:               # oder: while 1, Endlosschleife
    ....
```

```
# nur in Schleifen:
break                     # verlässt Schleife und macht dahinter weiter
continue                  # startet nächsten Schleifendurchgang

```


## Strings

```
s = ''                # Der leere String mit Länge 0
s1 = 'oha'
s2 = 'du'
s = s1 + ' ' + s2     # Verketten von Strings 

# Indexing
s = 'Habicht'         
len(s)       #  7, die Länge des Strings 
s[0]         # 'H'
s[3]         # 'i'
s[len(s)-1]  # 't'
s[-1]        # 't'
s[-2]        # 'h'

# Slicing (Teilstrings bilden)
s = 'Habicht'
s[:3]        # 'Hab'
s[3:]        # 'icht'
s[2:5]       # 'bic'
s[::2]       # jedes zweite Zeichen: 'Hbct'
s[::-1]      # den gesamten String rückwärts:  'thcibaH'
```

```
s.lower(), s.upper()   # alles in Klein-, Großbuchstaben
s.replace(s1,s2)       # alle Teilstrings s1 in s2 umwandeln
s.strip()          # entfernt vorne und hinten Leerzeichen und Seitenvorschub
s.strip('?.!;')    # entfernt vorne und hinten die angegebenen Zeichen
s.islower(), s.isupper() # besteht s aus Klein-, Großbuchstaben ?
s.isalpha(), s.isdigit() # besteht s aus Buchstaben, Ziffern ?
s.isalnum()        # besteht s nur aus Buchstaben und Ziffern?
s.startswith(s1), s.endswith(s1) # beginnnt, endet s mit s1 ?
s.count(s1)        # Anzahl Vorkommen von s1 in s
s.index(s1)        # Index erstes Vorkommen s1 in s, Fehler wenn nicht da
s.find(s1)         # Index erstes Vorkommen s1 in s, -1 wenn nicht da
s.find(s1,i,j)     # Suche Vorkommen im Intervall [i,j)
s1 = s.ljust(20)   # s1 beginnt links mit s, hat Länge 20, ggf. Leerzeichen rechts.
s1 = s.rjust(20)   # analog rechts
```

```
a = s.split()      # Trenner sind Leerzeichen (auch mehrere) und Seitenvorschub
a = s.split(' ')   # Trenner ist einzelnes Leerzeichen 
a = s.split(s1)    # Trenner ist s1 
a = list(s)        # Liste aus den einzelnen Zeichen von s
```
 
```
# Hilfe
help(str)         # alle Methoden des Strings
help(str.count)   # Hilfe zur Methode count
```
[W3C](https://www.w3schools.com/python/python_strings.asp)

## Listen

```
a = []        # leere Liste
a = [1,2,3]   # eine Liste mit 3 Elementen
len(a)        # Länge der Liste
a[0]          # 1    Indexing wie bei Strings
a[len(a)-1]   # 3    letztes Element
a[-1]         # 3    letztes Element       
a.append(4)   # [1,2,3,4]   ein Element hinten an die Liste einfügen.
```

```
# Unpacking 
a = [1, 2, 3]
x, y, z = a   # Die einzelnen Werte werden den Variablen zugewiesen
```

```
# Slicing
a[1:3]        # Teilliste von Index 1 bis ausschließlich Index 3  
a[3:]         # Teilliste ab Index 3 bis Ende 
a[:3]         # die ersten 3 Elementen: von Beginn bis Index 3 (ausschließlich) 
a[-3:]        # die letzten 3 Elemente
a[::2]        # jedes 2. Element
```

```
x in a, x not in a   # Element x in Liste a vorhanden?
k = a.count(x) # Anzahl Vorkommen von x in a 
i = a.index(x) # Index des ersten Vorkommens von x, Fehler wenn nicht vorhanden
x = a.pop()   # Entfernt und gibt zurück letztes Element von a 
x = a.pop(3)  # Entfernt und gibt zurück Element mit Index 3
del(a[3])     # Entfernt Element mit Index 3 aus a  
a.remove(x)   # Entfernt erstes Vorkommen von x in a, Fehler wenn nicht vorhanden
a.insert(i, x) # Fügt x bei Index i ein, Rest rückt nach hinten.
a.reverse()   # Reihenfolge umdrehen
a.sort()      # Liste sortieren (falls möglich)
a.sort(reverse=True)   # absteigend sortieren
b = a.copy()  # (flache) Kopie der Liste erstellen
a.clear()     # Liste leeren
```
 
```
help(list)          #  Methoden der Liste
help(list.insert)   #  Hilfe zur Listenmethode insert
```
[W3C](https://www.w3schools.com/python/python_lists.asp)

## Tuples

Wie Listen, aber nicht veränderbar
```
t = ()              # leeres Tupel
t = (3,)            # Tupel mit einem Element (Komma unterscheidet von geklammerter 3)
t = (4,2,9)         # Tupel mit drei Elementen
```
Indexing, slicing, Schleifen, x in t, unpacking, len, min, max etc. wie bei Listen 
```
a = [1,2,3]
t = tuple(a)        # Liste in Tupel umwandeln
a = list(t)         # Tupel in Liste umwandeln
```

## Dictionaries
```
m = {}        # leeres dict
m = dict()    # leeres dict
m = {'a':1, 'b':2} 
m['c'] = 3    # neuer Wert oder update im dictionary
k in m        # k Schlüssel in m ?
k not in m    # k kein Schlüssel in m?
len(m)        # Anzahl Einträge in m
del m['b']    # löscht Eintrag mit Schlüssel 'b'  
v = m.pop(k)  # löscht Eintrag mit Schlüssel k und gibt value v zurück
m.update(m1)  # aktualisiert Einträge und fügt ggf neue hinzu 

# durch ein dict laufen und die key-value Paare ausgeben
for k in m:            # durch alle keys von m laufen
    ...                # dasselbe wie: for k in m.keys():   

for v in m.values():   # durch alle values von m laufen
    ...

for k, v in m.items(): # durch alle key,value-Paare laufen
    ...
```

## Sets
```
s = set()           # ein leeres Set
s = {1, 2, 3}       # set mit 3 Elementen
len(s)              # Länge von s
x in s              # x im set?
x not in s          # x nicht im set?
s <= t, s < t       # s Teilmenge, echte Teilmenge von t?
s | t, s & t        # Vereinigung, Schnittmenge
s - t, s ^ t        # Differenz, Entweder-Oder
```

## Funktionen
```
def zeichen(s, k=3):
    '''
    s: String
    k: int
    returns: s k-mal hintereinander
    '''
    return s * k

```

Doctest
```
def func(x):
    '''
    >>> func(5)
    6
    '''
    return x + 1

import doctest
doctest.run_docstring_examples(func,globals(),optionflags=doctest.NORMALIZE_WHITESPACE) 
```

## Zufall
```
import random
random.random()       # float Zufallszahl x, 0 <= x < 1
random.uniform(0,10)  # float Zufallszahl x, 0 <= x <= 10
random.randint(0,20)  # int Zufallszahl k, 0 <= k <= 20
random.randrange(2, 101, 2)   # eine gerade Zahl zwischen 2 und 100   

random.seed(x)        # x irgendeine Zahl, setzt den random-seed für reproduzierbare Ergebnisse
random.choice(a)      # ein zufälliges Element der Liste a
random.shuffle(a)     # mischt die Elemente der Liste a
random.sample(a, 2)   # 2 zufällige Elemente aus Liste a
```

## Das Unendliche
Das Unendliche nutzen wir, wenn wir eine maximal große oder maximal kleine Zahl benötigen. Es gelten nicht alle Rechengesetze, aber es funktionieren die Vergleiche mit endlichen Zahlen und einige Eigenschaften, die man vom Unendlichen erwarten würde.
```
inf = float('inf')   
x < inf        # True, für jede Zahl x ungleich inf
-inf < x       # True für jede Zahl x ungleich -inf

# weitere Eigenschaften von inf
inf + 10000 == inf   # True
inf - 10000 == inf   # True
inf + inf == inf     # True
inf - inf            # nan  = not a number 
```

## Einlesen von Dateien

```
f = open('input.txt')
zeile = f.readline().strip()   # eine Zeile als String einlesen
x = int(f.readline())          # eine Zahl einlesen
f.close()
```

```
f = open('input.txt')
a = [int(x) for x in f.readline().split()]   # eine Zeile mit Zahlen in eine Liste einlesen
f.close()
```

```
f = open('input.txt', encoding='utf-8')   # meist die richtige Wahl für Umlaute etc.
text = f.read()                # den gesamten Text mit Zeilenvorschüben einlesen
f.close()
text = text.replace('\n',' ')  # Zeilenvorschub durch Leerzeichen ersetzen
```

## Fortsetzungszeichen
Wenn eine Programmzeile zu lang wird, kann man sie mit dem Fortsetzungzeichen `\`
auf mehrere Zeilen verteilen.

```
s = 'Hal\
lo Welt'

a = [1,2,3, \
     5,6]

if 3 < 5 or 7 < 10 \
or 8 < 10:
    print('ja')
```