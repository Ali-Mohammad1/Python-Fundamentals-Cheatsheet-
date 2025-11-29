print("=======================================================================")
print("📌 Section 1: Keywords and Initialization (Starts on line 3, ends on line 7)")
print("=======================================================================\n")

# Display a list of all built-in keywords
help("keywords") 
print("_" * 30)
print("\n")


print("=======================================================================")
print("📌 Section 2: Numeric Data Operations (Starts on line 15, ends on line 38)")
print("=======================================================================\n")

# Assigning integer variables
int_a, int_b, int_c = 1000, 200, 300

# Complex number example (k = real + imaginary*j)
complex_num_k = 6 + 8j
print(type(complex_num_k)) # Output the data type of the variable
print(f"Imaginary part: {complex_num_k.imag}") # Access and print the imaginary part (8.0)
print(f"Real part: {complex_num_k.real}") # Access and print the real part (6.0)

# Basic arithmetic operation
print(int_a * 2)
print(int_b)

# Standard and format specification for floats
# :f => float (displays all available decimal places)
# :.1f => float with 1 decimal place
print(f"Float format (default precision): {int_a:f}")
print(f"Float format (1 decimal place): {int_b:.1f}")


print("=======================================================================")
print("📌 Section 3: String Formatting (Starts on line 47, ends on line 71)")
print("=======================================================================\n")

# Examples of number and string formatting with f-strings
large_number_n = 867667
sample_string_s = "pythoncode"
float_value_v = 5755.888877

print("--- Integer Formatting ---")
print(f"With comma as thousands separator: {large_number_n:,}")
print(f"With underscore as thousands separator: {large_number_n:_}")
print(f"With underscore (d specifier is optional for integers): {large_number_n:_d}")
print("_" * 10)

print("--- String Formatting ---")
# :.2s => truncate string to 2 characters
print(f"String truncated to 2 chars: {sample_string_s:.2s}")
# :.5s => truncate string to 5 characters
print(f"String truncated to 5 chars: {sample_string_s:.5s}")
print("_" * 10)

print("--- Float Formatting ---")
# :.2f => float with 2 decimal places (rounds)
print(f"Float formatted to 2 decimals: {float_value_v:.2f}")
# :.5f => float with 5 decimal places (rounds)
print(f"Float formatted to 5 decimals: {float_value_v:.5f}")
print(f"Original float value: {float_value_v}")
print("_" * 10)


print("=======================================================================")
print("📌 Section 4: Escape Sequences (Starts on line 76, ends on line 100)")
print("=======================================================================\n")

# Escape Sequences Examples
print("--- Escape Sequences ---")
# \b Backspace: Deletes the character before it (often prints as a box or not at all in some consoles)
print("hello\bworld") 
# \\ Backslash: Prints a literal backslash
print("user\\")
# Implicit string concatenation and line breaking with a backslash
print("Line 1 \
line 2 \
line 3")
# Multi-line string with triple quotes and quotes escaping
print("""First line \\\\
'Second line'\\
"Third line" """)
# Escaping double quote within double quotes
print("I love \"Python\"")
# Single quotes can contain double quotes without escaping
print('I love "Python"')
# \r Carriage Return: Moves cursor to the start of the line and overwrites.
# Output: abcd56
print("123456\rabcd") 
# \t Tab: Inserts a horizontal tab
print("Item\tQuantity")
print("_" * 10)

# String concatenation with line breaks
line_one = "Part \
A \
Complete"
line_two = "X \
Y \
Z"
print(line_one + "\n" + line_two)
print("__________________________\n ")


print("=======================================================================")
print("📌 Section 5: List Operations (Starts on line 106, ends on line 144)")
print("=======================================================================\n")

print("LISTS".center(13,"*"))
print(" ")

# Initializing lists with different data types
numbers_h = [100, 6, 5, -10, 48, 20]
numbers_k = [80, 6, 8, 90]
numbers_s = [10, 8, 9, 3, 5, 6, 7]
chars_d = ["a", "b", "c", "d"]
chars_f = ["e", "f", "g", "h"]

