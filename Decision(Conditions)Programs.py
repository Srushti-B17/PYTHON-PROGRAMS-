'''
# IF statement
a=20
if(a==20):
    print("condition is false")
    print(a)

# if else---
a=int(input("enter the number "))
if(a>2 and a<30):
    print("Number satisfies condition")
else:
    print("Number is out of range")

x=int(input("enter the number 1"))
y=int(input("enter the number 2"))
if(x%2==0 and y%10==0):
    print("Number is even and multiple of 10")
else:
    print("Number is odd and not multiple of 10")

'''
# A=int(input("enter the number 1"))
# B=int(input("enter the number 2"))
# if(A%2==0  or  B%10==0):
#     print("Number is even and multiple of 10")
# else:
#     print("Number is odd and not multiple of 10")

#Nested if
# a=int(input("enter the number "))
# b=int(input("enter the number "))
# c = int(input("enter the number "))
# if(a>b):
#     print("value of a is greater ")
# elif(b>c):
#     print("value of b  is greater")
# elif(a>c):
#     print("value of a is greater ")
# elif(c>a):
#     print("value of c is greater ")
# else:
#     print("value of all are same ")

#Elif statement

# marks= int(input("enter the marks"))
# if(marks<=100  and  marks>=90):
#     print(" A+  ")
# elif(marks<90  and marks>=80):
#     print("A")
# elif(marks<80  and  marks>=70):
#     print("B+")
# elif(marks<70  and  marks>=60):
#     print("B")
# elif(marks<60  and  marks>=50):
#     print("c+")
# elif(marks<50  and  marks>=40):
#     print("c")
# else:
#     print("student is failed !!!")
