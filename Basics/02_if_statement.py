# if-statements
# just like in english the if-statement runs the code, when the condition is met.
# the code inside the if-statement is defined by the indent of the code outline

# Example
random_var = True
if random_var == True:
    # The executed code, when the condition is met, should be indented
    print("random_var is true")

# The code that should follow afterwards should not be indented anymore
print("This is after the if-statement")


# =============== if - elif - else ====================
# instead of writing multiple if-statements it is much better and visualy easier
# to use an (if-elif-else) statement
# (if) takes a condition. When the condition is NOT met, then it goes over to the (elif)
# just like (if), (elif) takes a condition and will not execute when the condition is not met
# if none of the conditions are met, then the coder inside (else) will run

# an if-statement doesn't have to consist of all 3 components. It can also consist of just:
# (if-else) or (if-elif) But an (if) is needed

# Example:
number = 30
if number < 30:
    print("number is smaller than 30")
elif number < 90:
    print("number is larger than 30 but smaller than 90")
else:
    print("the number is larger than 90")


# ================== Logistic and comparison ========================
# for comparison we have: < (smaller), > (larger), == (equal), <= (smaller or equal), >= (larger or equal), != (not equal)

a = 30
b = 30

smaller = a < b         # False
larger = a > b          # False
equal = a == b          # True
small_eq = a <= b       # True
large_eq = a >= b       # True
not_equal = a != b      # False

print(f"smaller: {smaller}\nlarger: {larger}\nequal: {equal}\nsmaller or equal: {small_eq}\nlarger or equal: {large_eq}\nnot equal: {not_equal}")

# Logistic operations are: and, or, not (can also we written as [&&, ||, !])
# it can be applied to get multiple comparison in an if-statement

# Example
goes_to_party_often = True
age = 22

# connecting two comarison with an "and". Both condition have to be met for the inner code to run
if (goes_to_party_often == True) and (age >= 18):
    print("most likely a univeristy student")
else:
    print("seems normal to me")

