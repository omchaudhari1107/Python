s1 = {1, 2, 5, 6}
s2 = {3, 6, 7, 5}
print("Union is", s1.union(s2))
# s1.update(s2)
print(s1, s2)

print("Intersection is", s1.intersection(s2))

# symmetric difference = (AuB)-(AnB)
print("symmetric difference", s1.symmetric_difference(s2))

# Disjoint:disjoint if AnB=Null
print("Disjoint:", s1.isdisjoint(s2))

# is subset

s1.remove(1)  # error if not exist in list but to not raise error we use discard()
print(s1)

del s1  # to delete a whole list
s2.clear()  # to truncate the whole list
