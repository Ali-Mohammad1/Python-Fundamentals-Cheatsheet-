import keyword

# ============================================================================
# SECTION 1: KEYWORDS AND INITIALIZATION
# ============================================================================
print("=======================================================================")
print("Section 1: Keywords and Initialization")
print("=======================================================================\n")

# Display all reserved keywords in Python
print("Python keywords:", keyword.kwlist)
print("_" * 30)
print("\n")


# ============================================================================
# SECTION 2: NUMERIC DATA OPERATIONS
# ============================================================================
print("=======================================================================")
print("Section 2: Numeric Data Operations")
print("=======================================================================\n")

# Integer variables - multiple assignment in one line
val_a, val_b, val_c = 1000, 200, 300

# Complex numbers (real + imaginary part)
complex_num = 6 + 8j
print(type(complex_num))                # <class 'complex'>
print(f"Imaginary part: {complex_num.imag}")   # 8.0
print(f"Real part: {complex_num.real}")        # 6.0

# Basic arithmetic
print(val_a * 2)        # 2000
print(val_b)            # 200

# Float formatting with f-strings
print(f"Float format (default): {val_a:f}")       # 1000.000000
print(f"Float format (1 decimal): {val_b:.1f}")   # 200.0


# ============================================================================
# SECTION 3: STRING FORMATTING
# ============================================================================
print("=======================================================================")
print("Section 3: String Formatting")
print("=======================================================================\n")

large_number = 867667
sample_text = "pythoncode"
float_val = 5755.888877

print("--- Integer Formatting ---")
print(f"Thousands separator (comma): {large_number:,}")          # 867,667
print(f"Thousands separator (underscore): {large_number:_}")     # 867_667
print(f"Underscore with d specifier: {large_number:_d}")
print("_" * 10)

print("--- String Truncation ---")
print(f"First 2 characters: {sample_text:.2s}")     # py
print(f"First 5 characters: {sample_text:.5s}")     # pytho
print("_" * 10)

print("--- Float Rounding ---")
print(f"Rounded to 2 decimals: {float_val:.2f}")    # 5755.89
print(f"Rounded to 5 decimals: {float_val:.5f}")    # 5755.88888
print(f"Original value: {float_val}")
print("_" * 10)


# ============================================================================
# SECTION 4: ESCAPE SEQUENCES
# ============================================================================
print("=======================================================================")
print("Section 4: Escape Sequences")
print("=======================================================================\n")

print("--- Escape Sequences Demonstration ---")
print("Backspace: hello\bworld")          # Removes 'o' before 'w'
print("Backslash: user\\")
print("Line continuation: Line 1 \
line 2 \
line 3")                                 # Multi-line string without newline
print("Triple quotes with escapes: \"\"\"First line \\\\\n'Second line'\\\n\"Third line\" \"\"\"")
print("Escaped double quotes: I love \"Python\"")
print("Single quotes containing double quotes: I love \"Python\"")
print("Carriage return: 123456\rabcd")   # Overwrites first 4 chars with 'abcd'
print("Tab: Item\tQuantity")
print("_" * 10)

# String concatenation with line continuation
part1 = "Part A \
Complete"          # Joins without newline
part2 = "X Y Z"
print(part1 + "\n" + part2)
print("__________________________\n ")


# ============================================================================
# SECTION 5: LIST OPERATIONS
# ============================================================================
print("=======================================================================")
print("Section 5: List Operations")
print("=======================================================================\n")

print("LISTS".center(13, "*"))
print(" ")

# Initialize several lists
nums_1 = [100, 6, 5, -10, 48, 20]
nums_2 = [80, 6, 8, 90]
nums_3 = [10, 8, 9, 3, 5, 6, 7]
chars_a = ["a", "b", "c", "d"]
chars_b = ["e", "f", "g", "h"]

# Slice assignment: replace a slice with new elements (can be different length)
nums_3[0:3] = "a", "b"
print(f"After slice assignment: {nums_3}")          # ['a', 'b', 9, 3, 5, 6, 7]

print("--- APPEND ---".center(10, "*"))
# append() adds its argument as a single element
chars_b.append(chars_a)
print(f"chars_b after append: {chars_b}")           # Adds entire list as one element

