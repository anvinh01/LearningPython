# Remember there are multiple Solutions.
# It is more important to experiment and get a deeper understanding.

# ===============================================================
# 1.1
# get multiple inputs for the Name, Age, one_hobby
# afterwards print out a whole introduction of yourself:
Name = input("my name:")
Age = input("my Age:")
Hobby = input("my Hobby:")
print(f"Hello there. My name is {Name} and I am {Age} years old. My Hobby is {Hobby}")

# 1.2
# now do the same thing again, but this time we add a line:
# "I was born in the year ...."
# your job is to calculate the year with the Age input
current_year = 2021
birth_year = current_year - int(Age)
print(f"Hello there. My name is {Name}. I was worn in {birth_year} and am {Age} years now. My Hobby is {Hobby}")

