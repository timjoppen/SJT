a = float(input("Geef coëfficiënt a in ax²+bx+c=0."))
b = float(input("Geef coëfficiënt b in ax²+bx+c=0."))
c = float(input("Geef coëfficiënt c in ax²+bx+c=0."))
if a == 0:
    print("Dit is geen tweedegraadsvergelijking.")
else:
    D = int(b**2-4*a*c)
    print("De discriminant is " + str(D) + ".")
    if D < 0:
        print("De vergelijking heeft geen oplossingen.")
    elif D == 0:
        x = -b/(2*a)
        print("De vergelijking heeft 1 oplossing: " + str(x) + ".")
    else:
        x1 = (-b-D**(1/2))/(2*a)
        x2 = (-b+D**(1/2))/(2*a)
        print("De vergelijking heeft 2 oplossingen: " + str(x1) + " en " + str(x2) + ".")
    if a < 0:
        print("De grafiek is een bergparabool.")
    else:
        print("De grafiek is een dalparabool.")
