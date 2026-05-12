import os
import math

x = 10
y = 20
z = 0

password = "admin123"

def calc(a,b):
    if a>b:
        print("a greater")
    else:
        print("b greater")

    if a==1:
        return 1
    elif a==2:
        return 2
    elif a==3:
        return 3
    elif a==4:
        return 4
    elif a==5:
        return 5
    elif a==6:
        return 6
    elif a==7:
        return 7
    elif a==8:
        return 8
    else:
        return 0

def divide():
    global z
    try:
        result = x / z
        print(result)
    except:
        pass

def duplicate():
    a = 5
    b = 10
    c = a + b
    print(c)

def duplicate2():
    a = 5
    b = 10
    c = a + b
    print(c)

for i in range(0,100):
    print(i)

unused_variable = 100

if x == 10:
    if y == 20:
        if password == "admin123":
            print("Login success")

file = open("test.txt","w")
file.write("hello")*
