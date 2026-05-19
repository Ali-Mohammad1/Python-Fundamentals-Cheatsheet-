import keyword

print("=======================================================================")
print("📌 Section 1: Keywords and Initialization")
print("=======================================================================\n")

# Display all built-in keywords
print("Python keywords:", keyword.kwlist)
print("_" * 30)
print("\n")


print("=======================================================================")
print("📌 Section 2: Numeric Data Operations")
print("=======================================================================\n")

# Integer variables
num_a, num_b, num_c = 1000, 200, 300

# Complex number example
complex_num = 6 + 8j
print(type(complex_num))
print(f"Imaginary part: {complex_num.imag}")
print(f"Real part: {complex_num.real}")

# Basic arithmetic
print(num_a * 2)
print(num_b)

# Float formatting
print(f"Float format (default precision): {num_a:f}")
print(f"Float format (1 decimal place): {num_b:.1f}")


print("=======================================================================")
print("📌 Section 3: String Formatting")
print("=======================================================================\n")

large_number = 867667
sample_string = "pythoncode"
float_value = 5755.888877

print("--- Integer Formatting ---")
print(f"With comma as thousands separator: {large_number:,}")
print(f"With underscore as thousands separator: {large_number:_}")
print(f"With underscore (d specifier): {large_number:_d}")
print("_" * 10)

print("--- String Formatting ---")
print(f"String truncated to 2 chars: {sample_string:.2s}")
print(f"String truncated to 5 chars: {sample_string:.5s}")
print("_" * 10)

print("--- Float Formatting ---")
print(f"Float formatted to 2 decimals: {float_value:.2f}")
print(f"Float formatted to 5 decimals: {float_value:.5f}")
print(f"Original float value: {float_value}")
print("_" * 10)


print("=======================================================================")
print("📌 Section 4: Escape Sequences")
print("=======================================================================\n")

print("--- Escape Sequences ---")
print("hello\bworld")
print("user\\")
print("Line 1 \
line 2 \
line 3")
print("""First line \\\\
'Second line'\\
"Third line" """)
print("I love \"Python\"")
print('I love "Python"')
print("123456\rabcd")
print("Item\tQuantity")
print("_" * 10)

line_one = "Part \
A \
Complete"
line_two = "X \
Y \
Z"
print(line_one + "\n" + line_two)
print("__________________________\n ")


print("=======================================================================")
print("📌 Section 5: List Operations")
print("=======================================================================\n")

print("LISTS".center(13, "*"))
print(" ")

numbers_h = [100, 6, 5, -10, 48, 20]
numbers_k = [80, 6, 8, 90]
numbers_s = [10, 8, 9, 3, 5, 6, 7]
chars_d = ["a", "b", "c", "d"]
chars_f = ["e", "f", "g", "h"]

numbers_s[0:3] = "a", "b"
print(f"After slice assignment: {numbers_s}")

print("--- APPEND ---".center(10, "*"))
chars_f.append(chars_d)
print(f"List 'chars_f' after append: {chars_f}")

print("--- EXTEND ---".center(10, "*"))
chars_d.extend(numbers_s)
print(f"List 'chars_d' after extend: {chars_d}")

print("*** sort(reverse=True or False) ***")
numbers_h.sort(reverse=True)
print(f"Descending sort: {numbers_h}")
numbers_h.sort(reverse=False)
print(f"Ascending sort: {numbers_h}")
numbers_h.sort()
print(f"Default sort(): {numbers_h}")

print("--- CLEAR ---".center(9, "*"))
numbers_k.clear()
print(f"List 'numbers_k' after clear: {numbers_k}")

print("--- COPY ---".center(8, "*"))
list_p = numbers_s.copy()
print(f"List 'list_p' (copy of numbers_s): {list_p}")
print("_________________________\n ")


print("=======================================================================")
print("📌 Section 6: Tuple Operations")
print("=======================================================================\n")

print("TUPLES".center(14, "*"))
print(" ")

