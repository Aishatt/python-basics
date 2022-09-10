text= "im new,yes 12 are new"
print(text.capitalize())
print(text.casefold())
print(text.center(50))
print(text.count('new'))
#print(text.expandstabs(10))
print(text.isalnum())
print(len(text))

#specialoperator membership (in,not in),identity (is,is not)
a= "python"
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

