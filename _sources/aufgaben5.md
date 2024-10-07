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
'''
Aufgabe 5.4
Lies die Zahlen aus input.txt in die Variablen a, b, c ein und gib 
diese Variablen und ihre Summe aus.

Erwartete Ausgabe:
42 -12 10 40
'''
```

```
%%writefile input.txt
42
-12
10
```
---
<!-- #2 #einlesen -->

```
'''
Aufgabe 5.5
Die erste Zahl gibt an, wieviele Zahlen noch folgen. Lies die Zahlen aus 
input.txt in eine Liste a ein und gib diese aus.

Erwartete Ausgabe:
[10, 20, 40]
'''
```

```
%%writefile input.txt
3
10
20
40
```
---- 
<!-- #2 #einlesen -->

```
'''
Aufgabe 5.6
Lies die Zahl n und den String s aus input.txt ein und gib s n-mal aus.

Erwartete Ausgabe:
Hallo
Hallo
Hallo
'''
# your code
```

```
%%writefile input.txt
3
Hallo 
```

---
<!-- #2 #einlesen -->

```
'''
Aufgabe 5.7
Alle Zahlen stehen in einer Zeile. Lies die Zahlen aus input.txt in 
eine Liste ein und gib diese aus.

Erwartete Ausgabe:
[3, 10, 8, 4, -3, 14, 42, -9]
'''
# your code
```
```
%%writefile input.txt
3 10 8 4 -3 14 42 -9
```
----
<!-- #2 #einlesen -->

```
'''
Aufgabe 5.8
Lies den Text aus input.txt in eine Variable data ein.
Ersetze jeden Zeilenvorschub durch ein Leerzeichen und ersetze alle Umlaute:
ä zu ae, ö zu oe, ü zu ue. Gib dann data aus.


Erwartete Ausgabe:

In der Innenwelt des Computers werden Nullen und Einsen verschoben, verrechnet und gespeichert. Dass dies keinerlei Einschraenkung bedeutet, wissen wir bereits: Toene, Bilder und beliebige andere Informationen lassen sich durch 0–1-Muster codieren.
'''
# your code
```

```
%%writefile input.txt
In der Innenwelt des Computers werden Nullen und Einsen verschoben, verrechnet
und gespeichert. Dass dies keinerlei Einschränkung bedeutet, wissen
wir bereits: Töne, Bilder und beliebige andere Informationen lassen sich durch
0–1-Muster codieren.
```


<!-- #2 #einlesen -->

```
'''
Aufgabe 5.10
Lies den Text aus dem letzten input.txt in eine Variable data ein.
Übernimm nur die Vokale aus dem Text gib den String, der nur aus diesen Vokalen besteht aus.

Erwartete Ausgabe:
IeIeeeoueeeueuEieeoeeeeueeieaieeieeiEiueeueieieeieieueieieaeeIoaioeaeiuueoiee
'''
# your code
```



