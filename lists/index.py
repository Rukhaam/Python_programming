import copy

# Creation, Indexing, and Slicing
readings = [10, 20, 30, 40, 50, 60]
print(readings[-1])       # Output: 60 (last element)
print(readings[1:4])      # Output: [20, 30, 40] (index 4 is exclusive)
print(readings[::-1])     # Output: [60, 50, 40, 30, 20, 10] (reverses list)

# Core Mutating Methods
readings.append(70)       # Adds 70 to the end -> O(1)
readings.extend([80, 90]) # Unpacks and appends multiple items -> O(k)
readings.insert(1, 15)    # Inserts 15 at index 1 (shifts others right) -> O(N)
popped_val = readings.pop(2) # Removes & returns item at index 2 (default is -1)
readings.remove(50)       # Removes first occurrence of value 50 (raises ValueError if absent)

# List Comprehension: Squares of even numbers only
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(f"Even Squares: {even_squares}")  # Output: [4, 16, 36, 64, 100]


original_list = [1, 2, 3, 4, 5]
# Shallow Copy
shallow_copy = original_list.copy()
deep = copy.deepcopy(original_list)


def normalize_in_place(scores): 
    if not scores:
        return  # Avoid division by zero
    max_score = max(scores)
    for i in range(len(scores)):
        scores[i] = round((scores[i] / max_score) * 100, 2)
def filter_outliers(data, lower_bound, upper_bound):
    return [val for val in data if lower_bound <= val <= upper_bound]


raw_marks = [40, 60, 80]
normalize_in_place(raw_marks)
print(f"In-place normalized: {raw_marks}")  # [50.0, 75.0, 100.0]

sensor_data = [12, -999, 15, 14, 5000, 13]
clean_data = filter_outliers(sensor_data, 0, 100)
print(f"Filtered new list: {clean_data}")   # [12, 15, 14, 13]



# 1. Binary Search Implementation (Iterative - O(log N) time, O(1) space)
def binary_search(sorted_list, target):
    low, high = 0, len(sorted_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# 2. Sorting with Custom Keys
students = [
    {"name": "Aarav", "marks": 88, "age": 20},
    {"name": "Zoya", "marks": 95, "age": 19},
    {"name": "Kabir", "marks": 88, "age": 18},
]

# Sort by marks descending (-x["marks"]), then by age ascending (x["age"]) on ties
ranked = sorted(students, key=lambda x: (-x["marks"], x["age"]))
for s in ranked:
    print(f"{s['name']}: Marks={s['marks']}, Age={s['age']}")

nums = [5, 2, 9, 1, 5, 6]
# Sort in-place using a custom key (absolute value)
nums.sort(key=abs)
print(f"Sorted by absolute value: {nums}")  # Output: [1, 2, 5, 5, 6, 9]


details = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]
print(sorted(details, key=lambda x: x["age"])) # This will print "Bob" since 'details' is a list of dictionaries