tuple_k = (1, 2, 3, 4, 5, 5)
tuple_p = (0, 10, 20)

print("*** Concatenation (a += b) ***")
tuple_k += tuple_p
print(f"Tuple 'tuple_k' after concatenation: {tuple_k}")

print("*** Concatenation (a = b + c + d) ***")
tuple_ll = ("user1", "user2")
tuple_m = tuple_k + tuple_ll + (9, 7)
print(f"Tuple 'tuple_m' from multiple concatenations: {tuple_m}")

print("*** count() ***")
print(f"Count of 5 in tuple_k: {tuple_k.count(5)}")

print("*** index() ***")
print(f"Index of 10 in tuple_p: {tuple_p.index(10)}")

print("*** Tuple Unpacking (a,b,c = (1,2,3)) ***")
tuple_o = (100, 200, 300)
var_v, var_r, var_y = tuple_o
print(f"Unpacked var_v: {var_v}")
print(f"Unpacked var_r: {var_r}")
print(f"Unpacked var_y: {var_y}")

print("*** Partial Unpacking with Placeholder (a,b,c,_ = (1,2,3,4)) ***")
tuple_me = (400, 500, 600, 700)
var_z, var_t, _, var_q = tuple_me
print(f"Unpacked var_z: {var_z}")
print(f"Unpacked var_t: {var_t}")
print(f"Unpacked var_q: {var_q}")
print(f"Placeholder variable (_): {_}")
print("_________________________\n ")


print("=======================================================================")
print("📌 Section 7: Set Operations")
print("=======================================================================\n")

print("**** SETS ****")
print(" ")

set_s = {1, 3, 5, 8}
set_s.clear()
print(f"Set 'set_s' after clear: {set_s}")

set_ds = {8, 7, 0, 4}
set_fs = {9, 1, 3, 2}
print(f"Union of sets: {set_ds.union(set_fs)}")

set_ds.add("new_item")
print(f"Set 'set_ds' after add: {set_ds}")

set_ii = set_fs.copy()
print(f"Set 'set_ii' (copy of set_fs): {set_ii}")

set_fs.remove(2)
print(f"Set 'set_fs' after remove(2): {set_fs}")

set_pp = {9, "j_item", 10.4, 90, 60}
set_pp.discard("j_item")
print(f"Set 'set_pp' after discard('j_item'): {set_pp}")

print(f"Random element popped from set_pp: {set_pp.pop()}")

set_kk = {"Project"}
set_pp.update("DEV")
set_pp.update(["javascript_lib"])
set_pp.update([100, 50.5])
set_pp.update(set_kk)
print(f"Set 'set_pp' after update: {set_pp}")

set_a = {10, 20}
set_b = {20, 30}
print(f"Difference (a - b): {set_a.difference(set_b)}")
set_c = {70, 40}
set_c.difference_update(set_a)
print(f"Set 'set_c' after difference_update(a): {set_c}")

set_cc = {"x_key", 6, 8}
set_ccc = {"x_key", 9, 6, 7, 4}
set_bb = {9, 6}
print(f"Intersection of (cc & ccc): {set_cc.intersection(set_ccc)}")
set_ccc.intersection_update(set_bb)
print(f"Set 'set_ccc' after intersection_update(bb): {set_ccc}")

set_j = {"zero", "ItemA", 80}
set_jj = {"one", 80, "zero", "ItemB"}
set_jjj = {"one", 80, "ItemC", 90, 2}
print(f"Symmetric difference (jj ^ j): {set_jj.symmetric_difference(set_j)}")
set_jj.symmetric_difference_update(set_jjj)
print(f"Set 'set_jj' after symmetric_difference_update(jjj): {set_jj}")

set_o = {1, 2, 3, 4}
set_oo = {1, 2, 3}
print(f"o.issuperset(oo): {set_o.issuperset(set_oo)}")
print(f"oo.issuperset(o): {set_oo.issuperset(set_o)}")
print(f"oo.issubset(o): {set_oo.issubset(set_o)}")
print(f"o.issubset(oo): {set_o.issubset(set_oo)}")

