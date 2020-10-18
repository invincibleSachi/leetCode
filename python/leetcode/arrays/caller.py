from iterables import Cubes,Fib,StrReverse

def getCubes():
    print()
    y=Cubes.cubes(3,9)
    for x in y:
        print(x)
    print(sum(y))

def getFib():
    y=Fib.Fib(400)
    for x in y:
        print(x)
def strReverse():
    y=StrReverse.StrReverse("Kaalapaani")
    for x in y:
        print (x)

if __name__=="__main__":
    strReverse()