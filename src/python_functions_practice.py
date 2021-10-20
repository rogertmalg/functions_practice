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
    test_string = "aaaaaaaaaaaaaaaaaaaaa" 
    return len(test_string)
#  Unsure why line 30 in test is there 

def join_string(string_1, string_2):
    return string_1 + string_2

def add_string_as_number(a, b):
    return int(a) + int(b)

def number_to_full_month_name(month):
    months =  ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return months[month -1]