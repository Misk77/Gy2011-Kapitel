# Övning 1
# Program som räknar ut produkten av två tal
print()
print ('Ange dina två tal: ')
tal1 = int(input('Ange tal 1: '))
tal2 = int(input('Ange tal 1: '))
prod = tal1+tal2
print('Produkten av Tal {} och tal {} blir: {}' .format ( tal1, tal2, prod))
print("Produkten av "+str(tal1)+" och "+str(tal2)+" blir: "+str(prod))


# Övning 2
# Räkna ut arean i en triangel
print()
print('Ange basen och höjden i triangeln, så beräknar vi arean')
basen = float(input('Ange basen: '))
höjden = float(input('Ange höjden: '))
Area = float(basen * höjden) / 2
print('Arean på triangeln är {}'.format(Area))


# Övning 3
# Räkna ut 15 % rabatt
print()
pris = float(input('Ange produktens summa: '))
rabatt = float(pris * 0.15)
nypris = pris - rabatt
print('Efter 15 % rabbat blir priset: {}'.format(nypris))


# Övning 4
# förbättrad rabattprogram
# print()
pris = float(input('Ange produktens summa: '))
rabatt = float(input('Ange rabatten: '))
medRabatt = pris * rabatt
rabatteratPris = pris - medRabatt
print('Du skrev in pris: {0} och rabatten: {1}. Ditt rabatterande pris blir: {2} '.format(pris, rabatt, rabatteratPris))

# Övning 5
# Räkna
print()
volym = float(input('Ange tankad volym: '))
pris = float(input('Ange liter priset: '))
betala = volym * pris

print()

print("""\n
+-------------------------------+
|           KVITTO              |
|                               |
|    Tankad volym {0} liter    | 
|    Pris per liter {1} kronor |
|    Betala kronor {2}        |
|                               |
|    Tack för besöket och       |
|    välkommen åter!            |                            |
+-------------------------------+""".format(volym, pris, betala))
print()

# Övning 6
# Formaterad uppställlgnin/uträkning
print()
tal1 = 27
tal2 = 8
tal3 = 213
summan = tal1 + tal2 + tal3
print()
print("""\n
\t{0}
\t {1}
+  {2}
======
   {3}""".format(tal1, tal2, tal3, summan))
print()

# Övning 7
# Formaterad uppställlgnin/uträkning MED 2 decimaler
print()
tal1 = 123.45
tal2 = 6.7
tal3 = 89.01
summan = (tal1 + tal2 + tal3)
print("""\n
 {0:.2f}
   {1:.2f}
+ {2:.2f}
=======
 {3:.2f}""".format(tal1, tal2, tal3, summan, ))
print()

# Övning 8
# BMI uträkning
print()
lenght = int(input('Skriv in din längd i centimeter: '))
vikt = int(input('skriv in din vikt i kg: '))
lenght2 = lenght / 100
bmi = vikt / (lenght2 * lenght2)
print('Ditt BMI är: {0:.1f}'.format(bmi))
