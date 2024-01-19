# tup = (1) output: <class 'int'> 1
# we need coma(,) in tuple to now showcase the tuple types as int
tup = (1,)
print(type(tup), tup)

tup1 = (1, 2, 3)
# tup1[0] = 1 : illegal for tuple but legal only for list
# Tuples are immutable
print(tup1)

if 3 in tup1:
    print("yes")
else:
    print("no")

# same as list just a difference is that the list in mutable and tuple is immutable
