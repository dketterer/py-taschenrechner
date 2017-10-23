#1. Zahl 1 eingeben
zahl1 = int(input("Gib Zahl 1 ein\n"))

#2. Rechenoperation
operation = input("Gib die Operation ein (+ - * /)\n")

#3. Zahl 2 eingeben
zahl2 = int(input("Gib Zahl 2 ein\n"))

#4. Ergebnis ausrechnen
ergebnis = 0
if operation == '+':
    ergebnis = zahl1 + zahl2
elif operation == '-':
    ergebnis = zahl1 -zahl2
elif operation == '*':
    ergebnis = zahl1 * zahl2
elif operation == '/':
    ergebnis = zahl1 / zahl2
else:
    print("Falsche Operation!")
    exit(1)

#5. Ergebnis ausgeben
print("Ergebnis ist " + str(ergebnis))
