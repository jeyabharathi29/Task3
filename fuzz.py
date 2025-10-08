number =int(input("Enter a number:"))
if(number%3==0)and(number%5==0):
    print("FUZZ and BUZZ")
elif(number%5==0):
    print("BUZZ")
elif(number%3==0):
    print("FUZZ")
else:
    print("statement is not clear")
