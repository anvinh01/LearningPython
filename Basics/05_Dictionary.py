# Dictionarys (Wörtebuch)
# Working with a dictionary is similar to how you work with an Array
# Instead of calling the value by the index, as you did with the Arrays.
# You call the value by a key

# dict = {"key": "value"}
# calling: dict["key"] = "value"

# ================== initialize dictionary ==================
book_1 = {"hallo": "hello", "Kaffe": "coffe"}
book_2 = dict()

# dict = {"key" : "value"}
# calling the value by the key
string = "hallo"
print(book_1["hallo"])

# adding a new element
# dict["key"] = "value"
book_1["Schlange"] = "snake"


# it is possible to convert the dictionary into an array
# it will create a list of all keys
print(list(book_1))
# or also a list of all values
print(book_1.values())

# It is already possible to achieve a lot with this knowledge above
# but there exist functions which are very useful and some which are important

# ============= functions ===================
# pop()
# removes the element with the specified key
book_1.pop("hallo")

# .popitem()
# Removes the last inserted key-value pair
book_1.popitem()

# get()
# Returns the value of the specified key
print(book_1.get("Kaffe"))

# .clear()
# Removes all elements from the dictionary

# ================= END of 05_Dictionary ====================
