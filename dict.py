#python dictionaries : key-value pairs
#cant access by indexing

#accessing elements of a dict
member= {'name': "Aisha", 'school': 'lautech'}
print(member.get('name'))
print(member['school'])

#dict are mutable, update a value or add a new key pair value
member['name']= 'Islamiyat'
member['occupation']='developer'
print(member)

#delete an item or whole dict
del member['occupation']
print(member)

#dict functions
print(member.keys())
print(member.values())#returns list of all values
print(member.items()) #returns a list in form of tuples
print(member.clear()) #returns an empty dictionary

#####
employee={
    100: 'james',
    101: 'laurel'
}
employee.update({102:'jane',103:'jon'})

# dict can be a list or tuple data type
employee.update({'countries':["india","Nigeria","china"]})
print(employee.keys())
print(employee.values())

#access element of the list
employee['countries'].append('UAE')
employee['countries'].remove('china')
employee.get('countries').append('kenya')
del employee['countries']
print(employee)

#iterating over dicts
nw=[]
for i in employee:
    print(i) # returns only the keys

for i in employee.values():
    print(i)
    nw.append(i)
print(nw)

for i in employee.items():
    print(i) #returs both keys and values

#membership
if 100 in employee:
    print("james found")