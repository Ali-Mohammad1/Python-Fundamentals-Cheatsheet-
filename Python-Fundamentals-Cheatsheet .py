import keyword

print("=======================================================================")
print("Section 1: Keywords and Initialization")
print("=======================================================================\n")

print("Python keywords:", keyword.kwlist)
print("_" * 30)
print("\n")


print("=======================================================================")
print("Section 2: Numeric Data Operations")
print("=======================================================================\n")

int_val1, int_val2, int_val3 = 1000, 200, 300
complex_num = 6 + 8j
print(type(complex_num))
print(f"Imaginary part: {complex_num.imag}")
print(f"Real part: {complex_num.real}")
print(int_val1 * 2)
print(int_val2)
print(f"Float format (default): {int_val1:f}")
print(f"Float format (1 decimal): {int_val2:.1f}")


print("=======================================================================")
print("Section 3: String Formatting")
print("=======================================================================\n")

big_number = 867667
sample_str = "pythoncode"
float_num = 5755.888877

print("--- Integer Formatting ---")
print(f"Comma separator: {big_number:,}")
print(f"Underscore separator: {big_number:_}")
print(f"Underscore with d: {big_number:_d}")
print("_" * 10)

print("--- String Formatting ---")
print(f"Truncated to 2 chars: {sample_str:.2s}")
print(f"Truncated to 5 chars: {sample_str:.5s}")
print("_" * 10)

print("--- Float Formatting ---")
print(f"2 decimals: {float_num:.2f}")
print(f"5 decimals: {float_num:.5f}")
print(f"Original: {float_num}")
print("_" * 10)


print("=======================================================================")
print("Section 4: Escape Sequences")
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

line_a = "Part \
A \
Complete"
line_b = "X \
Y \
Z"
print(line_a + "\n" + line_b)
print("__________________________\n ")


print("=======================================================================")
print("Section 5: List Operations")
print("=======================================================================\n")

print("LISTS".center(13, "*"))
print(" ")

list_one = [100, 6, 5, -10, 48, 20]
list_two = [80, 6, 8, 90]
list_three = [10, 8, 9, 3, 5, 6, 7]
chars_a = ["a", "b", "c", "d"]
chars_b = ["e", "f", "g", "h"]

list_three[0:3] = "a", "b"
print(f"After slice assignment: {list_three}")

print("--- APPEND ---".center(10, "*"))
chars_b.append(chars_a)
print(f"chars_b after append: {chars_b}")

print("--- EXTEND ---".center(10, "*"))
chars_a.extend(list_three)
print(f"chars_a after extend: {chars_a}")

print("*** sort(reverse=True or False) ***")
list_one.sort(reverse=True)
print(f"Descending sort: {list_one}")
list_one.sort(reverse=False)
print(f"Ascending sort: {list_one}")
list_one.sort()
print(f"Default sort(): {list_one}")

print("--- CLEAR ---".center(9, "*"))
list_two.clear()
print(f"list_two after clear: {list_two}")

print("--- COPY ---".center(8, "*"))
list_copy = list_three.copy()
print(f"list_copy (copy of list_three): {list_copy}")
print("_________________________\n ")


print("=======================================================================")
print("Section 6: Tuple Operations")
print("=======================================================================\n")

print("TUPLES".center(14, "*"))
print(" ")

tuple_one = (1, 2, 3, 4, 5, 5)
tuple_two = (0, 10, 20)

print("*** Concatenation (a += b) ***")
tuple_one += tuple_two
print(f"tuple_one after concatenation: {tuple_one}")

print("*** Concatenation (a = b + c + d) ***")
tuple_three = ("user1", "user2")
tuple_four = tuple_one + tuple_three + (9, 7)
print(f"tuple_four from multiple concatenations: {tuple_four}")

print("*** count() ***")
print(f"Count of 5 in tuple_one: {tuple_one.count(5)}")

print("*** index() ***")
print(f"Index of 10 in tuple_two: {tuple_two.index(10)}")

