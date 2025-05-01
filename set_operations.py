a = {12,23,45,67,89,90};
b = {23,45,67,89,90,100}; # set of numbers
c = a.union(b); # union of a and b
print(c); # {100, 2, 3, 4, 5, 6, 7, 8, 9, 10}

d = a.intersection(b); # intersection of a and b
print(d); # {23, 45, 67, 89, 90}