# Slice assignment: Replaces a range of elements (s[0] to s[2]) with new elements.
# The length of the replacement doesn't need to match the sliced length.
numbers_s[0:3] = "a", "b"
print(f"After slice assignment: {numbers_s}")

print("--- APPEND ---".center(10,"*"))
# append(): Adds the *entire* argument as a single element to the end of the list.
chars_f.append(chars_d)
print(f"List 'chars_f' after append: {chars_f}")

print("--- EXTEND ---".center(10,"*"))
# extend(): Adds elements of an iterable (e.g., another list) to the end of the current list.
chars_d.extend(numbers_s)
print(f"List 'chars_d' after extend: {chars_d}")

print("*** sort(reverse=True or False) ***")
# sort(reverse=True): Sorts the list in descending order (in-place modification)
numbers_h.sort(reverse=True)
print(f"Descending sort: {numbers_h}")
# sort(reverse=False): Sorts the list in ascending order
numbers_h.sort(reverse=False)
print(f"Ascending sort: {numbers_h}")
# sort() default is ascending
numbers_h.sort()
print(f"Default sort(): {numbers_h}")

print("--- CLEAR ---".center(9,"*"))
# clear(): Removes all elements from the list.
numbers_k.clear()
print(f"List 'numbers_k' after clear: {numbers_k}")

print("--- COPY ---".center(8,"*"))
# copy(): Creates a shallow copy of the list.
list_p = numbers_s.copy()
print(f"List 'list_p' (copy of numbers_s): {list_p}")
print("_________________________\n ")


print("=======================================================================")
print("📌 Section 6: Tuple Operations (Starts on line 147, ends on line 186)")
print("=======================================================================\n")

print("TUPLES".center(14,"*"))
print(" ")

# Tuples are immutable, but new tuples can be created through concatenation
tuple_k = (1, 2, 3, 4, 5, 5)
tuple_p = (0, 10, 20)

print("*** Concatenation (a += b) ***")
# tuple_k = tuple_k + tuple_p (This creates a *new* tuple)
tuple_k += tuple_p
print(f"Tuple 'tuple_k' after concatenation: {tuple_k}")

print("*** Concatenation (a = b + c + d) ***")
tuple_ll = ("user1", "user2")
# Concatenating multiple tuples
tuple_m = tuple_k + tuple_ll + (9, 7)
print(f"Tuple 'tuple_m' from multiple concatenations: {tuple_m}")

print("*** count() ***")
# count(): Returns the number of times a specified value occurs in a tuple.
print(f"Count of 5 in tuple_k: {tuple_k.count(5)}")

print("*** index() ***")
# index(): Searches for the first occurrence of a value and returns its index.
print(f"Index of 10 in tuple_p: {tuple_p.index(10)}")

print("*** Tuple Unpacking (a,b,c = (1,2,3)) ***")
# Unpacking elements into individual variables
tuple_o = (100, 200, 300)
var_v, var_r, var_y = tuple_o
print(f"Unpacked var_v: {var_v}")
print(f"Unpacked var_r: {var_r}")
print(f"Unpacked var_y: {var_y}")

print("*** Partial Unpacking with Placeholder (a,b,c,_ = (1,2,3,4)) ***")
# Unpacking multiple elements, using '_' as a variable placeholder for a value we don't need
tuple_me = (400, 500, 600, 700)
var_z, var_t, _, var_q = tuple_me
print(f"Unpacked var_z: {var_z}")
print(f"Unpacked var_t: {var_t}")
print(f"Unpacked var_q: {var_q}")
print(f"Placeholder variable (_): {_}")
print("_________________________\n ")


print("=======================================================================")
print("📌 Section 7: Set Operations (Starts on line 189, ends on line 282)")
print("=======================================================================\n")

print("**** SETS ****")
print(" ")
# Sets are unordered collections of unique elements (no duplicates), and do not support indexing or slicing.

