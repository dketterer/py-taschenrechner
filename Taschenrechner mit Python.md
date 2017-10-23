# Taschenrechner mit Python

## Entwicklungsumgebung

## Hallo Welt

```
print("Hallo Welt")
```

## Taschenrechner auf der Console

**Programmablauf**

1. Zahl 1 eingeben
2. Rechenoperation
3. Zahl 2 eingeben
4. Zahlen von Text in Computerzahlen
5. Ergebnis ausrechnen
6. Ergebnis ausgeben

**Vorbereitungen**

*Text einlesen*

`variable = input("Jetzt Text eingeben\n")`

*if - else*

Entscheiden welche Rechenoperation wir durchführen wollen

```
if operation == '+':
    ergebnis = zahl1 + zahl2
elif operation == '-':
    ergebnis = zahl1 - zahl2
else:
    ergebnis = "Operation nicht gefunden."
```

**Merke: Einrückung**
> in Python sind die Einrückungen wichtig. Die Einrückungen ersetzen die geschweiften Klammern die wir aus Java oder anderen Programmiersprachen kennen.

**Merke: Zeilenende**
> in Python brauchen wir am Zeilenende kein Semikolon

**Merke: Klammern**
> in Python brauchen wir um die Bedingungen beim if keine Klammern

*Datentypen*

Für unser Pythonprogramm macht es einen Unterschied, ob eine Variable ein Text (String) oder eine Zahl (int) oder eine Kommazahl (float) ist.  
Wir müssen dem Pythonprogramm aber nicht sagen was für eine Variable das sein soll, dass entscheidet Python selber.

Wenn wir mit unserem Variablen rechnen wollen, dann müssen die aber Zahlen sein. Entweder int oder float.

```
string_zahl = "5"
string_zahl2 = "7"
ergebnis = string_zahl + string_zahl2
# ergebnis ist jetzt 57

zahl1 = int(string_zahl)
zahl2 = int(string_zahl2)
ergebnis = zahl1 + zahl2
# ergebnis ist jetzt 12
```
