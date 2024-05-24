numero2=(input("Ingrese un numero\n"))
if ((numero2.isdigit())):
    numero=int(numero2)
    while ((numero > 0)):
        palabra= input("Ingrese una palabra\n")
        numero2= len(palabra)
        acum=1
        print(numero2)
        for i in range (1, numero2+1):
            acum=acum *i
        print(acum)
        if (acum % 2== 0):
            print ("El factorial es par")
        else:
            print ("El factorial es impar") 
        numero=int(input("Ingrese un numero\n"))
    