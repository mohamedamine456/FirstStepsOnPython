# define dictionary
customer = {"name": "Moctar", "age": 24, "is_verified": True}

# print it
print(customer)

# access dictionary
print(customer["name"])

# to access it without getting error in case of nonexisting use get method,also u can give it a default value
print(customer.get("birthDay", "2-04-2021"))

# updating value
customer["name"] = "Mamado Moctar"
print(customer)

# add new key
customer["birthday"] = "11-30-1996"
print(customer)