# get a value with try except to ignore Errors
try :
    age = int(input("Age: "))
    # print value
    print(age)
except ValueError:
    print("Invalid Value")


def division(a, b):
    try :
        result = a / b
        return result
    except ZeroDivisionError:
        print("Invvalid Division")


print(division(4, 0))