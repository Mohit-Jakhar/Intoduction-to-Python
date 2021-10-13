# Fibonacci Series upto 8th term.

nterms=8
n1=0
n2=1
count=0
tup=()
if nterms<=0:
print("PLEASE ENTER A POSITIVE INTEGER.")
elif nterms==1:
print("FIBONACCI SEQUENCE UPTO",nterms,":")
    print(n1)
else:
    print("FIBONACCI SERIES UPTO",nterms,":")
while count<nterms:
    tup=tup+(n1,)
    nth=n1+n2
    n1=n2
    n2=nth
    count+=1
    print(tup)