print("*** clear() ***")
set_s = {1, 3, 5, 8}
set_s.clear()
print(f"Set 'set_s' after clear: {set_s}")

print("*** union() ***")
set_ds = {8, 7, 0, 4}
set_fs = {9, 1, 3, 2}
# union(): Returns a new set containing all items from both sets (set_ds | set_fs)
print(f"Union of sets: {set_ds.union(set_fs)}")

print("*** add() ***")
# add(): Adds a single element to the set.
set_ds.add("new_item")
print(f"Set 'set_ds' after add: {set_ds}")

print("*** copy() ***")
# copy(): Creates a shallow copy of the set.
set_ii = set_fs.copy()
print(f"Set 'set_ii' (copy of set_fs): {set_ii}")

print("*** remove() ***")
# remove(): Removes the specified element. **Raises a KeyError if the element is not found.**
set_fs.remove(2)
print(f"Set 'set_fs' after remove(2): {set_fs}")

print("*** discard() ***")
# discard(): Removes the specified element. **Does nothing if the element is not found (no error).**
set_pp = {9, "j_item", 10.4, 90, 60}
set_pp.discard("j_item")
print(f"Set 'set_pp' after discard('j_item'): {set_pp}")

print("*** pop() ***")
# pop(): Removes and returns an arbitrary element from the set (sets are unordered).
print(f"Random element popped from set_pp: {set_pp.pop()}")

print("*** update() ***")
# update(): Adds elements from an iterable (or multiple iterables) to the set.
set_kk = {"Project"}
set_pp.update("DEV") # Adds D, E, V as separate elements
set_pp.update(["javascript_lib"])
set_pp.update([100, 50.5])
set_pp.update(set_kk)
print(f"Set 'set_pp' after update: {set_pp}")

print("*** difference() / difference_update() ***")
set_a = {10, 20}
set_b = {20, 30}
# difference(): Returns a NEW set with items from 'a' that are NOT in 'b' (a - b)
print(f"Difference (a - b): {set_a.difference(set_b)}")
set_c = {70, 40}
# difference_update(): Removes the items from the original set 'c' that are also included in 'a'.
set_c.difference_update(set_a)
print(f"Set 'set_c' after difference_update(a): {set_c}")

print("*** intersection() / intersection_update() ***")
set_cc = {"x_key", 6, 8}
set_ccc = {"x_key", 9, 6, 7, 4}
set_bb = {9, 6}
# intersection(): Returns a NEW set with only the items present in both sets (a & b)
print(f"Intersection of (cc & ccc): {set_cc.intersection(set_ccc)}")
# intersection_update(): Keeps only the items in 'ccc' that are also in 'bb'.
set_ccc.intersection_update(set_bb)
print(f"Set 'set_ccc' after intersection_update(bb): {set_ccc}")

print("*** symmetric_difference() / symmetric_difference_update() ***")
# Returns a NEW set with items that are present in EITHER set, but NOT in both (exclusive OR).
set_j = {"zero", "ItemA", 80}
set_jj = {"one", 80, "zero", "ItemB"}
set_jjj = {"one", 80, "ItemC", 90, 2}
# symmetric_difference(): (jj ^ j)
print(f"Symmetric difference (jj ^ j): {set_jj.symmetric_difference(set_j)}")
# symmetric_difference_update(): Updates 'jj' with the exclusive items.
set_jj.symmetric_difference_update(set_jjj)
print(f"Set 'set_jj' after symmetric_difference_update(jjj): {set_jj}")

print("*** issuperset() / issubset() ***")
set_o = {1, 2, 3, 4}
set_oo = {1, 2, 3}
# o.issuperset(oo): True if all elements of 'oo' are in 'o'.
print(f"o.issuperset(oo): {set_o.issuperset(set_oo)}") # True
# oo.issuperset(o): False if 'o' has elements 'oo' doesn't.
print(f"oo.issuperset(o): {set_oo.issuperset(set_o)}") # False

