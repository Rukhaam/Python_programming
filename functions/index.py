def add(a,b):
    return a+b
print("The sum of 5 and 3 is:", add(5,3))


def subtract(a,b):
     return a-b
print("The difference of 10 and 4 is:", subtract(10,4))


def calc_compund_interest(principal, rate, time):
    if principal < 0 or rate < 0 or time < 0:
        return "Invalid input. Principal, rate, and time must be non-negative."
    amount = principal * ((1 + rate / 100) ** time)
    return round(amount, 2)

final_balance = calc_compund_interest(10000, 7.5, 5)
print(f"Maturity Amount: {final_balance}")


def analyze_dataset(numbers):
    total = sum(numbers)
    count = len(numbers)
    mean = total / count
    minimum = min(numbers)
    maximum = max(numbers)
    return mean, minimum, maximum 


avg_val, min_val, max_val = analyze_dataset([12, 45, 7, 23, 89, 34])
print(f"Mean: {avg_val:.2f}, Min: {min_val}, Max: {max_val}")


def connect_database(host, port=5432, timeout=30, use_ssl=True):
    return f"Connecting to {host}:{port} (SSL={use_ssl}, Timeout={timeout}s)"

# 1. All positional
print(connect_database("127.0.0.1", 3306, 10, False))

# 2. Positional mixed with Keyword (order of keyword args doesn't matter)
print(connect_database("db.example.com", use_ssl=False, timeout=60))

# THE MUTABLE DEFAULT ARGUMENT TRAP & FIX:
def append_item_bad(item, target_list=[]):  # BAD: target_list persists across calls!
    target_list.append(item)
    return target_list

def append_item_good(item, target_list=None):  # GOOD: Use None as sentinel
    if target_list is None:
        target_list = []
    target_list.append(item)
    return target_list