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

## Variablen
Die wichtigsten einfachen Datentypen sind: int, float, str, bool.

```
k = 5        # Zuweisungen eines int (ganze Zahl)
x = 2.6      # Zuweisung eines float (Dezimalzahl)
s = 'Hallo'  # Zuweisung eines Strings mit einfachen
s1 = "Welt"  #    oder doppelten Hochkommata
```

## Ausgabe

```
print(a)                 # einen Wert ausgeben
print(a, b)              # zwei Werte ausgeben mit Leerzeichen getrennt
print(a, end=' ')        # nach der Ausgabe keine neue Zeile, sondern ein Leerzeichen 
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

## Boolesche Operatoren
```
# Boolesche Operatoren
a and b      # True wenn a und b True sind
a or  b      # True wenn mindestens einer von beiden True ist
not a        # dreht den Wahrheitswert um
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
# while-Schleife
while a < 10:             # solange a kleiner 10 ...
    ....
```

## Strings

```
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

```
# Schleifen mit Strings
s = 'Habicht'
for i in range(len(s)):             # durch die Zeichen eines Strings mit dem Index laufen.
    print(s[i])

s = 'Habicht'
for c in s:                         # durch die Zeichen eines Strings laufen
    print(c)

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
m = {'A':1, 'B':2}  

# durch ein dict laufen und die key-value Paare ausgeben
for k in m:
    print(k, m[k])
```

## Funktionen
```
def add(x, y):
    return x + y

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