print("--- EXTEND ---".center(10, "*"))
# extend() adds each element of the iterable individually
chars_a.extend(nums_3)
print(f"chars_a after extend: {chars_a}")           # Flattens nums_3 into chars_a

print("*** sort(reverse=True or False) ***")
nums_1.sort(reverse=True)
print(f"Descending sort: {nums_1}")                 # [100, 48, 20, 6, 5, -10]
nums_1.sort(reverse=False)
print(f"Ascending sort: {nums_1}")                  # [-10, 5, 6, 20, 48, 100]
nums_1.sort()                                       # Default ascending
print(f"Default sort(): {nums_1}")

print("--- CLEAR ---".center(9, "*"))
# clear() removes all elements
nums_2.clear()
print(f"nums_2 after clear: {nums_2}")              # []

print("--- COPY ---".center(8, "*"))
# copy() creates a shallow copy
list_copy = nums_3.copy()
print(f"list_copy (copy of nums_3): {list_copy}")
print("_________________________\n ")


# ============================================================================
# SECTION 6: TUPLE OPERATIONS
# ============================================================================
print("=======================================================================")
print("Section 6: Tuple Operations")
print("=======================================================================\n")

print("TUPLES".center(14, "*"))
print(" ")

# Tuples are immutable, but can be concatenated
tup_1 = (1, 2, 3, 4, 5, 5)
tup_2 = (0, 10, 20)

print("*** Concatenation (a += b) ***")
tup_1 += tup_2                                    # Creates a new tuple
print(f"tup_1 after concatenation: {tup_1}")      # (1,2,3,4,5,5,0,10,20)

print("*** Concatenation (a = b + c + d) ***")
tup_3 = ("user1", "user2")
tup_4 = tup_1 + tup_3 + (9, 7)
print(f"tup_4 from multiple concatenations: {tup_4}")

print("*** count() ***")
print(f"Count of 5 in tup_1: {tup_1.count(5)}")   # 2 (two 5's)

print("*** index() ***")
print(f"Index of 10 in tup_2: {tup_2.index(10)}") # 1

print("*** Tuple Unpacking ***")
tup_unpack = (100, 200, 300)
x, y, z = tup_unpack
print(f"Unpacked x: {x}, y: {y}, z: {z}")

print("*** Partial Unpacking with Placeholder ***")
tup_place = (400, 500, 600, 700)
a, b, _, c = tup_place
print(f"Unpacked a: {a}, b: {b}, c: {c}")
print(f"Placeholder (_): {_}")
print("_________________________\n ")


# ============================================================================
# SECTION 7: SET OPERATIONS
# ============================================================================
print("=======================================================================")
print("Section 7: Set Operations")
print("=======================================================================\n")

print("**** SETS ****")
print(" ")

# Sets are unordered, unique elements; no indexing
set_empty = {1, 3, 5, 8}
set_empty.clear()
print(f"set_empty after clear: {set_empty}")

set_first = {8, 7, 0, 4}
set_second = {9, 1, 3, 2}
print(f"Union (first | second): {set_first.union(set_second)}")   # {0,1,2,3,4,7,8,9}

set_first.add("new_item")
print(f"set_first after add: {set_first}")

set_copy = set_second.copy()
print(f"set_copy (copy of set_second): {set_copy}")

set_second.remove(2)
print(f"set_second after remove(2): {set_second}")                 # remove() raises error if missing

set_sample = {9, "j_item", 10.4, 90, 60}
set_sample.discard("j_item")
print(f"set_sample after discard('j_item'): {set_sample}")         # discard() does nothing if missing

print(f"Random pop from set_sample: {set_sample.pop()}")           # removes arbitrary element

set_proj = {"Project"}
set_sample.update("DEV")                     # adds D, E, V
set_sample.update(["javascript_lib"])
set_sample.update([100, 50.5])
set_sample.update(set_proj)
print(f"set_sample after multiple updates: {set_sample}")

set_a = {10, 20}
set_b = {20, 30}
print(f"Difference (a - b): {set_a.difference(set_b)}")            # {10}
set_c = {70, 40}
set_c.difference_update(set_a)              # removes any element found in set_a
print(f"set_c after difference_update: {set_c}")

set_one = {"x_key", 6, 8}
set_two = {"x_key", 9, 6, 7, 4}
set_three = {9, 6}
print(f"Intersection (one & two): {set_one.intersection(set_two)}") # {'x_key', 6}
set_two.intersection_update(set_three)
print(f"set_two after intersection_update: {set_two}")