print("*** Tuple Unpacking ***")
tuple_unpack = (100, 200, 300)
var_x, var_y, var_z = tuple_unpack
print(f"Unpacked var_x: {var_x}")
print(f"Unpacked var_y: {var_y}")
print(f"Unpacked var_z: {var_z}")

print("*** Partial Unpacking with Placeholder ***")
tuple_place = (400, 500, 600, 700)
var_a, var_b, _, var_c = tuple_place
print(f"Unpacked var_a: {var_a}")
print(f"Unpacked var_b: {var_b}")
print(f"Unpacked var_c: {var_c}")
print(f"Placeholder (_): {_}")
print("_________________________\n ")


print("=======================================================================")
print("Section 7: Set Operations")
print("=======================================================================\n")

print("**** SETS ****")
print(" ")

set_empty = {1, 3, 5, 8}
set_empty.clear()
print(f"set_empty after clear: {set_empty}")

set_first = {8, 7, 0, 4}
set_second = {9, 1, 3, 2}
print(f"Union: {set_first.union(set_second)}")

set_first.add("new_item")
print(f"set_first after add: {set_first}")

set_copy = set_second.copy()
print(f"set_copy (copy of set_second): {set_copy}")

set_second.remove(2)
print(f"set_second after remove(2): {set_second}")

set_sample = {9, "j_item", 10.4, 90, 60}
set_sample.discard("j_item")
print(f"set_sample after discard('j_item'): {set_sample}")

print(f"Random pop from set_sample: {set_sample.pop()}")

set_proj = {"Project"}
set_sample.update("DEV")
set_sample.update(["javascript_lib"])
set_sample.update([100, 50.5])
set_sample.update(set_proj)
print(f"set_sample after update: {set_sample}")

set_a = {10, 20}
set_b = {20, 30}
print(f"Difference (a - b): {set_a.difference(set_b)}")
set_c = {70, 40}
set_c.difference_update(set_a)
print(f"set_c after difference_update(a): {set_c}")

set_one = {"x_key", 6, 8}
set_two = {"x_key", 9, 6, 7, 4}
set_three = {9, 6}
print(f"Intersection (one & two): {set_one.intersection(set_two)}")
set_two.intersection_update(set_three)
print(f"set_two after intersection_update(three): {set_two}")

set_j1 = {"zero", "ItemA", 80}
set_j2 = {"one", 80, "zero", "ItemB"}
set_j3 = {"one", 80, "ItemC", 90, 2}
print(f"Symmetric difference (j2 ^ j1): {set_j2.symmetric_difference(set_j1)}")
set_j2.symmetric_difference_update(set_j3)
print(f"set_j2 after symmetric_difference_update(j3): {set_j2}")

set_m = {1, 2, 3, 4}
set_n = {1, 2, 3}
print(f"m.superset(n): {set_m.issuperset(set_n)}")
print(f"n.superset(m): {set_n.issuperset(set_m)}")
print(f"n.subset(m): {set_n.issubset(set_m)}")
print(f"m.subset(n): {set_m.issubset(set_n)}")

set_x = {1, 2, 3}
set_y = {1, 2, 3, 4, 5}
set_z = {6, 7, 8}
print(f"x.disjoint(y): {set_x.isdisjoint(set_y)}")
print(f"x.disjoint(z): {set_x.isdisjoint(set_z)}")
print("__________________________ \n ")


print("=======================================================================")
print("Section 8: Dictionary Operations")
print("=======================================================================\n")

print("DICTIONARIES".center(20, "*"))
print(" ")

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
print(f"projects.get('module_one'): {projects.get('module_one')}")
print(f"projects['module_two']['name']: {projects['module_two']['name']}")
print(f"Length of projects: {len(projects)}")
print(f"Length of nested 'module_one': {len(projects['module_one'])}")

all_dicts = {"first": dict_person, "second": dict_extra}
print(f"all_dicts: {all_dicts}")

