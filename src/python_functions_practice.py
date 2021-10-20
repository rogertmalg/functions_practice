def return_10():
    return 10

def add(num1, num2):
    return num1 + num2 

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def length_of_string(test_string):
    return len(test_string)

def join_string(string_1, string_2):
    return string_1 + string_2

def add_string_as_number(a, b):
    return int(a) + int(b)

def number_to_full_month_name(month):
    months =  ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return months[month -1]

def number_to_short_month_name(month):
    short_month = number_to_full_month_name(month)
    return(short_month[0:3])

def cube_volume(length):
    return length * length * length

def reverse_string(word):
    return word[::-1]
    # another option
    # return "".join(reversed(word))

def cel_fah(f):
    return int((f - 32) / 1.8)