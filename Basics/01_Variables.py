string = "ist text oder eine Zeichenkette"

integer = 5

float = 5.5

# add string with string
string_add = string + string
print(string_add)

# try to add string with integer
string_add_int = string + str(integer)
print(string_add_int)

# multiplying string with integer
string_mul_int = string * integer
print(string_mul_int)

# user input is always a string
user_in = input("your input: ")
print(type(user_in))

# convertieren in integer
user_in_int = int(user_in)
print(type(user_in_int))

# convert in float
# user_in_float = float(user_in)
# print(type(user_in_float))
# doenst work