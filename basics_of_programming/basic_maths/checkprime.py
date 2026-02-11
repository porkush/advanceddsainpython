def checkprime(a):
    if a<2:
        return "Not prime"
    for i in range(2,int( a**0.5)+1):
        if a%i==0:
            return "Not prime"
    return "Prime"

a= int(input("enter number"))
print(f"the output is {checkprime(a)}")
