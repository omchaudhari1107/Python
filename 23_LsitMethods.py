l = [1, 2, 3, 4]
print(l)

l.append(5)
print("After append", l)

l.sort(reverse=True)  # or l.sort()
print(l)

l.reverse()
print(l)

print(l.count(2))  # use to count repeated number inside of list

m = l.copy()
m[0] = 0
print(l)
print(m)
# if we do
# m=l
# m[0] = 0
# print(l) then l will also change due to reference, but we only use copy function


l.insert(1, 63456)
print(l)

m = [900, 1000, 1100]
l.extend(m)  # OR new_list = l + m
print(l)
# OR
new_list = m + l
print(new_list)
