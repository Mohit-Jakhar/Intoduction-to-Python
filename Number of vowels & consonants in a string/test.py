name= str(input("enter any string:"))
vow=0
con=0
l=len(name)
for i in range(0,l,1):
if name[i]=='a' or name[i]=='e' or name[i]=='i' or name[i]=='o' or name[i]=='u':
vow=vow+1
else:
con=con+1
print("No. of  vowel is :",vow)
print("No. of consonants is : ",con)
