names = ["Rafid", "Sakib", "Ragib", "Towhid"]

print(names)
print(names[0])
print(names[0:3])
print(len(names))

names.remove("Rafid")
print(names)

names.insert(2, "Undertaker")
print(names)

print("Sakib" in names)
print("Rafid" in names)