# Loops
# Very often the code is repeating itself.
# for that reason we have 2 kinds of Loops to offer.
# one is the while-Loop and the other one is called a for-Loop

# =========================== while-Loop ========================================
# A while-Loop has an exit-condition just like an if-statement
# The condition will be checked again, after each run in the Loop
# Example 1:
print("Example 1:")
a = 1                     
while a <= 10:                  # The Loop will run as long as the condition is still met. Else it will exit it     
    print("a is now:", a)
    a = a + 1                   # if we dont increase the value of a, the Loop will go on forever, since the condition has to be met.


# we can also forcefully go out of the Loop with "break"
# Example 2:
print("\nExample 2:")
a = 1
while a <= 10:
    if a == 4:
        print("the Loop stoped at a == 4")
        break
    print("in while-Loop:", a)
    a = a + 1

print("We are ouside the Loop and a has the value:", a)
# when the if-statement activates the command "break" will be run and the Loop will be exited

# Note: "while True:" will run forever until there is a break

# ======================== for-Loop =================================
# Your understanding of a for-Loop will deepen in the next chapter.
# For now the for-Loop will be used to Loop through numbers

# first we create the variable "i" which will change it value according to a "range()"
# the range has a start, end, and optional step value ==> range(start, stop, step*)
# step* is per default 1
# Example 3:

print("\nExample 3:")
for i in range(0, 10):
    print("for-Loop output:", i)

# the output will be 1 to 10



