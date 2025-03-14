#builtin-function
from functools import reduce
import time
import math

def multiply_list(numbers):
    return reduce(lambda x, y: x * y, numbers)

def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return upper, lower

def is_palindrome(s):
    return s == s[::-1]

def delayed_sqrt(number, delay):
    time.sleep(delay / 1000)
    return math.sqrt(number)

def all_true(t):
    return all(t)

print(multiply_list([1, 2, 3, 4]))

upper, lower = count_case("Hello World")
print("Upper case letters:", upper, "Lower case letters:", lower)

print(is_palindrome("madam"))

num = 25100
ms = 2123
print(f"Square root of {num} after {ms} milliseconds is {delayed_sqrt(num, ms)}")

print(all_true((True, True, False)))



#dir-and-files
from functools import reduce
import time
import math
import os
import shutil

def multiply_list(numbers):
    return reduce(lambda x, y: x * y, numbers)

def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return upper, lower

def is_palindrome(s):
    return s == s[::-1]

def delayed_sqrt(number, delay):
    time.sleep(delay / 1000)
    return math.sqrt(number)

def all_true(t):
    return all(t)

def list_directories_files(path):
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    return directories, files

def check_path_access(path):
    return {
        "Exists": os.path.exists(path),
        "Readable": os.access(path, os.R_OK),
        "Writable": os.access(path, os.W_OK),
        "Executable": os.access(path, os.X_OK)
    }

def path_info(path):
    if os.path.exists(path):
        return os.path.dirname(path), os.path.basename(path)
    return "Path does not exist"

def count_lines_in_file(filename):
    with open(filename, 'r') as f:
        return sum(1 for _ in f)

def write_list_to_file(filename, data_list):
    with open(filename, 'w') as f:
        f.writelines("\n".join(data_list))

def generate_alphabet_files():
    for letter in range(65, 91):  # ASCII values for A-Z
        with open(f"{chr(letter)}.txt", "w") as f:
            f.write(f"This is file {chr(letter)}.txt")

def copy_file(source, destination):
    shutil.copy(source, destination)

def delete_file(path):
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)
        return "File deleted successfully"
    return "File cannot be deleted"

print(multiply_list([1, 2, 3, 4]))

upper, lower = count_case("Hello World")
print("Upper case letters:", upper, "Lower case letters:", lower)

print(is_palindrome("madam"))

num = 25100
ms = 2123
print(f"Square root of {num} after {ms} milliseconds is {delayed_sqrt(num, ms)}")

print(all_true((True, True, False)))

