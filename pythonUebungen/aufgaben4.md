# Aufgaben 4

<!-- #2 #str #list #func -->
```
'''
Aufgabe 4.1:
Schreibe eine Funktion func1, der ein String s und ein Index k übergeben wird und die
eine Liste mit den beiden Teilstrings vor und nach der Stelle k zurückgibt.

>>> func1('Habicht', 3)
['Hab', 'cht']

>>> func1('Hallo', 4)
['Hall', '']
'''
#your code
```

<!-- #2 #list #func #durchlauf  -->
```
'''
Aufgabe 4.2:
Schreibe eine Funktion func2, der eine Liste a mit ints und ein int k übergeben wird und die
'YES' zurück, wenn in a mindestens k gerade Zahlen sind.

>>> func2([1,2,3,4],2)
'YES'

>>> func2([1,2,3,4,5,6],4)
'NO'
'''
#your code
```


<!-- #2 #func #str #index   -->
```
'''
Aufgabe 4.3:
Schreibe eine Funktion func3, der ein String s übergeben wird und die den längsten Teilstring von hinten in
s zurückgibt, der kein '.' enthält

>>> func3('abc.de')
'de'

>>> func3('abc.de.com')
'com'

>>> func3('abc')
'abc'
'''
# your code
```

<!-- #2 #func #list #durchlauf #str  -->
```
'''
Aufgabe 4.4:
Schreibe eine Funktion func4, der eine Liste a mit Strings und eine String s übergeben wird 
und die 'YES' returned, wenn s als Teilstring in einer der Strings in Liste a vorkommt, sonst 'NO'.

>>> func4(['abc', 'abd', 'abe'], 'bd')
'YES'

>>> func4(['abc', 'abd', 'abe'], 'bf')
'NO'

'''
# your code
```

<!-- #1 #func #list #str  -->
```
'''
Aufgabe 4.5:
Schreibe eine Funktion func5, der eine Liste mit Strings übergeben wird und die eine Liste mit diesen
Strings in umgekehrter Reihenfolge zurückgibt.

>>> func10(['ab','cd','efg'])
['efg','cd','ab']

'''
#your code
```

<!-- #2 #str #index  -->
```
'''
Aufgabe 4.6:
Schreibe eine Funktion func6, der ein String s und ein int k übergeben wird und 
die einen String zurückgibt, der aus s dadurch entsteht, dass das erste 
Auftreten von 'o' in s k-mal wiederholt wird.

>>> func6('Long',4)
'Loooong'

>>> func6('Long',0)
'Lng'

>> func6('Hollow',3)
'Hooollow'
'''
# your code
```

<!-- #2 #func #str #index #durchlauf  -->
```
'''
Aufgabe 4.7:
Schreibe eine Funktion func7, der eine String s und zwei Zeichen c1 und c2 übergeben werden
und die das Zeichen c1 oder c2 zurückgibt, das als erstes in s vorkommt. Wenn keines der Zeichen vorkommt,
soll False zurückgegeben werden.

>>> func7('Hallo','a', 'o')
'a'

>>> func7('sssdbbbcooocdcd','c', 'd')
'd'

>>> func7('abc','e','g')
False
'''
# your code
```

<!-- #1 #str #count -->
```
'''
Aufgabe 4.8:
Schreibe eine Funktion func8, der ein String s übergeben wird der nur aus '0' und '1' besteht und 
die 'YES' zurückgibt wenn 1 häufiger in s vorkommt als 0, sonst 'NO'.

>>> func8('10011')
'YES'

>>> func8('01101010110000')
'NO'

>>> func8('0')
'NO'
'''
# your code
```

<!-- #1 #str #range #list #func  -->
```
'''
Aufgabe 4.9:
Schreibe eine Funktion func9, der ein String s und eine Zahl k übergeben wird und die
eine Liste zurückgibt, in der s 1..k mal wiederholt wird.


>>> func9('a',5)
['a', 'aa', 'aaa', 'aaaa', 'aaaaa']

>>> func9('ja',4)
['ja', 'jaja', 'jajaja', 'jajajaja']

'''
# your code
```

<!-- #1 #func #list #min #max  -->
```
'''
Aufgabe 4.10:
Schreibe eine Funktion func10, der eine Liste a mit Zahlen übergeben wird und die die Differenz
zwischen dem größten und kleinsten Element zurückgibt.

>>> func1([3,7,9])
6

>>> func1([-10,7,4,17])
27

'''
# your code
```

<!-- #1 #func #list #max  -->
```
Aufgabe 4.11:
Schreibe eine Funktion func11, der eine Liste a mit Zahlen übergeben wird und eine Zahl k
und die 'YES' returned, wenn k größer als alle Zahlen in a ist, sonst 'NO'.

>>> func11([3,4,5],5)
'NO'

>>> func11([3,4,5],6)
'YES'
'''
# your code
```

<!-- #1 #list #avg #sum  -->
```
'''
Aufgabe 4.12:
Schreibe eine Funktion func12, der eine Liste a mit Zahlen übergeben wird und die
den Durchschnittswert der Zahlen in a zurückgibt.
(Durchschnitt = Summe der Zahlen / Anzahl der Zahlen)

>>> func4([1,2,3])
2.0

>>> func4([3,4,7,8,9])
6.2
'''
# your code
```

