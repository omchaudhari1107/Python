letter = "Hey my name is {1} and i am from {0}"
country = "India"
name = "om"

print(letter.format(name, country))
print(letter.format(country, name))

# we can do this using F string: need to just add f
# now we use f string instead of .format
print(f"Hey my name is {name} and i am from {country}")
print(type(f"Hey my name is {name} and i am from {country}"))