set_f = {1, 2, 3}
set_ff = {1, 2, 3, 4, 5}
set_fff = {6, 7, 8}
print(f"f.isdisjoint(ff): {set_f.isdisjoint(set_ff)}")
print(f"f.isdisjoint(fff): {set_f.isdisjoint(set_fff)}")
print("__________________________ \n ")


print("=======================================================================")
print("📌 Section 8: Dictionary Operations")
print("=======================================================================\n")

print("DICTIONARIES".center(20, "*"))
print(" ")

dict1 = {"name": "UserA", "age": 25, "number": (1, 2), "float": 10.5}
dict2 = {"number1": [3, 4]}
dict3 = {"number2": (5, 6), (7, 8): "number3"}

print("*** keys() / values() ***")
print(f"Keys of dict1: {dict1.keys()}")
print(f"Values of dict1: {dict1.values()}")

print("*** Accessing Values ***")
print(f"Value for 'name': {dict1['name']}")
print(f"Value for 'age': {dict1.get('age')}")

print("*** get() with Default Value ***")
print(f"Value for (7, 8): {dict3.get((7, 8), 'Key not found')}")
print(f"Value for 'non_existent_key': {dict1.get('non_existent_key', 'Key not found')}")
print("_________")

print("--- Nested Dictionaries ---")
project_languages = {
    "module_one": {"name": "HTML"},
    "module_two": {"name": "C++"}
}
print(f"Accessing 'module_one' dict: {project_languages.get('module_one')}")
print(f"Accessing 'name' in 'module_two': {project_languages['module_two']['name']}")
print(f"Length of project_languages: {len(project_languages)}")
print(f"Length of nested 'module_one': {len(project_languages['module_one'])}")

all_data_dicts = {"1": dict1, "2": dict2}
print(f"Dictionary of dictionaries: {all_data_dicts}")

print("*** clear() ***")
user_profile = {"name": "UserB"}
print(f"Original user_profile: {user_profile}")
user_profile.clear()
print(f"user_profile after clear: {user_profile}")

print("*** update({key : value}) ***")
user_profile.update({"year": 2008})
user_profile["age"] = 25
print(f"user_profile after update: {user_profile}")

print("*** copy() ***")
copied_profile = user_profile.copy()
user_profile.update({"age": 26})
print(f"Copied profile: {copied_profile}")
print(f"Original user_profile: {user_profile}")

print("*** setdefault(key, value) ***")
temp_dict = {}
temp_dict.setdefault("age", 30)
temp_dict.setdefault("year")
print(f"temp_dict after setdefault: {temp_dict}")

print("*** popitem() ***")
temp_dict.update({"name_key": "ValueX"})
print(f"popitem(): {temp_dict.popitem()}")

print("*** items() ***")
items_view = temp_dict.items()
temp_dict["os_key"] = "Linux"
print(f"temp_dict.items(): {temp_dict.items()}")
print(f"Previous items_view: {items_view}")

print("*** dict.fromkeys() ***")
keys_tuple = ("key1", "key2")
default_val = "default_value"
print(f"dict.fromkeys(keys_tuple, default_val): {dict.fromkeys(keys_tuple, default_val)}")
print(f"dict.fromkeys(keys_tuple[0], 10): {dict.fromkeys(keys_tuple[0], 10)}")

print("*** del statement ***")
temp_dict_mm = {1: "value_j", 2: "value_k"}
del temp_dict_mm[1]
print(f"temp_dict_mm after del key 1: {temp_dict_mm}")

print("*** pop(key, default) ***")
temp_dict_lo = {1: 2, 2: 4, 3: 6, 4: 8}
temp_dict_lo.pop(1, None)
temp_dict_lo.pop(4, 8)
print(f"temp_dict_lo after pop: {temp_dict_lo}")
print("_________________________")


print("=======================================================================")
print("📌 Section 9: Boolean Logic and Type Casting")
print("=======================================================================\n")

