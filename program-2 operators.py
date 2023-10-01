'''operators in python
1. Arithmetic opearor
2.Assignment operator
3.Comparison opeartor
4.Logical opeartors
5.Bitwise operators
6.Identity opeartors
'''

a=5
b=10
c=30

print("Arithmetic")
print("Addition of two numbers " ,a,"and ",b,"is",a+b)
print("Substraction of two numbers " ,a,"and ",b,"is",a-b)
print("Multiplocation of two numbers " ,a,"and ",b,"is",a*b)
print("Division of two numbers " ,a,"and ",b,"is",a/b)
print("Remainder of two numbers " ,a,"and ",b,"is",a%b)

print("\n")

print("Assingement oerators")
a=10
print("value of a is ",a)
a+=25
print("value of a becomes after adding 25 is",a)
a-=5
print("value of a becomes after substracting 5 is ",a)
a*=12
print("value of a becomes after multiplying 12 is ",a)
a%=2
print("value of a becomes division from 2 is ",a)

print("\n")

print("Comparison operators")
x=15
y=20
print(x>y)
print(x<y)
x+=5
print(x==y)
y-=5
print(x>=y)
print(x<=y)
x-=5
print(x)
print(y)
print(x!=y)

print("\n")

# Logical opeartors
P=True
Q=False
print("result of AND opeartion is " ,P and Q)
print("result of OR opeartion is " , P or Q)
print("result of NOT opeartion is " ,not Q)

print("\n")

# Bitwise opearator
A=10
B=5
print(A&B)
print(A|B)
print(A^B)
print(~A)

x = (1 == True)
y = (2 == False)
z = (3 == True)
a = True + 10
b = False + 10

print("x is", x)
print("y is", y)
print("z is", z)
print("a:", a)
print("b:", b)