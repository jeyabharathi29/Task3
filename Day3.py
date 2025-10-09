#Odd or Even
num=int(input("Enter a number:"))
if num % 2 == 0:
   print("The number is Even")
else:
    print("The number is Odd")

#Vote
age=int(input("Enter your Age:"))
if age >=18:
    print("You are Eligible to Vote.")
else:
    print("You are not Eligible to Vote.")
    
   
#Fuzz and Buzz
number =int(input("Enter a number:"))
if(number%3==0)and(number%5==0):
    print("FUZZ and BUZZ")
elif(number%5==0):
    print("BUZZ")
elif(number%3==0):
    print("FUZZ")
else:
    print("statement is not clear")


