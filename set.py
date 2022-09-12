#collection of data type in pyton,unordered , 
#unique,no duplicate element
#can be modified, elements must be immutable

#create empty se
data=set()
print(type(data))

#sets are mutable but the elements are immutable
setOne={2,1,"james"}
setTwo={"saturday","monday","tuesday","friday", 2.7,}

#access elements with for loop
for i in setTwo:
    print(i)

#set operations : union,intersection,difference,copy(),
# discard,clear,sum(), isdisjoint(), add(),issubset(),
# issuperset(),pop()
A={1,2,5,3,12}
B={"ais","ha","t",12,1,3,5}
print(A|B)  #using operator
print(A.union(B)) #or using union mthd
#intersection
print(A&B)
print(A.intersection(B))
#difference
print(A-B)
print(A.difference(B))
print(B.difference(A))
C={2,4,3,7}
D={3,9,1,5}

#functions
print(sum(C))
print(len(C))
print(min(C))
print(max(C))
#methods
C.add(43)
print(C)
C.remove(4)
print(C)
C.pop()
print(C)
print(A.issubset(B))
print(A.issuperset(B))
print(A.isdisjoint(B))
brics={'B','R','i','C'}
brics.discard('h')
print(brics)#no change ,h is not a member,will only remove an element if its a memebre
brics.remove('h') #will raise an error keyError 


 
