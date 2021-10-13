def power(x, n):
      if (n==0):
            return 1
      else:
            return x*power(x,n-1)
a=int(input("ENTER NUMBER"))
b=int(input("ENTER THE POWER"))
print(power(a, b))
