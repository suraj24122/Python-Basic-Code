#dictonary stores data in key-value pairs

marks = {"suraj":34, "jack":43, "john":23, "jane":45}
print(marks); # {'suraj': 34, 'jack': 43, 'john': 23, 'jane': 45}
print(type(marks)); # <class 'dict'>

#common dictionary methods
print(marks.keys()); # dict_keys(['suraj', 'jack', 'john', 'jane'])
print(marks.values()); # dict_values([34, 43, 23, 45])
print(marks.pop("jack")); # 43
print(marks); # {'suraj': 34, 'john': 23, 'jane': 45}