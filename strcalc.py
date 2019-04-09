str=input("Enter string:")
l=0
u=0
d=0
s=0
for i in str:
	if(i.islower()):
			l+=1
	elif(i.isupper()):
			u+=1
	elif(i.isdigit()):
			d+=1
	else:
		s+=1
print("Number of Upper Case: ", u)
print("Number of Lower Case: ", l)
print("Number of Digits: ", d)
print("Number of Special Symbols: ", s)
