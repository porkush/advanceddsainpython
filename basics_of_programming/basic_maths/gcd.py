
def gcd(a,b):
    while(b!=0):
        a,b=(b,a%b)
    return a

a= int(input("enter a"))
b= int(input("enter b"))
print(f"gcd of {a} and {b} is {gcd(a,b)}")
