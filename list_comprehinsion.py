# #create a list containing table 5

# a = 5;
# table = []; # create an empty list to store the table
# for i in range(1, 11):
#     table.append(a * i); # append the product of a and i to the list
# print(table); # [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

table = [5 * i for i in range(1, 11)]; # create a list containing table 5 using list comprehension
print(table); # [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]