a=int(input("Enter number a:"))
b=int(input("Enter number b:"))
c=int(input("Enter number c:"))
p=b**2-4*a*c
m=2*a
if p<0:
   	print("Roots are imaginary")
else:
   	print(“First root is:”, ((-b+ p)/m)), ”Second root is:”, ((-b-p)/m))
