# 06 tuple

print("July", '\t', type("July"))
print(2021, '\t', type(2021))
print(3.14, '\t', type(3.14))
print(True, '\t', type(True))
print()

data = ("July", 2021, 3.14, True)   # Tuples are immutable sequences
for d in data:
    print(d, '\t', type(d))
