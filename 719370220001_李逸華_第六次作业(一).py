# LeeIHua
def sumN(n):
    sumN = 0
    for i in range (n+1):
        sumN = sumN +i
    return sumN    

def sumNCubes(n):
    sumNCubes = 0
    for i in range(1,n+1):
        cubicNumber = i**3
        sumNCubes = sumNCubes+cubicNumber
    return sumNCubes

def main():
    n = int(input("please enter the number:"))
    print("the sum of the first n natural numbers is"
          ,sumN(n))
    print("the sum of the cubes of the first n natural numbers is",sumNCubes(n))
main()
input()
