#Task1
numl=int(input ("Enter your First Number:"))
num2=int(input("Enter your Second Number:"))
operator input ("Enter your Operator:")
if operator=="+":
	print (numl+num2)
elif operator=="-":
	print (numl-num2)
elif operator=="*":
	print (num1*num2)
elif operator=="/":
	print(num1/num2)
else:
	print("Not Operator Found")
	

#Task2
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def multy(n1,n2):
    return n1*n2
def division(n1,n2):
    return n1/n2
n1=int(input("Enter the no1:"))
n2=int(input("Enter the no2:"))
symbol=input("Enter the symbol:")
if symbol=="+":
    print(n1+n2)
elif symbol=="-":
    print(n1-n2)
elif symbol=="*":
    print(n1*n2)
elif symbol=="/":
    print(n1/n2)
else:
    print("none")