# oo.issubset(o): True if all elements of 'oo' are in 'o'.
print(f"oo.issubset(o): {set_oo.issubset(set_o)}") # True
# o.issubset(oo): False if 'o' has elements 'oo' doesn't.
print(f"o.issubset(oo): {set_o.issubset(set_oo)}") # False

print("*** isdisjoint() ***")
# isdisjoint(): Returns True if the sets have NO items in common (their intersection is empty).
set_f = {1, 2, 3}
set_ff = {1, 2, 3, 4, 5}
set_fff = {6, 7, 8}
# False because they share elements (1, 2, 3)
print(f"f.isdisjoint(ff): {set_f.isdisjoint(set_ff)}")
# True because they share no elements
print(f"f.isdisjoint(fff): {set_f.isdisjoint(set_fff)}")
print("__________________________ \n ")


print("=======================================================================")
print("📌 Section 8: Dictionary Operations (Starts on line 285, ends on line 386)")
print("=======================================================================\n")

print("DICTIONARIES".center(20,"*"))
print(" ")
# Dictionaries are collections of key:value pairs. Keys must be unique and immutable (e.g., strings, numbers, tuples).

dictionary_data_1 = {"name": "UserA", "age": 25, "number": (1, 2), "float": 10.5}
dictionary_data_2 = {"number1": [3, 4]}
# Tuple can be a key, List cannot be a key (since lists are mutable)
dictionary_data_3 = {"number2": (5, 6), (7, 8): "number3"} 

print("*** keys() / values() ***")
# keys(): Returns a view object that displays a list of all the keys.
print(f"Keys of dictionary_data_1: {dictionary_data_1.keys()}")
# values(): Returns a view object that displays a list of all the values.
print(f"Values of dictionary_data_1: {dictionary_data_1.values()}")

print("*** Accessing Values (Slicing/Indexing) ***")
# Accessing value using bracket notation (key)
print(f"Value for 'name': {dictionary_data_1['name']}")
# Accessing value using get() method
print(f"Value for 'age': {dictionary_data_1.get('age')}")

print("*** get() with Default Value ***")
# get(): Returns the value for the key. If the key is not found, returns None or the specified default value.
print(f"Value for (7, 8): {dictionary_data_3.get((7, 8), 'Key not found')}")
print(f"Value for 'non_existent_key': {dictionary_data_1.get('non_existent_key', 'Key not found')}")
print("_________")

print("--- Nested Dictionaries ---")
# Dictionaries within dictionaries
project_languages = {
 "module_one": {"name": "HTML"},
  "module_two": {"name": "C++"}
}

# Accessing a nested dictionary
print(f"Accessing 'module_one' dictionary: {project_languages.get('module_one')}")
# Accessing a value deep in the nested structure
print(f"Accessing 'name' in 'module_two': {project_languages['module_two']['name']}")

# Length of the main dictionary (number of key:value pairs)
print(f"Length of project_languages: {len(project_languages)}")
# Length of a nested dictionary
print(f"Length of nested 'module_one': {len(project_languages['module_one'])}")

# Dictionary containing other dictionaries
all_data_dictionaries = {"1": dictionary_data_1, "2": dictionary_data_2}
print(f"Dictionary of dictionaries: {all_data_dictionaries}")

print("*** clear() ***")
user_profile = {"name": "UserB"}
print(f"Original user_profile: {user_profile}")
user_profile.clear()
print(f"user_profile after clear: {user_profile}")

print("*** update({key : value}) ***")
# update(): Adds item(s) to the dictionary.
user_profile.update({"year": 2008})
# Adding/modifying using bracket notation
user_profile["age"] = 25
print(f"user_profile after update: {user_profile}")

print("*** copy() ***")
# copy(): Creates a shallow copy.
copied_profile = user_profile.copy()
user_profile.update({"age": 26}) # Change in user_profile does not affect copied_profile
print(f"Copied profile: {copied_profile}")
print(f"Original user_profile: {user_profile}")

