# lists can stores muiltiple datatypes
#lists are mutable, meaning they can be changed after creation
marks = [54,34,65,78,98,100]
mixed = [43, "Hello", False, 4.2]

print(marks);
print(mixed);


print(marks[0]); # 54
print(marks[1]); # 34   
print(marks[2]); # 65
print(marks[3]); # 78
print(marks[4]); # 98
print(marks[5]); # 100

print("\n");

print(marks[0:3]); # [54, 34, 65]
print(marks[1:4]); # [34, 65, 78]
print(marks[2:5]); # [65, 78, 98]
print(marks[3:6]); # [78, 98, 100]
print(marks[4:7]); # [98, 100]
print(marks[5:8]); # [100]