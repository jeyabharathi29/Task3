$LIST
transport= ["Bike", "Car", "Train"]
transport.append("Cycle")
print(transport)
another_transport=["Flight"]
transport.extend(another_transport)
print(transport)
transport.remove("Cycle")
print(transport)
removed_item=transport.pop(2)
print("Removed Item:",removed_item)
print(transport)
count=transport.count("Bike")
print("count of bike",count)
transport.reverse()
print("Reveresd List",transport)
new_transport=transport.copy()
print("Copied List",new_transport)
transport.clear()
print(transport)

$TUPLE
tuple=(11,22,11,33,44,55)
count=tuple.count(11)
print(count)
index_value=tuple.index(33)
print("Index of 33:",index_value)

$SET
set1={"Apple","mango","cherry"}
set1.add("plam")
print(set1)
new_items={"banana"}
set1.update(new_items)
print(set1)
set1.remove("plam")
print(set1)
set1.discard("banana")
print(set1)
item=set1.pop()
print("Removed:",item)
print(set1)
set2={"Apple","Blueberry"}
print("Union:",set1.union(set2))
print("Intersection:",set1.intersection(set2))
set1.clear()
print("Cleared",set1)

$DICTIONARY
my_dict = {"name": "Jeyabharathi", "Age": "21", "City": "Madurai"}
my_dict.keys()
print(my_dict.keys())
my_dict.values()
print(my_dict.values())
my_dict.items()
print(my_dict.items())
print(my_dict.get('name'))
print(my_dict.get('Age'))
print(my_dict.get('City'))
my_dict.update({"country": "India"})
print(my_dict)
item = my_dict.popitem()
print("Removed item:", item)
print("Dictionary after popitem:", my_dict)
copied_dict=my_dict.copy()
print(copied_dict)
my_dict.clear()
print("Cleared",my_dict)