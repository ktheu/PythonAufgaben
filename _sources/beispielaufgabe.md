# Beispielaufgabe

Die Aufgabenstellung ist im Kommentar beschrieben, gefolgt von der erwarteten Ausgabe oder
von Beispieldialogen. 

```
'''
Aufgabe 8:
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
Über das `copy`-Icon in der rechten oberen Ecke der Zelle kann die Aufgabenstellung in den eigenen Programmeditor kopiert werden. Die Kommentarzeile `#your code` wird durch den eigenen Programmcode ersetzt. Der Leser kontrolliert selbst
die Korrektheit des Programms. Eine Lösung für die obige Aufgabe könnte sein:

```
'''
Aufgabe 8:
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
s = input('Bitte einen String eingeben: ')
zaehl = 0
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        zaehl+=1
print(zaehl)
```
 
