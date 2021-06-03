# Remember there are multiple Solutions.
# It is more important to experiment and get a deeper understanding.

# ===============================================================
# 2.1
# You will create a simple calculator which will get 3 inputs.
# Create 3 variables a, b and operation.
# All three should be an input. a and b should be an integer.
# the operation will be an input. The user has to input "+", "-", "*" or "/"
# depending on the operation the output should print out the calculation
# if an invalid operation is given in, the output should say so.

a = int(input("a: "))
b = int(input("b: "))
operation = input("operation: ")

print("output:")
if operation == "+":
    print(f"{a} + {b} = {a+b}")
elif operation == "-":
    print(f"{a} - {b} = {a-b}")
elif operation == "*":
    print(f"{a} * {b} = {a*b}")
elif operation == "/":
    print(f"{a} / {b} = {a/b}")
else:
    print("   no valid operation has been selected")





