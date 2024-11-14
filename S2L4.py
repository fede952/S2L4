def perimetroQ():
    numero=int(input("Inserisci valore lato: "))
    print(f"\nIl perimetro di un quadrato lato {numero} è:{numero*4}\n")

def circonferenza():
    numero=int(input("Inserisci valore raggio: "))
    print(f"\nLa circonferenza di un cerchio R {numero} è:{2*numero*3.14:.3f}\n")

def perimetroR():
    base=int(input("Inserisci valore base: "))
    altezza=int(input("Inserisci valore altezza: "))
    print(f"\nIl perimetro di un rettangolo base{base} e {altezza} è: {(base*2) + (altezza*2)} \n")
    
onoff=True
while(onoff):
    scelta=input("Cosa vuoi calcolare?\n1)Perimetro quadrato\n2)Circonferenza cerchio\n3)Perimetro rettangolo\n0)esci\n")
    if scelta=="1":
        perimetroQ()
    elif scelta=="2":
        circonferenza()
    elif scelta=="3":
        perimetroR()
    elif scelta=="0":
        onoff=False
    else :print("\n**Inserisci il valore corretto**\n")

