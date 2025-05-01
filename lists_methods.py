marks = [5,2,2,5,7,21];
extra_marks = [100, 200, 300, 400, 500]; # list of extra marks
print(marks); # [5, 2, 2, 5, 7, 21]
marks.append(63); # add 100 to the end of the list
print(marks); # [5, 2, 2, 5, 7, 21, 63]
marks.pop(); # remove the last element of the list
print(marks); # [5, 2, 2, 5, 7, 21]
marks.extend(extra_marks); # add extra marks to the end of the list
print(marks); # [5, 2, 2, 5, 7, 21, 100, 200, 300, 400, 500]
marks.remove(2); # remove 5 from the list
print(marks); # [2, 2, 5, 7, 21, 100, 200, 300, 400, 500]
marks.insert(0, 100); # insert 100 at the beginning of the list
print(marks); # [100, 2, 2, 5, 7, 21, 100, 200, 300, 400, 500]