print("**** BOOLEAN ****")
print("*** bool() Type Casting ***")

print("--- True values ---")
print(f"bool(' '): {bool(' ')}")
print(f"bool(100): {bool(100)}")
print(f"bool(1.5): {bool(1.5)}")
print(f"bool(True): {bool(True)}")
print(f"bool([1, 2]): {bool([1, 2])}")
print(f"bool((1, 3)): {bool((1, 3))}")
print(f"bool({{1: 2}}): {bool({1: 2})}")
print(f"bool({{1, 2}}): {bool({1, 2})}")

print("--- False values ---")
print(f"bool(0): {bool(0)}")
print(f"bool(''): {bool('')}")
print(f"bool(\"\"): {bool('')}")
print(f"bool(False): {bool(False)}")
print(f"bool(None): {bool(None)}")

print("*** Logical Operators ***")
age_val = 25
country_val = "canada"
rank_val = 10

print("--- and ---")
print(f"age_val == 25 and country_val == 'canada': {age_val == 25 and country_val == 'canada'}")
print(f"age_val == 25 and country_val != 'USA': {age_val == 25 and country_val != 'USA'}")
print(f"Complex 'and' check: {age_val < 30 and country_val == 'canada' and rank_val < 20}")
print(f"False 'and' check: {age_val == 25 and country_val == 'usa'}")

print("--- or ---")
print(f"age_val == 25 or country_val == 'usa' or rank_val == 90: {age_val == 25 or country_val == 'usa' or rank_val == 90}")
print(f"False 'or' check: {age_val == 60 or rank_val == 3}")

print("--- not ---")
print(f"not (age_val == 13): {not age_val == 13}")
print(f"not (rank_val == 10): {not rank_val == 10}")

print("\n*** Arithmetic, Assignment, and Comparison Operators ***")
print("Assignment Operators: =, +=, -=, *=, /=, //=, %=, **=")
print("Comparison Operators: ==, >=, <=, !=, <, >")

print("\n**** Type Casting Functions ****")
print(f"list('User'): {list('User')} -> list")
print(f"set('User'): {set('User')} -> set (removes duplicates, unordered)")
print(f"tuple('User'): {tuple('User')} -> tuple")
print("========")

list_ex = [1, 2, 3, 4]
tuple_ex = (4, 5, 6, 7)
set_ex = {8, 9, 10, 11}
dict_ex = {12: 2, 13: 4, 14: 6}

print("--- Casting to LIST ---")
print(f"list(list): {list(list_ex)}")
print(f"list(tuple): {list(tuple_ex)}")
print(f"list(set): {list(set_ex)}")
print(f"list(dictionary): {list(dict_ex)}")
print("------")

print("--- Casting to SET ---")
print(f"set(list): {set(list_ex)}")
print(f"set(tuple): {set(tuple_ex)}")
print(f"set(set): {set(set_ex)}")
print(f"set(dictionary): {set(dict_ex)}")
print(" ")

print("-- dict() Casting --")
print("dict() only accepts iterables of key-value pairs (e.g., tuples/lists of two items).")
print(" ")

tuple_pairs = (("A", 1),ؤيتجرزو ("B", 2), ("C", 3))
print(f"Original: {tuple_pairs}")
print(f"dict(nested tuple): {dict(tuple_pairs)}")
print(" \n ")

list_pairs = [["D", 4], ["E", 5], ["F", 6]]
print(f"Original: {list_pairs}")
print(f"dict(nested list): {dict(list_pairs)}")
print(" \n ")

mixed_pairs = [(4, 7), [9, 7]]
print(f"Original: {mixed_pairs}")
print(f"dict(mixed list): {dict(mixed_pairs)}")
print(" ")

tuple_mixed = ([8, 9], (0, 1))
print(f"Original: {tuple_mixed}")
print(f"dict(mixed tuple): {dict(tuple_mixed)}")

print("=======================================================================")
print("📌 End of Code")
print("=======================================================================")