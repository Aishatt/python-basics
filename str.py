
multiline_str= """ejneen Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(multiline_str)

loop= "Aisha"
print(len(loop))
for x in loop:
    print(x)
if 'i' in loop :
    print("i is present")    

if 'w' not in loop:
    print('w is not presnt')
    print(loop.replace('a','t'))

    b = " Hello, World! "
print(b[2:5]) #fom index 2 exclude 5
print(b[:5])  #from beginning exclude 5
print(b[2:])  # fro 2 to end
print(loop.upper())
print(loop.lower())
print(b.strip()) # remove white spaces

s= "fine girl"
print(s.split(","))
print(s+b)
age= 36
name= str(input("name :\t"))
txt= "My name is {} \r,and i am {}" #can be indexed {0}-name...
print(txt.format(name,age))
text= "We are the 'vikings' from the north"
print(text)
tet= "We are the \"vikings\" \f from the \rnorth"
print(tet)