print("*** setdefault(key , value) ***")
# setdefault(): Inserts key with value if key is NOT in the dictionary. If key IS present, it returns the current value and does nothing.
temp_dict = {}
# Key 'age' is NOT present, so it's added
temp_dict.setdefault("age", 30)
# Key 'year' is NOT present, default value is None
temp_dict.setdefault("year")
print(f"temp_dict after setdefault: {temp_dict}")

print("*** popitem() ***")
# popitem(): Removes and returns the last inserted key/value pair (since Python 3.7, dictionaries are ordered).
temp_dict.update({"name_key": "ValueX"})
print(f"popitem() returns the last inserted item: {temp_dict.popitem()}")

print("*** items() ***")
# items(): Returns a view object that displays a list of a dictionary's key-value tuple pairs.
items_view = temp_dict.items()
temp_dict["os_key"] = "Linux" # The view object is dynamic and reflects changes
print(f"temp_dict.items() view object: {temp_dict.items()}")
print(f"Previous items_view reference: {items_view}")

print("*** dict.fromkeys() ***")
keys_tuple = ("key1", "key2")
default_value_b = "default_value"
single_value_cm = 10
# Creates a dictionary with keys from keys_tuple, all assigned default_value_b
print(f"dict.fromkeys(keys_tuple, default_value_b): {dict.fromkeys(keys_tuple, default_value_b)}")
# Using a single character from the tuple as key (it's iterable)
print(f"dict.fromkeys(keys_tuple[0], single_value_cm): {dict.fromkeys(keys_tuple[0], single_value_cm)}")

print("*** del statement ***")
temp_dict_mm = {1: "value_j", 2: "value_k"}
# del key: Removes the specified key-value pair.
del temp_dict_mm[1]
print(f"temp_dict_mm after del key 1: {temp_dict_mm}")
# del dictionary: Completely deletes the dictionary object from memory.
# del temp_dict_mm 
# print(temp_dict_mm) # Would result in a NameError

print("*** pop(key, default) ***")
# pop(): Removes the item with the specified key and returns its value. 
# Second argument is an optional default value to return if the key is not found (avoids KeyError).
temp_dict_lo = {1: 2, 2: 4, 3: 6, 4: 8}
# Removes key 1, ignores the optional value (None)
temp_dict_lo.pop(1, None)
# Removes key 4, ignores the optional value (8)
temp_dict_lo.pop(4, 8)
print(f"temp_dict_lo after pop: {temp_dict_lo}")
print("_________________________")


print("=======================================================================")
print("📌 Section 9: Boolean Logic and Type Casting (Starts on line 390, ends on line 492)")
print("=======================================================================\n")

print("**** BOOLEAN ****")
print("*** bool() Type Casting ***")

print("--- True values ---")
# Any non-empty string
print(f"bool(' '): {bool(' ')}")
# Any non-zero number
print(f"bool(100): {bool(100)}")
print(f"bool(1.5): {bool(1.5)}")
print(f"bool(True): {bool(True)}")
# Any non-empty sequence/collection (list, tuple, dictionary, set)
print(f"bool([1, 2]): {bool([1, 2])}")
print(f"bool((1, 3)): {bool((1, 3))}")
print(f"bool({{1: 2}}): {bool({1: 2})}")
print(f"bool({{1, 2}}): {bool({1, 2})}")

print("--- False values ---")
# Zero (integer or float)
print(f"bool(0): {bool(0)}")
# Empty strings
print(f"bool(''): {bool('')}")
print(f"bool(\"\"): {bool('')}")
# Boolean False
print(f"bool(False): {bool(False)}")
# None value
print(f"bool(None): {bool(None)}")

print("*** Logical Operators (and, or, not) ***")
age_val = 25
country_val = "canada"
rank_val = 10

