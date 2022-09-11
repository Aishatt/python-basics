import random
text= "im new,yes 12 are new"
print(text.capitalize())
print(text.casefold())
print(text.center(50))
print(text.count('new'))
#print(text.expandstabs(10))
print(text.isalnum())
print(len(text))

#specialoperator membership (in,not in),identity (is,is not)
a= "pythonprog"
b= 3
c= 3
d=8
print("p" in a)
print("s" not in a)
print(d // c)
print(b is not c)
print(id(a)) #memory address

# walrus operator:assign to var within an exp using d notation
#colon and equal sign used together :=
#combines steps of declaration n implementation same time
print(name:= "aisha")
print(a[::2])
first="aisha"
last="ade"
print(" ".join([first,last]))
print(a.find("x"))
print(a.find("g"))
print(a.count("a"))
print(a.capitalize())
print(a[2::3])

ask= "aishat"
for i in ask:
    if ("sha") in ask:
        print("aisha")
        break
    else:
        print("not there")
        break

loop_m= 'aisha'
for i in loop_m[1:3]:
    print(list(i.capitalize()))

count= 0
while count < 4 :
    print('hello')
    count=count+1
#print odd or even

for i in range(1,10,2):
    if i%2==0:
        print("its even", i)
        break
    else:
        print('its odd', i)
      
num= int(input('enter number you want to generate even number to(range): '))
i=0
while i<= num:
    if i % 2 == 0:
          print("its even", i)
        
    else:
        print('its odd', i)
    i=i+1
#print(list(range(1,5)))