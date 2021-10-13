# Armstrong Number between 1-200.
num=int(input("Enter any number:"))
num1=num
Sum=0
for i in range(1,200,1):
   		digit=num%10
   		num=num//10
  		Sum+=digit*digit*digit
if num1==Sum:
    print("It is an Armstrong number.")
elif num1!=Sum:
    print("It is not an Armstrong number.")
