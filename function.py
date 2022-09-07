def calculate(change):
    coins=[2,1.4,0.5,0.05]

    for coin in coins:
      #  remainder= change % coin 
        no_of_coins= int(change/coin)
        print(str(coin) +': '+ str(no_of_coins))
     #   change=remainder
def name():
    my_name= str(input("what is your name: "))
    age= int(input("your Age: "))
    print(my_name)
    print(age)

def f():
    s="i am s i live inside f()"
    print(s)
    name()
#passing parameter(formal para..) to be called with args(actual para...)
def q(qty,item,price):
    print(f'{qty} {item} costs {price}')

#passling mutable parameter(lists)
def l(my_list=[]):
    my_list.append('###')
    print(my_list)
    return my_list
count=1
while (count < 11):
    print(count)
    count= count + 1

if count == 11:
    print("counting complete")
    

#calculate(4)
l(["aisha","24","Developer"])
f()
print("Welcome s")
q(1,'banana','$250')

num1=4
num2=2
print("division is", num1 % num2)
print("floor division", num1 // num2)



