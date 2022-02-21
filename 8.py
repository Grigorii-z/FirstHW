print("Your name?")
a=input()
print("Your age?")
b = int(input())
c=0
if (a.isspace())==True:
    print("Введите Имя правильно - без пробелов")
    c=1
if (a.isalpha())==True:
    print("ВВедите Имя правильно - без цифр")
    c=1
if b<0 and b>150:
    print("Введите коректный возраст!")
    c=1
if c==0:
    print(a," ",b)
