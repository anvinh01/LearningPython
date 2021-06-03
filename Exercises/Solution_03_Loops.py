# Remember there are multiple Solutions.
# It is more important to experiment and get a deeper understanding.
# In this exercise you can also try to write down multiple solutions

# ===============================================================
# 3.0:
# first write down an input("Exercise Number")
# depending on the input number we will run the Exercise number
exercise_nr = int(input("Exercise number: "))
if exercise_nr == 1:
    # 3.1:
    # write a loop which prints out all even numbers from (10, 30)
    # try to write 2 different approaches

    # 3.1.1:
    for i in range(10, 31):
        if i % 2 == 0:
            print("approach 1:", i)

    # 3.1.2:
    for j in range(10, 31, 2):
        print("approach 2:", j)

elif exercise_nr == 2:

    # 3.2:
    # write the fibonacci sequence down.
    # fibonacci sequence: 1, 1, 2, 3, 5, 8, 13, 21, 33, 54
    # the sequence from 1 to 100
    a = 1
    b = 1
    while (a + b) < 100:
        a = a + b
        if a <= 100:
            print(a)

        b = b + a
        if b <= 100:
            print(b)

elif exercise_nr == 3:

    # Write an input
    # calculate the falkutät from the number
    number = int(input("number in: "))
    temp = 1
    for k in range(1, number + 1):
        temp = temp * k
    print("after calculating:", temp)

else:
    print("no valid exercise number")



