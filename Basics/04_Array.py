# ============== "What is an Array?" ================
# An Array is a datatype which contains multiple elements.
# Commonly the elements are all from the same datatype: integer, string, etc.
# a String can also be viewed as an Array of invidual characters.

# To initialize an Array (or list) we can either write one of the following lines:
array_1 = []            # or array_1 = [1, 2, 3, 4]
array_2 = list()
# the first line of Array can already hold elements in the List
# the second one is empty but there are not many differences

# Array indexes: [0, 1, 2, 3, ....., len(Array) - 1]
# to get an element of the Array we have to call it by the index
# we start counting the index at 0. Meaning the last element is the length - 1
array = [4, 5, 2, 10]
print("index[0] of array:", array[0])     # index: 0 corresponds to the number 4


# =========== important functions =================

# len(array_name) returns the length of the array. (how many elements are in it)
print("length of the array:", len(array))   # returns 4

# array_name.append(element)  adds the element at the end of the array
array.append(6)
print("after array.append(6):", array)        # array = [4, 5, 2, 10, 6]

# array_name.pop()  deletes the last element of the list
array.pop()
print("after array.pop():", array)

# array.index(element)  returns the index of the element. That can be used as a find function
index_of_5 = array.index(5)
print("index of 5: index", index_of_5)

# array.sort()  Array will be sorted
array.sort()
print("sorted array:", array)

# array.insert(index, element)  Will insert the element at the index
array.insert(3, 16)     # insert at index: 3 the number 16
print("after array.insert(3, 16):", array)

# ============ working with Arrays ====================
# We can Loop through an Array  in two Ways
# The first ways should not be new, if you have understood 03_Loops and how to access the data in an Array
Data = [1, 2, 4, 5, 2, 3]
print("the first Loop method:")
for i in range(0, len(Data)):
    print("Data:", Data[i])

# The Second Method: (new)
# this method allows to write cleaner and more understandable code
# our variable Data_point will take the value of the list, from left to right.
print("the Second Loop method:")
for Data_point in Data:
    print("Data:", Data_point)
# a way to under stand is that "for Data_point = each element in Data:"

# ============ String as Array ===================
# the same is also possible in strings, as they are also Arrays with characters
# ["H", "e", "l", "l", "o", ...., "d"]
print("for Loop through Word ('Hello World'):")
Word = "Hello World"
for character in Word:
    print("Char in Word:", character)