set_j1 = {"zero", "ItemA", 80}
set_j2 = {"one", 80, "zero", "ItemB"}
set_j3 = {"one", 80, "ItemC", 90, 2}
print(f"Symmetric difference (j2 ^ j1): {set_j2.symmetric_difference(set_j1)}")
set_j2.symmetric_difference_update(set_j3)
print(f"set_j2 after symmetric_difference_update: {set_j2}")

set_m = {1, 2, 3, 4}
set_n = {1, 2, 3}
print(f"m superset of n? {set_m.issuperset(set_n)}")        # True
print(f"n superset of m? {set_n.issuperset(set_m)}")        # False
print(f"n subset of m? {set_n.issubset(set_m)}")            # True
print(f"m subset of n? {set_m.issubset(set_n)}")            # False

set_x = {1, 2, 3}
set_y = {1, 2, 3, 4, 5}
set_z = {6, 7, 8}
print(f"x disjoint with y? {set_x.isdisjoint(set_y)}")      # False (share elements)
print(f"x disjoint with z? {set_x.isdisjoint(set_z)}")      # True
print("__________________________ \n ")


# ============================================================================
# SECTION 8: DICTIONARY OPERATIONS
# ============================================================================
print("=======================================================================")
print("Section 8: Dictionary Operations")
print("=======================================================================\n")

print("DICTIONARIES".center(20, "*"))
print(" ")

# Dictionaries store key-value pairs
dict_person = {"name": "UserA", "age": 25, "number": (1, 2), "float": 10.5}
dict_extra = {"number1": [3, 4]}
dict_special = {"number2": (5, 6), (7, 8): "number3"}

print("*** keys() / values() ***")
print(f"Keys: {dict_person.keys()}")
print(f"Values: {dict_person.values()}")

print("*** Accessing Values ***")
print(f"dict_person['name']: {dict_person['name']}")
print(f"dict_person.get('age'): {dict_person.get('age')}")

print("*** get() with Default Value ***")
print(f"dict_special.get((7,8), 'Not found'): {dict_special.get((7,8), 'Not found')}")
print(f"dict_person.get('missing', 'Default'): {dict_person.get('missing', 'Default')}")
print("_________")

print("--- Nested Dictionaries ---")
projects = {
    "module_one": {"name": "HTML"},
    "module_two": {"name": "C++"}
}
print(f"Access nested dict: {projects.get('module_one')}")
print(f"Access deeper: {projects['module_two']['name']}")
print(f"Length of projects: {len(projects)}")
print(f"Length of nested 'module_one': {len(projects['module_one'])}")

all_dicts = {"first": dict_person, "second": dict_extra}
print(f"Dictionary of dictionaries: {all_dicts}")

print("*** clear() ***")
profile = {"name": "UserB"}
print(f"Original profile: {profile}")
profile.clear()
print(f"After clear: {profile}")

print("*** update() ***")
profile.update({"year": 2008})
profile["age"] = 25
print(f"After update: {profile}")

print("*** copy() ***")
profile_copy = profile.copy()
profile["age"] = 26
print(f"Copied profile: {profile_copy}")       # unchanged
print(f"Original profile: {profile}")          # changed

print("*** setdefault() ***")
temp = {}
temp.setdefault("age", 30)      # adds key 'age' with value 30
temp.setdefault("year")          # adds key 'year' with value None
print(f"temp after setdefault: {temp}")

print("*** popitem() ***")
temp.update({"name_key": "ValueX"})
print(f"popitem removes last item: {temp.popitem()}")

print("*** items() ***")
items_view = temp.items()
temp["os_key"] = "Linux"
print(f"items view (dynamic): {temp.items()}")
print(f"Previous items view also reflects change: {items_view}")

print("*** dict.fromkeys() ***")
keys = ("key1", "key2")
print(f"fromkeys with default: {dict.fromkeys(keys, 'default_val')}")
print(f"fromkeys with single char: {dict.fromkeys(keys[0], 10)}")

print("*** del statement ***")
temp_dict = {1: "val1", 2: "val2"}
del temp_dict[1]
print(f"After del key 1: {temp_dict}")

