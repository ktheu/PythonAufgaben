# Aufgaben 5

<!-- #2 #dict -->
```
'''
Aufgabe 5.1:
Gegeben ist ein text und ein dictionary m, das einigen Zeichen Zahlen zuordnet.
Schreibe ein Programm das zählt, wieviele Zeichen von s im dictionary m als key vorkommen.

Erwartete Ausgabe
38
'''
text = 'In der Innenwelt des Computers werden Nullen und Einsen \
verschoben, verrechnet und gespeichert'
m = {'l': 1, 'e': 3, 'd': 2, 'p': 2, 'c': 1, 'h': 3, 'b': 3, 'j': 2, 'u': 1}
# your code

```

<!-- #2 #dict -->
```
'''
Aufgabe 5.2
Gegeben ist eine Liste von Zahlen. Wenn eine Zahl durch 2 teilbar ist, 
erhalten wir 1 Punkt, ist sie durch 3 oder 5 teilbar, erhalten wir 2 Punkte,
ist sie durch 7 teilbar, erhalten wir 5 Punkte, ist sie durch 11 teilbar, 
erhalten wir 7 Punkte. 
Ermittle die Punkte für die Liste a = [2,3,5,1,11]

Pseudocode:

Erstelle ein dictionary m, das der Teilungszahl seine Punktezahl zuordnet:
2->1, 3->2, 5->2, 7->5, 11->7

setze punkte auf 0
für jedes x in a:
     wenn x key in m:
         erhöhe punkte um den Wert, der x in m zugeordnet ist
gib punkte aus

Erwartete Ausgabe:
12
'''
# your code
```

<!-- #2 #loop #str #ord #modulo #index  -->
```
'''
Aufgabe 5.3
s = 'In der Innenwelt des Computers werden Nullen und Einsen verschoben'

Wir beginnen beim ersten Zeichen des Strings s. Wir ermitteln den ASCII-Wert
modulo 7 des Zeichens und erhöhen diesen Wert um 1. Soviele Schritte rücken wir
im String vor. Wir zählen, wie häufig wir das machen müssen, bis wir außerhalb
des Strings landen.

Pseudocode: 

Setze pos auf 0
Setze zaehl auf 0
Solange pos kleiner als die Länge von s:
    Erhöhe zaehl um 1
    Setze c auf das Zeichen von s an der Stelle pos.
    Setze w auf den ASCII-Wert von c modulo 7
    Erhöhe pos um w + 1
Gib zaehl aus


Erwartete Ausgabe: 15
'''
# your code
```

<!-- #2 #einlesen -->
```
%%writefile input.txt
42
-12
10
```
```
'''
Aufgabe 5.4
Lies die Zahlen aus obigem input.txt in die Variablen a, b, c ein und gib 
diese Variablen und ihre Summe aus.

Erwartete Ausgabe:
42 -12 10 40
'''
# your code
```

<!-- #2 #einlesen -->
```
%%writefile input.txt
3
10
20
40
```
```
'''
Aufgabe 5.5
Die erste Zahl gibt an, wieviele Zahlen noch folgen. Lies die Zahlen aus obigem
input.txt in eine Liste a ein und gib diese aus.

Erwartete Ausgabe:
[10, 20, 40]
'''
# your code
```

<!-- #2 #einlesen -->
```
%%writefile input.txt
3
Hallo 
```
```
'''
Aufgabe 5.6
Lies die Zahl n und den String s aus obigem input.txt ein und gib s n-mal aus.

Erwartete Ausgabe:
Hallo
Hallo
Hallo
'''
# your code
```

<!-- #2 #einlesen -->

```
%%writefile input.txt
3 10 8 4 -3 14 42 -9
```
```
'''
Aufgabe 5.7
Alle Zahlen stehen in einer Zeile. Lies die Zahlen aus obigem input.txt in 
eine Liste ein und gib diese aus.

Erwartete Ausgabe:
[3, 10, 8, 4, -3, 14, 42, -9]
'''
# your code
```

