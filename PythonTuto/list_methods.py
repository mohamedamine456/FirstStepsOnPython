# declare a list
numbers = [2, 1, 5 , 6, 7, 9, 1, 4]

# add item to a list
numbers.append(12)

# add item on an index
numbers.insert(0, 14)

# remove item
numbers.remove(6)

# print the list
print(numbers)

# remove last item in list
numbers.pop()

# get the index of item
print(numbers.index(2))

# check existing
print(5 in numbers)

# count occurances of item
print(numbers.count(1))

# sort the list
numbers.sort()

# reverse the list
numbers.reverse()

# copy the list
numbers2 = numbers.copy()

# clear all list
print(numbers2)
numbers2.clear()
print(numbers2)

print(numbers)