print("Your name?")
a = input()
print("Your age?")
b = int(input())
count=0
mult=1
sum=0
c=0
for i in a:
    count+=1
while b>0:
    c=b%10
    b=b//10
    sum+=c
    mult=mult*c
print(count, "We count letters")
print(sum, "Add your age", mult, "Multiply your age")