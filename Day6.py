#Task1
n=0
while True:
    n+=1
    print(n, "J")
    if n==10:
        break

#Task2
print("Task2")
list1=[]
list2=[]
i=0
while i<=100:
    if i%2==0:
        list1.append(i)
    else:
        list2.append(i)
    i+=1
print(list1)
print(list2)