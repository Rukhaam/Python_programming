not_a_tuple = (1)

print(type(not_a_tuple))  # Output: <class 'int'>

tuple_with_one_element = (1,)
print(type(tuple_with_one_element))  # Output: <class 'tuple'>

coordinates = 34.0837, 74.7973

scores = (98, 92, 85, 79, 74, 60)
gold, silver, *middle_pack, lowest = scores
print(f"Gold: {gold}, Middle: {middle_pack}, Lowest: {lowest}")

# Immutable Container vs Mutable Element Nuance:
# While the tuple's references cannot change, a mutable object INSIDE a tuple CAN be mutated!
record = ("User_01", [100, 200])
record[1].append(300)  # Valid! The tuple still points to the same list address
print(record)          # ('User_01', [100, 200, 300])


#SET

backend_devs = {"Aisha", "Rohan", "Vikram", "Neha"}
frontend_devs = {"Rohan", "Neha", "Karan", "Simran"}

full_stack = backend_devs & frontend_devs
print(full_stack)  # Output: {'Rohan', 'Neha'}

all_eng = backend_devs | frontend_devs
print(all_eng)  # Output: {'Aisha', 'Rohan', 'Vikram', 'Neha', 'Karan', 'Simran'}

only_backend = backend_devs - frontend_devs
print(only_backend)  # Output: {'Aisha', 'Vikram'}


#dictonary
devs = {
    "backend": {"Aisha", "Rohan", "Vikram", "Neha"},
    "frontend": {"Rohan", "Neha", "Karan", "Simran"}
}

devs["full_stack"] = devs["backend"] & devs["frontend"]
print(devs)  # Output: {'backend': {'Aisha', 'Rohan', 'Vikram', 'Neha'}, 'frontend': {'Rohan', 'Neha', 'Karan', 'Simran'}, 'full_stack': {'Rohan', 'Neha'}} 

keys = ["id", "role", "active"]
vals = [101, "Admin", True]
user_profile = dict(zip(keys, vals))
print(user_profile)  # Output: {'id': 101, 'role': 'Admin', 'active': True}

print(type(user_profile))  # Output: <class 'dict'>

print(user_profile.get("role", "Not Found"))  # Output: Admin

text = "mississippi"

char_freq ={}

for char in text : 
    char_freq[char] = char_freq.get(char,0)+1
print(f"Character Frequency: {char_freq}")  # Output: Character Frequency: {'m': 1, 'i': 4, 's': 4, 'p': 2} 


students_by_dept = [("Computer Science", "Alice"), ("Mathematics", "Bob"), ("Computer Science", "Charlie"), ("Physics", "David")]

dept_map = {}
for dept,name in students_by_dept:
       dept_map.setdefault(dept, []).append(name)
print(dept_map)  # Output: {'Computer Science': ['Alice', 'Charlie'], 'Mathematics': ['Bob'], 'Physics': ['David']}