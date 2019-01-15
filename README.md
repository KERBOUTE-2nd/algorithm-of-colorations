# algorithm-of-colorations
python solution

x = int(input("enter the number of vertices you want to enter"))
sommets = []
for i in range(x):
    u = str(input("enter the vertices of your graph"))
    sommets.append(u)

l = {}
input("""enter each vertex and their adjacent shaped form for example
a and adjacent with b and c we write >>> a then >>> bc ... with for
  >>> c then >>> a ... is necessary, 'other summits ect also for >>> b and a ...
  typing on keyboard for continuous""")
for i in range(x):
    h=input("enter a summit")
    m=str(input("enter their adjacent form linked string"))
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


def def3():
    for sommet in sommets:
        colorersommets[sommet] = def2(sommet)

    print(colorersommets)


# fin de la liste des deffinitions ;(

def3()
print("we are not responsible if you do not respect the instructions")
a=colorersommets.values()
nbr=0
for i in couleurs:
    passage=list(a)
    element=passage.count(i)
    if element!=0:
        nbr+=1
print("the chromatic number of graph is : apha<",nbr)
