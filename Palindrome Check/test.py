# Palindrome - String being read forward or backward is same
def main():
      istr=input("ENTER A STRING")
      if Palindrome(istr):
            print("THE STRING IS PALINDROME")
      else:
            print("THE STRING IS NOT A PALINDROME")
def Palindrome(string):
      if len(string)<=1:
            return True
      if string[0]==string[len(string)-1]:
            return Palindrome(string[1:len(string)-1])
      else:
            return False
main()
