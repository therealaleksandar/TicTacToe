#from IPython.display import clear_output

def prikazi_tablu(tabla,dostupno):
    print('\n'*100)
    #clear_output()
    print()
    print("TABLA","\t","\t","\t","DOSTUPNA POLJA")
    print(tabla[7],"|",tabla[8],"|",tabla[9],"\t","\t",dostupno[7],"|",dostupno[8],"|",dostupno[9],)
    print("---------","\t","\t","---------")
    print(tabla[4],"|",tabla[5],"|",tabla[6],"\t","\t",dostupno[4],"|",dostupno[5],"|",dostupno[6])
    print("---------","\t","\t","---------")
    print(tabla[1],"|",tabla[2],"|",tabla[3],"\t","\t",dostupno[1],"|",dostupno[2],"|",dostupno[3])
    print()

def biraj():
    print()
    print("Dobrodosli u Tic Tac Toe!")
    print()
    print()
    prikazi_tablu(tabla1,dostupno1)
    unos=input("Igrac 1: Da li zelite da igrate sa X ili O: ").upper()
    if unos=="X":
        xo=("Igrac 1","X"),("Igrac 2","O")
    else:
        xo=("Igrac 1","O"),("Igrac 2","X")
    return xo

def provera(tabla,a):
    for i in range (1,4):
        if tabla[i]==tabla[i+3]==tabla[i+6]==a:
            return True
    for i in range (1,8,3):
        if tabla[i]==tabla[i+1]==tabla[i+2]==a:
            return True
    if tabla[1]==tabla[5]==tabla[9]==a or tabla[7]==tabla[5]==tabla[3]==a:
        return True
    return False

def unosi(tabla,dostupno):
    uneti=[]
    xo=biraj()
    igraj=True
    while igraj:
        for j,i in xo:
            pozicija=0
            while pozicija in uneti or pozicija not in range(1,10):
                try:
                    pozicija=int(input(f"{j}: unesite broj gde zelite da unesete {i}: "))
                except ValueError:
                    print("Pogresan unos!")
            tabla[pozicija]=i
            uneti.append(pozicija)
            dostupno[pozicija]=" "
            prikazi_tablu(tabla,dostupno)
            if provera(tabla,i)==True:
                print(f"Igra je zavrsena. Pobednik je {j}!")
                igraj=False
                break
            elif len(uneti)<9:
                continue
            else:
                print("Igra je zavrsena bez pobednika!")
                igraj=False
                break

def igra(tabla,dostupno):
    while True:
        
        odgovor=input("Da li zelite novu igru (da,ne): ")
        if odgovor=="da":
            dostupno=[0,1,2,3,4,5,6,7,8,9]
            tabla=[" "," "," "," "," "," "," "," "," "," "]
            unosi(tabla,dostupno)
        else:
            break
dostupno1=[0,1,2,3,4,5,6,7,8,9]
tabla1=[" "," "," "," "," "," "," "," "," "," "]
igra(tabla1,dostupno1)