print("--- First (and) ---")
# 'and': True if BOTH operands are True.
print(f"age_val == 25 and country_val == 'canada': {age_val == 25 and country_val == 'canada'}")
print(f"age_val == 25 and country_val != 'USA': {age_val == 25 and country_val != 'USA'}")
print(f"Complex 'and' check: {age_val < 30 and country_val == 'canada' and rank_val < 20}")
print(f"False 'and' check: {age_val == 25 and country_val == 'usa'}") # False because country is 'canada'

print("--- Second (or) ---")
# 'or': True if AT LEAST ONE operand is True.
print(f"age_val == 25 or country_val == 'usa' or rank_val == 90: {age_val == 25 or country_val == 'usa' or rank_val == 90}") # True
print(f"False 'or' check: {age_val == 60 or rank_val == 3}") # False

print("--- Third (not) ---")
# 'not': Inverts the boolean result (not True = False, not False = True).
print(f"not (age_val == 13): {not age_val == 13}") # not False = True
print(f"not (rank_val == 10): {not rank_val == 10}") # not True = False

print("\n*** Arithmetic, Assignment, and Comparison Operators ***")
print("Assignment Operators: = , += , -= , *= , /= , //= , %= , **= (power)")
print("Comparison Operators: == , >= , <= , != , < , > ")

print("\n**** Type Casting Functions (str(), int(), float(), list(), set(), tuple(), dict()) ****")
# Casting a string into other sequence types
print(f"list('User'): {list('User')}", "-> list")
print(f"set('User'): {set('User')}", "-> set (removes duplicates, unordered)")
print(f"tuple('User'): {tuple('User')}", "-> tuple")
print("========")

list_ab1 = [1, 2, 3, 4]
tuple_ab2 = (4, 5, 6, 7)
set_ab3 = {8, 9, 10, 11}
dict_ab4 = {12: 2, 13: 4, 14: 6}

print("--- Casting to TUPLE ---")
print(f"tuple(list): {tuple(list_ab1)}")
print(f"tuple(tuple): {tuple(tuple_ab2)}")
print(f"tuple(set): {tuple(set_ab3)}")
# When casting a dictionary to a sequence, only the KEYS are kept.
print(f"tuple(dictionary): {tuple(dict_ab4)}")
print("------")

print("--- Casting to LIST ---")
print(f"list(list): {list(list_ab1)}")
print(f"list(tuple): {list(tuple_ab2)}")
print(f"list(set): {list(set_ab3)}")
# Only keys are kept from the dictionary
print(f"list(dictionary): {list(dict_ab4)}")
print("------")

print("--- Casting to SET ---")
print(f"set(list): {set(list_ab1)}")
print(f"set(tuple): {set(tuple_ab2)}")
print(f"set(set): {set(set_ab3)}")
# Only keys are kept from the dictionary
print(f"set(dictionary): {set(dict_ab4)}")
print(" ")

print("-- dict() Casting --")
print("dict() only accepts iterables where each element is a key-value pair (e.g., a tuple of two items).")
print("It will NOT work with a flat set/tuple/list of single values.")
print(" ")

# Example 1: Tuple of key-value tuples
tuple_a1 = (("A", 1), ("B", 2), ("C", 3))
print(f"Original: {tuple_a1}")
print(f"dict(nested tuple): {dict(tuple_a1)}")
print(" \n ")

# Example 2: List of key-value lists
list_a2 = [["D", 4], ["E", 5], ["F", 6]]
print(f"Original: {list_a2}")
print(f"dict(nested list): {dict(list_a2)}")
print(" \n ")

# Example 3: Mixed list of tuples and lists (as long as each sub-element has 2 items)
list_a3 = [(4, 7), [9, 7]]
print(f"Original: {list_a3}")
print(f"dict(mixed list): {dict(list_a3)}")
print(" ")

# Example 4: Tuple of mixed list and tuple
tuple_a4 = ([8, 9], (0, 1))
print(f"Original: {tuple_a4}")
print(f"dict(mixed tuple): {dict(tuple_a4)}")

print("=======================================================================")
print("📌 End of Code")
print("=======================================================================")