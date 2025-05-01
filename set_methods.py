s = {2,1,4,5,6,7,9};

print(s); # {1, 2, 4, 5, 6, 7, 9}
s.add(32); # add 32 to the set
print("added = ",s); # {1, 2, 4, 5, 6, 7, 9, 12, 14, 32, 322}

# s.remove(242323); #this will throw an error if 242323 is not in the set
s.discard(242323); # this will not throw an error if 242323 is not in the set