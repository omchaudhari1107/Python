dic = {"name": "om", "age": 19, "eligible": True}

# print(dic['name']) it give error if an element not exist
print(dic.get("name2"))  # it give None as output of an element not exist

print("-------")

print(dic.keys())
for key in dic.keys():
    print(f"{key}:{dic[key]}")

print("-------")
# idc.items() give the key with calue in truple form
for key, value in dic.items():
    print(key, ":", value)
