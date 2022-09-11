def lists():
    my_list= ["rice","beans","garri","dodo","beans"]
    new= str(input('what are you buying? '))
    my_list.append(new)
    print(my_list)
    new2= str(input('buying more ? '))
    my_list.insert(1,new2)
    print(my_list)
    my_list.remove(new2)
    print(my_list)
    print(my_list.count("beans"))

#lists() 

lst=[ ] 
for x in range(1,10):
    if x%2==0:
        lst.append(x)
print( lst )

#list comprehension===> python smart list
#var_name=[output_exp,input_seq,varx,condition]
even=[x for x in range(1,10) if x%2==0]
print(even)
str="ello there"
charlist=[x for x in str if x != ' ']
print(charlist)
print(str)