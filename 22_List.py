l = [3, 5, 6]
print(type(l))
for i in l:
    print("List elements are", i)

# store multiple variable in single list
lst = [1, "a", 2, "b", False]
print(lst)
# output:[1, 'a', 2, 'b', False]


# Negative Indexing to Positive Indexing
print(lst[-3])  # len(lst)-3 = 5-3 = 2 = lst[2] = 2

# in keyword
lst2 = [1, "a", 2, "b", False]
if "c" in lst2:  # using (in) keyword we can find that an item of list is three or not which i considered
    print("Yes(use of in keyword)")
else:
    print("no(use of in keyword)")

lst3 = [1, "a", 2, "b", 3, "c", 4, "d"]
print(len(lst3))
num_list = lst3[0:len(lst3):2]  # [from:to:jumping_digit(0+2=2=>2+2=4=>4+2=6)]
char_list = lst3[1:len(lst3):2]  # [from:to:jumping_digit(1+2=3=>3+2=5=>5+2=7)]
# we can fetch a list data by doing this type of tricks instead of using loops and different stuff
print("(fetch a data from same list using from:to:jump concept)", num_list, char_list)

# list Comprehension:create a list at there
lst = [i for i in range(5)]
print("(Create an comprehensive list)", lst)

lst = [i for i in range(10) if i % 2 == 0]  # also include if else
print("lst(if condition concept)", lst)

new_lst = [i for i in lst3]
print("new_list(copying concept)", new_lst)  # copy one list data into another
