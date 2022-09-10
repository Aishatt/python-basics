#calculate BML
def bml():
    my_name= str(input("what is your name: "))
    age= str(input("your Age: "))
    weight = float(input("what is your weight ? \n"))
    height = float(input("what is height ? \n"))
    my_bml= str(weight/height ** 2)
    print(my_name + "\n" + age + "\n"+"BML = " + my_bml)

#conditional loop, age requirement
def sign_in():
    name= str(input("Enter name: "))
    age = int(input("Enter age? \n"))
    required_age= 18
    if(name == "john"):
        if (age is required_age):
            print("welcome john")
        elif(age > required_age):
            print("old but still eligible")
        
        print("login sucessful")
    else:
        print("input correct name")

#traffic light code
def traffic_light():
    name="True"
    light= input("what color can you see : ")
    if name == "True" :
        if light == "green":
            print("green means go!")
        elif light == "yellow":
            print("yellow means wait!")
        elif light == "red":
            print("red means go!")
        else:
            print("not a traffic color") 

        print("thats it!")
    else:
        print("not a user")    

def multi_player():
    player1= 10
    player2=20
    player3= 20

    if (player1 < player2 and player2 < player3):
        print('congrats player 3 you won')
    elif (player1 > player2 and player2 < player3):
        print('congrats player 1 you won')
    elif(player1 < player2 and player2 > player3):
        print('congrats player 2 you won')
    elif(player1 == player2 or player2 == player3):
        print('its a tie')
    else:
        print("computer wins")    

#calculate th area of a circle
def area() :
    print("Area of a cirlce")
#get radius from usr
    radius = float(input("what is the radius of the circle ? \n"))
    print("Area of a circle: \n",3.142 * radius*radius)

#Calculate Change 
def calculate(change):
    coins=[2,1.4,0.5,0.05]

    for coin in coins:
#remainder= change % coin 
        no_of_coins= int(change/coin)
        print(str(coin) +': '+ str(no_of_coins))
#change=remainder

#passing parameter(formal para..) to be called with args(actual para...)
def stock(qty,item,price):
    print(f'{qty} {item} costs {price}')

#passing mutable parameter(lists)
def append_list(my_list=[]):
    my_list.append('###')
    print(my_list)
    return my_list
count=1
while (count < 11):
    print(count)
    count= count + 1

if count == 11:
    print("counting complete")

#main  
#calculate(4)
#bml()
#append_list(["aisha","24","Developer"])
#print("Welcome s")
#stock(1,'banana','$250')
#sign_in()
#traffic_light()
multi_player()
#area()
num1=4
num2=2
#print("division is", num1 % num2)
#print("floor division", num1 // num2)



