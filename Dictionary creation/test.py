d={}    #Creating Dictionary with name as key and number of winning as values.
n=int(input("How many Students?"))
for i in range(n):
        key=input("Enter the name of Student:")
        value=int(input("Enter No. of wins:"))
d[key]=value
print(d)