<!-- #2 #einlesen -->
```
%%writefile input.txt
In der Innenwelt des Computers werden Nullen und Einsen verschoben, verrechnet
und gespeichert. Dass dies keinerlei Einschränkung bedeutet, wissen
wir bereits: Töne, Bilder und beliebige andere Informationen lassen sich durch
0–1-Muster codieren.
```
```
'''
Aufgabe 5.8
Lies den Text aus dem obigen input.txt in eine Variable data ein.
Ersetze jeden Zeilenvorschub durch ein Leerzeichen und ersetze alle Umlaute:
ä zu ae, ö zu oe, ü zu ue. Gib dann data aus.


Erwartete Ausgabe:

In der Innenwelt des Computers werden Nullen und Einsen verschoben, verrechnet und gespeichert. Dass dies keinerlei Einschraenkung bedeutet, wissen wir bereits: Toene, Bilder und beliebige andere Informationen lassen sich durch 0–1-Muster codieren.
'''
# your code
```




<!-- #2 #einlesen -->

```
%%writefile input.txt
Die ist ein Text. Da haben wir die Umlaute ä ö und ü. Wir testen auch das ß.
Satzzeichen wie ?,!; sollen nicht übernommen werden.
```

```
'''
Aufgabe 5.9
Lies den Text aus dem obigen input.txt in eine Variable data0 ein.
Wandle alles in Kleinbuchstaben um. In die Variable data sollen nur die Buchstaben 
(auch Umlaute und ß) aus data0 übernommen werden, keine Leerzeichen,
Zeilenvorschübe oder Satzzeichen. Gib data aus.

Erwartete Ausgabe:
dieisteintextdahabenwirdieumlauteäöundüwirtestenauchdasßsatzzeichenwiesollennichtübernommenwerden
'''
```

```
'''
Aufgabe 5.10
Erstelle ein dictionary m, das jedem kleinen Buchstaben seine Stelle im Alphabet zuordnet.
a -> 1, b -> 2, ... z -> 26. 
Erweitere das dict um folgende Einträge: ä -> 27, ö -> 28, ü -> 29, ß -> 30.

Teste ein paar Werte:
>>> m['c']
3
>>> m['o']
15
>>> m['ö']
28
'''
```

<!-- #2 #Jwinf -->
```
'''
Aufgabe 5.11
Lies eine positive ganze Zahl ein und gib alle Möglichkeiten aus, wie diese
Zahl durch eine Multiplikation zweier ganzer positiver Zahlen erreicht werden kann.

Beispieldialoge:

Bitte eine Zahl eingeben: 49
49 = 1 * 49
49 = 7 * 7
49 = 49 * 1

Bitte eine Zahl eingeben: 30
30 = 1 * 30
30 = 2 * 15
30 = 3 * 10
30 = 5 * 6
30 = 6 * 5
30 = 10 * 3
30 = 15 * 2
30 = 30 * 1
''' 
```

<!-- #2 #Jwinf -->

```
'''
Aufgabe 5.12 (siehe auch 5.11)
Schreibe eine Funktion func, der eine positive ganze Zahl übergeben wird 
und die eine Liste zurückgibt mit allen Möglichkeiten, wie diese
Zahl durch eine Multiplikation zweier ganzer positiver Zahlen erreicht kann.

>>> func(49)
[[1, 49], [7, 7], [49, 1]]

>>> func(30)
[[1, 30], [2, 15], [3, 10], [5, 6], [6, 5], [10, 3], [15, 2], [30, 1]]
''' 
```

<!-- #2 #Jwinf -->
```
'''
Aufgabe 5.13
Schreibe eine Funktion func, der eine Liste a mit Zahlen übergeben wird und die
die Zahl zurückgibt, die zu 1 den kleinsten Abstand hat.

>>> func([2.4, 1.3, 0.9, -1])
0.9

>>> func([6.1, 11, -1.2, 23, 19.6])
-1.2
''' 
```


