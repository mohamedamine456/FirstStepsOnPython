# define a function with parameters
def greet_user(firstname, lastname):
    print(f"Hi {firstname} {lastname}!")
    print("Welcome To Python Functions")


# call function with keyword parameter
# in keyword parameter the position of parameter doesnt matter
# either use positional or keyword arguments
print("Call of Function with Parameters:")
greet_user(firstname="Mohamed", lastname="LACHHEB")
print("Call it One more Time with Different Values:")
greet_user(lastname="EL ORCHI", firstname="El mehdi")
print("End.")