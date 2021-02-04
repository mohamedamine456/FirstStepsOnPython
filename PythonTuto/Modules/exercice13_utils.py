# define functions

def find_max(numbers):
    max_number = 0
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number


def find_min(numbers):
    min_number = numbers[0]
    for number in numbers:
        if number < min_number:
            min_number = number
    return min_number