print("*** pop(key, default) ***")
temp_lo = {1: 2, 2: 4, 3: 6, 4: 8}
temp_lo.pop(1)                  # removes key 1
temp_lo.pop(4, 8)               # removes key 4, returns 8 if not found (found)
print(f"After pop: {temp_lo}")
print("_________________________")


# ============================================================================
# SECTION 9: BOOLEAN LOGIC AND TYPE CASTING
# ============================================================================
print("=======================================================================")
print("Section 9: Boolean Logic and Type Casting")
print("=======================================================================\n")

print("**** BOOLEAN ****")
print("*** bool() Type Casting ***")

print("--- Truthy values ---")
print(f"bool(' '): {bool(' ')}")             # non-empty string -> True
print(f"bool(100): {bool(100)}")             # non-zero number -> True
print(f"bool(1.5): {bool(1.5)}")             # non-zero float -> True
print(f"bool(True): {bool(True)}")
print(f"bool([1,2]): {bool([1,2])}")         # non-empty list -> True
print(f"bool((1,3)): {bool((1,3))}")         # non-empty tuple -> True
print(f"bool({{1:2}}): {bool({1:2})}")       # non-empty dict -> True
print(f"bool({{1,2}}): {bool({1,2})}")       # non-empty set -> True

print("--- Falsy values ---")
print(f"bool(0): {bool(0)}")
print(f"bool(''): {bool('')}")
print(f"bool(\"\"): {bool('')}")
print(f"bool(False): {bool(False)}")
print(f"bool(None): {bool(None)}")

print("*** Logical Operators ***")
age = 25
country = "canada"
rank = 10

print("--- and ---")
print(f"age == 25 and country == 'canada': {age == 25 and country == 'canada'}")
print(f"age == 25 and country != 'USA': {age == 25 and country != 'USA'}")
print(f"age < 30 and country == 'canada' and rank < 20: {age < 30 and country == 'canada' and rank < 20}")
print(f"age == 25 and country == 'usa': {age == 25 and country == 'usa'}")

print("--- or ---")
print(f"age == 25 or country == 'usa' or rank == 90: {age == 25 or country == 'usa' or rank == 90}")
print(f"age == 60 or rank == 3: {age == 60 or rank == 3}")

print("--- not ---")
print(f"not (age == 13): {not age == 13}")
print(f"not (rank == 10): {not rank == 10}")

print("\n*** Operators Summary ***")
print("Assignment: =, +=, -=, *=, /=, //=, %=, **=")
print("Comparison: ==, >=, <=, !=, <, >")

print("\n**** Type Casting Functions ****")
print(f"list('User'): {list('User')}")          # ['U','s','e','r']
print(f"set('User'): {set('User')}")            # {'U','r','s','e'} (order may vary)
print(f"tuple('User'): {tuple('User')}")        # ('U','s','e','r')
print("========")

list_ex = [1,2,3,4]
tuple_ex = (4,5,6,7)
set_ex = {8,9,10,11}
dict_ex = {12:2,13:4,14:6}

print("--- Casting to LIST ---")
print(f"list(list): {list(list_ex)}")
print(f"list(tuple): {list(tuple_ex)}")
print(f"list(set): {list(set_ex)}")
print(f"list(dict): {list(dict_ex)}")           # only keys
print("------")

print("--- Casting to SET ---")
print(f"set(list): {set(list_ex)}")
print(f"set(tuple): {set(tuple_ex)}")
print(f"set(set): {set(set_ex)}")
print(f"set(dict): {set(dict_ex)}")             # only keys
print(" ")

print("-- dict() Casting --")
print("Requires iterable of key-value pairs (e.g., list of tuples)")
pair_tup = (("A",1), ("B",2), ("C",3))
print(f"Original: {pair_tup}")
print(f"dict(pair_tup): {dict(pair_tup)}")
print(" \n ")

pair_list = [["D",4], ["E",5], ["F",6]]
print(f"Original: {pair_list}")
print(f"dict(pair_list): {dict(pair_list)}")
print(" \n ")

mixed = [(4,7), [9,7]]
print(f"Original: {mixed}")
print(f"dict(mixed): {dict(mixed)}")
print(" ")

tuple_mixed = ([8,9], (0,1))
print(f"Original: {tuple_mixed}")
print(f"dict(tuple_mixed): {dict(tuple_mixed)}")

print("=======================================================================")
print("End of Code")
print("=======================================================================")