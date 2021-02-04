#define a lits
names = ["Moctar", "El mehdi", "Otmane", "Ayoub", "Haitam"]

#print the list defined
print(names)

# print element by index
print(names[2])
print(names[-2])

# print by range
print(names[1: 4])
print(names[2:])
print(names[:3])

# modify element
names[0]  = "Mamado Moctar"
print(names)