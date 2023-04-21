modulus1 = float(input("Geef de modulus van het eerste complex getal:"))
argument1 = float(input("Geef het argument van het eerste complex getal:"))
modulus2 = float(input("Geef de modulus van het tweede complex getal:"))
argument2 = float(input("Geef het argument van het tweede complex getal:"))
modulus = modulus1/modulus2
print("De modulus is " + str(modulus) + ".")
argument = argument1 - argument2
print("Het argument is " + str(argument) + ".")
print("Het quotiënt is " + str(modulus) + " . (cos " + str(argument) + " - i sin " + str(argument) + ").")
if argument == -90 or argument == 90:
    print("Het complexe getal ligt op de Y-as.")
    print("Dit is een zuiver imaginair getal.")
elif argument == 0 or argument == -180 or argument == 180:
    print("Het getal ligt op de X-as.")
    print("Dit is een reëel getal.")
elif argument < -90:
    print("Het complexe getal ligt in het 3de kwadrant.")
    print("Dit is een imaginair getal.")
elif argument < 0:
    print("Het complexe getal ligt in het 4de kwadrant.")
    print("Dit is een imaginair getal.")
elif argument < 90:
    print("Het complexe getal ligt in het 1ste kwadrant.")
    print("Dit is een imaginair getal.")
else:
    print("Het complexe getal ligt in het 2de kwadrant.")
    print("Dit is een imaginair getal.")
