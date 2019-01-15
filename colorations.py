x = int(input("entrer le nombre de sommets que vous voulez entrer"))
sommets = []
for i in range(x):
    u = str(input("entrer les sommets de votre graphe"))
    sommets.append(u)

l = {}
input("""entrer chaque sommet et leur adjacent a forme suite par exemple 
a et adjacent avec b et c on ecrit >>>a puis >>> bc... avec pour
 >>> c puis >>> a... est necessere ,'autres sommets ect aussi pour>>>b et a...
 taper sur clavier pour continue""")
for i in range(x):
    h=input("entrer un sommet")
    m=str(input("entrer leur adjacent sous form chaine de caractaire liée"))
    k=list(m)
    l[h]=k

couleurs = ['Red', 'Blue', 'Green', 'Yellow', 'Black']

colorersommets = {}


# liste des deffinitions ;)
def def1(sommet, couleur):
    for i in l.get(sommet):
        p = colorersommets.get(i)
        if p == couleur:
            return False

    return True


def def2(sommet):
    for couleur in couleurs:
        if def1(sommet, couleur):
            return couleur


def gogogo():
    for sommet in sommets:
        colorersommets[sommet] = def2(sommet)

    print(colorersommets)


# fin de la liste des deffinitions ;(

gogogo()
print("on est pas responsable si vous n'avez pas respecter les consignes ")
a=colorersommets.values()
nbr=0
for i in couleurs:
    passage=list(a)
    element=passage.count(i)
    if element!=0:
        nbr+=1
print("le nombre chromatique de se graphe est: apha<",nbr)