print("*** clear() ***")
profile = {"name": "UserB"}
print(f"Original: {profile}")
profile.clear()
print(f"After clear: {profile}")

print("*** update() ***")
profile.update({"year": 2008})
profile["age"] = 25
print(f"After update: {profile}")

print("*** copy() ***")
profile_copy = profile.copy()
profile["age"] = 26
print(f"Copied: {profile_copy}")
print(f"Original: {profile}")

print("*** setdefault() ***")
temp = {}
temp.setdefault("age", 30)
temp.setdefault("year")
print(f"temp after setdefault: {temp}")

print("*** popitem() ***")
temp.update({"name_key": "ValueX"})
print(f"popitem: {temp.popitem()}")

print("*** items() ***")
items_view = temp.items()
temp["os_key"] = "Linux"
print(f"temp.items(): {temp.items()}")
print(f"items_view (dynamic): {items_view}")

print("*** dict.fromkeys() ***")
keys_tuple = ("key1", "key2")
print(f"fromkeys with default: {dict.fromkeys(keys_tuple, 'default_val')}")
print(f"fromkeys with single char: {dict.fromkeys(keys_tuple[0], 10)}")

print("*** del statement ***")
temp_dict = {1: "val1", 2: "val2"}
del temp_dict[1]
print(f"After del key 1: {temp_dict}")

print("*** pop(key, default) ***")
temp_lo = {1: 2, 2: 4, 3: 6, 4: 8}
temp_lo.pop(1)
temp_lo.pop(4, 8)
print(f"After pop: {temp_lo}")
print("_________________________")


print("=======================================================================")
print("Section 9: Boolean Logic and Type Casting")
print("=======================================================================\n")

print("**** BOOLEAN ****")
print("*** bool() Type Casting ***")

print("--- True values ---")
print(f"bool(' '): {bool(' ')}")
print(f"bool(100): {bool(100)}")
print(f"bool(1.5): {bool(1.5)}")
print(f"bool(True): {bool(True)}")
print(f"bool([1,2]): {bool([1,2])}")
print(f"bool((1,3)): {bool((1,3))}")
print(f"bool({{1:2}}): {bool({1:2})}")
print(f"bool({{1,2}}): {bool({1,2})}")

print("--- False values ---")
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
print(f"list('User'): {list('User')}")
print(f"set('User'): {set('User')}")
print(f"tuple('User'): {tuple('User')}")
print("========")

list_ex = [1,2,3,4]
tuple_ex = (4,5,6,7)
set_ex = {8,9,10,11}
dict_ex = {12:2,13:4,14:6}

print("--- Casting to LIST ---")
print(f"list(list): {list(list_ex)}")
print(f"list(tuple): {list(tuple_ex)}")
print(f"list(set): {list(set_ex)}")
print(f"list(dict): {list(dict_ex)}")
print("------")

print("--- Casting to SET ---")
print(f"set(list): {set(list_ex)}")
print(f"set(tuple): {set(tuple_ex)}")
print(f"set(set): {set(set_ex)}")
print(f"set(dict): {set(dict_ex)}")
print(" ")

print("-- dict() Casting --")
print("Requires iterable of key-value pairs (e.g., list of tuples)")
pair_tuple = (("A",1), ("B",2), ("C",3))
print(f"Original: {pair_tuple}")
print(f"dict(pair_tuple): {dict(pair_tuple)}")
print(" \n ")

pair_list = [["D",4], ["E",5], ["F",6]]
print(f"Original: {pair_list}")
print(f"dict(pair_list): {dict(pair_list)}")
print(" \n ")

mixed_pairs = [(4,7), [9,7]]
print(f"Original: {mixed_pairs}")
print(f"dict(mixed_pairs): {dict(mixed_pairs)}")
print(" ")

tuple_mixed = ([8,9], (0,1))
print(f"Original: {tuple_mixed}")
print(f"dict(tuple_mixed): {dict(tuple_mixed)}")

print("=======================================================================")
print("End of Code")
print("=======================================================================")