# Kapitel 4 - Villkor, IF-satser


# Övning 1
# Räkna ut medevärdet på 3 prov

print()
prov1 = int(input('Ange poäng på prov 1: '))
prov2 = int(input('Ange poäng på prov 2: '))
prov3 = int(input('Ange poäng på prov 3: '))

mv = (prov1 + prov2 + prov3) / 3
print()
if mv > 90:
    print('Ditt medevärde blev: {0}'.format(mv))
    print('Bra jobbat!')
else:
    print('Ditt medevärde blev: {0}'.format(mv))
    print('Du får öva lite mera')

# Övning 2
# Räknaut bmi sedan skriver ut status ang bmi
print()
lenght = int(input('Ange din längd: '))
weight = int(input('Ange din vikt: '))
lenght /= 100
bmi = weight / (lenght * lenght)
print()
if bmi < 18.5:
    print('Ditt bmi är: {:.2f}'.format(bmi))
    print('Du har undervikt')
elif bmi >= 18.5 or bmi < 25:
    print('Ditt bmi är: {:.2f}'.format(bmi))
    print('Du har normalvikt')
elif bmi >= 25 or bmi < 30:
    print('Ditt bmi är: {}'.format(bmi))
    print('Du har övervikt')
elif bmi > 30:
    print('Ditt bmi är: {}'.format(bmi))
    print('Du har tyvärr fetma')
else:
    print('Något blev fel')

# Övning 3
# Rvillkor som är sant om antingen eller stämmer
print()

a = 5
b = 7
c = 12

if a < b or b < c:
    print('a är mindre än b ELLER b är mindre än c')

    # Övning 4
    # fråga efter bensinpris sedan utskrift med tex för olika värden
print()

bensinPris = int(input('Ange bensinpriset: '))

if bensinPris < 10:
    print('Bensin priset du skrev in var: {}'.format(bensinPris))
    print('Det var billigt')
elif bensinPris >= 10 and bensinPris <= 15:
    print('Bensin priset du skrev in var: {}'.format(bensinPris))
    print('Tanka full tank')
elif bensinPris >= 15 and bensinPris <= 20:
    print('Bensin priset du skrev in var: {}'.format(bensinPris))
    print('Tanka 10 liter')
else:
    print('Bensin priset du skrev in var: {}'.format(bensinPris))
    print('Nu säljer jag bilen och cyklar istället')

    # Övning 5
    # årtal, skottår eller inte
    # Anävnd modulus year delat i 4 och kolla så ingen rest blir kvar
    print()
year = int(input('Ange årtal: '))

if year % 4 == 0:
    print('Du skrev in årtalet: {}'.format(year))
    print('Det är skottår')
elif year == 1700 or year == 1800 or year == 1900:
    print('Du skrev in årtalet: {}'.format(year))
    print('Årtalet är 1800 eller 1900 och var ej skottår')
else:
    print('Du skrev in årtalet: {}'.format(year))
    print('Det var inte skottår')

    # Övning 6
    # betalning via faktura koll
    # ålder,inkomst ev kreditanmälningar gå igenom  villkor för att bli beviljad

    print()
age = int(input('Ange din ålder: '))
annualIncome = int(input('ange din årsinkomst'))

if age >= 18 and annualIncome > 12000:
    print('fakturabetalning beviljad.')
else:
    print('Tyvärr kan vi ej bevilja fakturabetalning.')


    # Övning 7
    # betalning via faktura koll
    # ålder,inkomst ev kreditanmälningar direkt ge svar vid något villkor som ej godkänt
    print()

age = int(input('Ange ålder: '))
if age < 18:
    print('Avslag')
elif age >= 18:
    annualIncome = int(input('ange din årsinkomst: '))
if annualIncome < 12000:
    print('Avslag')
elif annualIncome >= 12000:
    anmärkning = (input('Har du betalningsanmärkning (1 = Ja / 2 = N?): '))
    if anmärkning == 'j':
        print('Avslag')
    elif anmärkning == 'n':
        print('Beviljad fakturabetalning')
