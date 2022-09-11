#its a read only list
#immutable ordered list,works like list
#except that it csant be edited
#can be concat and repeated (+ ,*)
employee_dob=(1994,1996,1993,1897)
employee_dob2=(1992,1993,1995,1895)
#print(employee_dob + employee_dob2)
#can also use membership op
print(1992 in employee_dob) 
#iterate over tuple
#only index and count method can be used
print(employee_dob2.count(1998))
print(employee_dob2.index(1995))
#iterating 2ru tuple is faster than list
#generally used for heterogenous data(diff datatypes)
#list is for homogenoue datatypes
#tuples immutable element can be used as keys for dictionaries
#better when working with data that doesnt change 