<!-- #2 #str #list #durchlauf -->
```
'''
Aufgabe 4.13:
Schreibe eine Funktion func13, der eine Liste a mit Zahlen übergeben wird und
die eine Liste zurückgibt, in der alle geraden Zahlen von a in umgedrehter Reihenfolge
vorkommen.
 

>>> func13([1,2,3,4,5,6])
[6, 4, 2]

>>> func13([3,3,4,1,2,7,8])
[8, 2, 4]

>>> func13([1,3,9])
[]

'''
# your code
```

<!-- #1 #func #list #sort  -->
```
'''
Aufgabe 4.14:
Schreibe eine Funktion func14, der eine Liste a von Zahlen übergeben wird und die eine Liste
zurückgibt mit allen Zahlen von a aufwärts sortiert, dann abwärts sortiert.
 

>>> func14([4,2,9])
[2, 4, 9, 9, 4, 2]

>>> func14([9,1,5,0])
[0, 1, 5, 9, 9, 5, 1, 0]

>>> func14([1,1])
[1, 1, 1, 1]

'''
# your code
```

<!-- #1 #func #comprehension  -->
```
'''
Aufgabe 4.15
Schreibe eine Funktion func15, der eine Liste a mit Zahlen übergeben wird, und die eine Liste zurückgibt, 
in der alle Zahlen aus a verdoppelt sind.
Nutze eine List-Comprehension.

>> func15( [1,2,3])
[2, 4, 6]
'''

# your code 
```

<!-- #1 #list #comprehension  -->
```
'''
Aufgabe 4.16:
Schreibe eine Funktion func16, der eine positive Zahl k übergeben wird die eine
Liste mit allen Quadraten der Zahlen von 1 bis k zurückgibt.
Nutze eine List-Comprehension.

>>> func16(2)
[1, 4]

>>> func16(7)
[1, 4, 9, 16, 25, 36, 49]

>>> func16(0)
[]
'''
# your code
```

<!-- #1 #str #ord  -->
```
'''
Aufgabe 4.17:
Schreibe eine Funktion func17, der ein String s übergeben wird und die eine Liste mit
den ASCII-Nummern der Zeichen von s zurückgibt.

>>> func17('Hallo')
[72, 97, 108, 108, 111]

>>> func17('Habicht')
[72, 97, 98, 105, 99, 104, 116]

'''
# your code
```

<!-- #1 #str #chr -->
```
'''
Aufgabe 4.18:
Schreibe eine Funktion func18, der eine Liste mit ASCII-Zahlen übergeben wird und
die den dazugehörigen String zurückgibt.

>>> func18([77, 111, 122, 97, 114, 116])
'Mozart'

>>> func18([65, 98, 98, 97])
'Abba'

'''
# your code
```

<!-- #2 #func #ord #str  -->
```
'''
Aufgabe 4.19:
Schreibe eine Funktion func19, der ein String mit kleinen Buchstaben des englischen Alphabets 
und ein Zeichen c übergeben werden und die die Anzahl Zeichen in s zurückgibt, die alphabetisch vor c
vorkommen.

>>> func19('hallo','l')
2

>>> func19('habicht','i')
5

>>> func19('habicht','a')
0

'''
# your code
```

<!-- #2 #str #ord #chr -->
```
'''
Aufgabe 4.20:
Schreibe eine Funktion func20, der ein kleiner Buchstabe des englischen Alphabets übergeben wird
und die den nächsten Buchstaben zurückgibt. Falls c ein 'z' ist, soll 'a' ausgegeben werden.

>>> func20('a')
'b'

>>> func20('s')
't'

>>> func20('z')
'a'
'''
 
# your code
```

<!-- #2 #dict #func  -->
```
'''
Aufgabe 4.21:
Schreibe eine Funktion func21, der eine positive ganze Zahl k übergeben wird und die
eine dictionary zurückgibt, dass jeder Zahl von 1..k 'YES' zuordnet, falls die Zahl gerade, sonst 'NO'.

>>> func21(5)
{1: 'NO', 2: 'YES', 3: 'NO', 4: 'YES', 5: 'NO'}

>>> func21(1)
{1: 'NO'}

>>> func21(0)
{}
'''
# your code
```

<!-- #1 #func #list #dict  -->
```
'''
Aufgabe 4.22:
Schreibe eine Funktion func22, der eine Liste a mit Strings übergeben wird und die ein dictionary 
zurückgibt, das jedem String in a seine Länge zuordnet.

>>> func22(['Hallo', 'Habicht'])
{'Hallo': 5, 'Habicht': 7}   

>>> func22(['a', '', 'aaa', 'aaaaaa'])
{'a': 1, '': 0, 'aaa': 3, 'aaaaaa': 6}

'''

# your code
```

<!-- #1 #str #dict  -->
```
'''
Aufgabe 4.23:
Schreibe eine Funktion func23, der ein String s übergeben wird und die ein dictionary zurückgibt,
das jedem Zeichen c in s die Häufigkeit seines Vorkommens in s zuordnet.

>>> func23('Tralala')
{'T': 1, 'r': 1, 'a': 3, 'l': 2}

>>> func23('abbcccdddd')
{'a': 1, 'b': 2, 'c': 3, 'd': 4}
'''

# your code
```




