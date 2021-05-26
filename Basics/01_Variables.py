
# ====================== Assigning Variable ====================
# assigning a variable by stating the variable name = the_dataype
# variable_name = data

# String:
# a String is list of characters. Also called a text.
# starts and ends with "text"
string = "ist text oder eine Zeichenkette"

# boolean:
# a boolean can either be true or false
boolean = True

# Integer:
# an integer is a whole number.
# The maximum value it can project is: 9223372036854775807 which is (2 ** 63) - 1
# on a 64 bit system
integer = 5

float = 5.5


# ===================== Calculating (math) =======================
a = 9
b = 3

# plus
plus = a + b

# minus
minus = a - b

# multiply
mult = a * b

# divide into float
div_f = a / b

# div into int
div_int = a // b

# modulo
mod = a % b

# print formated
print(f"a : {a}, b : {b}\n  a+b = {plus}\n  a-b = {minus}\n  a*b = {mult}\n  a/b = {div_f}\n  a//b = {div_int}\n  a%b = {mod}")


# ====================== Special string operators ========================
# add string with string
string_add = string + string
print("string add with string:\n", string_add)

# try to add string with integer
string_add_int = string + str(integer)
print("string add woth str(int):\n", string_add_int)

# multiplying string with integer
string_mul_int = string * integer
print("string multiply with int:\n", string_mul_int)

# user input is always a string
user_in = input("your input: ")
print("raw input type is:", type(user_in))

# convertieren in integer
user_in_int = int(user_in)
print("convert input to int():", type(user_in_int))

# convert in float
# user_in_float = float(user_in)
# print(type(user_in_float))
# doenst work