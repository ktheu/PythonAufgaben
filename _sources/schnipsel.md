# Python-Schnipsel


## Jupyter Notebooks

```
Strg + Enter - Ausführen der Zelle und Sprung zur nächsten Zelle  
Shift + Enter - Ausführen der Zelle ohne Sprung in die nächste Zelle 
Neue Zelle: Click auf + oberhalb des Hauptarbeitsbereichs  
Zelle löschen: Mit dem Cursor neben die Zelle klicken, dann zweimal Taste D  
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
```

Kurzformen für spezielle Zuweisungen
```
x += 1       # statt x = x + 1
x *= 2       # statt x = x * 2
             # analog - / // %
```

## Ausgabe

```
print(a)                 # einen Wert ausgeben
print(a, b)              # zwei Werte ausgeben mit Leerzeichen getrennt
print(a, end=' ')        # nach der Ausgabe keine neue Zeile, sondern ein Leerzeichen 
``` 

```
# Ausgabe mit f-Strings
a = 42
print(f'Der Wert von a ist {a}.')
print(f'{a} zum Quadrat ist {a**2}.')
x = 3.1415

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
s[1]         # 'i'
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

## Dictionaries
```
m = {}        # leeres dict
m = dict()    # leeres dict
m = {'a':1, 'b':2} 
m['c'] = 3    # neuer Wert oder update im dictionary
k in m        # k Schlüssel in m ?
k not in m    # k kein Schlüssel in m?
len(m)        # Anzahl Einträge in m
del m['b']    # den Eintrag mit Schlüssel 'b' löschen

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
def add(x, y):
    return x + y

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
f = open('input.txt')
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