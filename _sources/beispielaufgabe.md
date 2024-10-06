# Beispielaufgabe

Die Aufgabenstellung ist im Kommentar beschrieben, gefolgt von der erwarteten Ausgabe oder
von Beispieldialogen. 

```
'''
Aufgabe 1.12:
Lies eine ganze Zahl ein und gib aus, ob sie gerade oder ungerade ist

Beispieldialoge:

Bitte eine ganze Zahl eingeben: 3
ungerade

Bitte eine ganze Zahl eingeben: 8
gerade
''' 
# your code 

```
Über das `copy`-Icon in der rechten oberen Ecke der Zelle kann die Aufgabenstellung in den eigenen Programmeditor kopiert werden. Die Kommentarzeile `#your code` wird durch den eigenen Programmcode ersetzt. Der Leser kontrolliert selbst
die Korrektheit des Programms. Eine Lösung für die obige Aufgabe könnte sein:

```
'''
Aufgabe 1.12:
Lies eine ganze Zahl ein und gib aus, ob sie gerade oder ungerade ist

Beispieldialoge:

Bitte eine ganze Zahl eingeben: 3
ungerade

Bitte eine ganze Zahl eingeben: 8
gerade
''' 
x = int(input('Bitte eine ganze Zahl eingeben:'))
if x % 2 == 0:
    print('gerade')
else:
    print('ungerade')
```
 
