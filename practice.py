# # Reverse a list

# original = [1, 2, 3, 4, 5]
# reversed_list = []


# for i in range(len(original)-1,-1,-1):
#     reversed_list.append(original[i])
    
# print(reversed_list)



# # filter function  -- extract items based on the condition i.e Ture or False
# def is_even(n):
#     return n%2==0

# l = [1, 2, 3, 4, 5]

# res = filter(is_even,l)
# print(list(res))


# # map - transform items

# def square(n):
#     return n*n
# res = map(square,l)
# print(list(res))


# #reduce - reduce all elements to single value
# from functools import reduce

# def add(x,y):
#     return x+y
# res = reduce(add,l)

# print(res)

# --------------------------------------------------------------------------------
# Pagination , Throttler , internationlization, 
# Operation overloading , operation overriding 
# supervised and unsupervised ML

 
# deadlock in python.

# import threading
# import time

# lock_a = threading.Lock()
# lock_b =  threading.Lock()

# def thread_1():
#     with lock_a:
#         print("Thread 1 acquired lock A")
#         time.sleep(1)
#         with lock_b:
#             print("Thread 1 acquired lock B")
            
# def thread_2():
#     with lock_b:
#         print("Thread 2 acquired lock B")
#         time.sleep(1)
#         with lock_a:
#             print("Thread 2 acquired lock A")
            
# t1 = threading.Thread(target=thread_1)
# t2 = threading.Thread(target=thread_2)

# t1.start()
# t2.start()


# t1.join()
# t2.join()
# --------------------------------------------------------------------------------

# First Non-Repeating Character Problem Statement
# You are given a string consisting of English alphabet characters. 
# Your task is to identify and return the first character in the string that does not repeat. If every character repeats, return the first character of the string.
# from collections import OrderedDict,Counter

# def first_non_repeating_charcter(s: str) -> str:
#     if not s:
#         return ""
    
#     freq = Counter(s)
    
#     for char in s:
#         if freq[char] ==1:
#             return char
        
#     return s[0]
# def first_non_repeating_charcter(s: str) -> str:
#     if not s:
#         return ""
    
#     char_count = {}
#     for char in s:
#         if char in char_count:
#             char_count[char] += 1
#         else:
#             char_count[char] = 1
            
#     for char in s:
#         if char_count[char] == 1:
#             return char

#     return s[0]
    
# print(first_non_repeating_charcter("teeterr"))

# Write a function to find the second largest element from an integer array in a single traversal.
def second_largest(arr):
    if len(arr) < 2:
        return None
    
    first = second = float('-inf')
    
    for num in arr:
        if num > first:
            second = first
            first = num 
            
        elif first > num > second:
            second = num 
        
    return second if second !=float("-inf") else None
    
print(second_largest([10, 5, 20, 8]))


# Explain the difference between encapsulation and abstraction.

# --------------------------------------------------------------------------------
# Allowed data types as dictionary keys:
# These are the most common hashable and immutable types:

# int — e.g., {1: "one"}

# float — e.g., {3.14: "pi"}

# str — e.g., {"name": "Alice"}

# bool — e.g., {True: "yes", False: "no"}

# tuple (only if all elements are also immutable) — e.g., {(1, 2): "coords"}

# frozenset — immutable version of a set — e.g., {frozenset([1, 2]): "group"}

# --------------------------------------------------------------------------------

#  Given a sentence, find the frequency of each word.


# --------------------------------------------------------------------------------
# Q46. If Python is an interpreted language, why are .pyc files generated?
# Ans. Python compiles source code to bytecode for faster execution, stored in .pyc files.
# Python interpreter compiles source code to bytecode before execution

# Bytecode is platform-independent and faster to execute than source code

# Compiled bytecode is stored in .pyc files for future use and faster startup time

# If source code is modified, .pyc files are automatically recompiled

# To stop creating .pyc file;
    # python -B your_script.py
    # set PYTHONDONTWRITEBYTECODE=1

    # import sys
    # sys.dont_write_bytecode = True

# --------------------------------------------------------------------------------

# How can you diagonally iterate through and print the elements of a 2D array?
# mat = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ]

# rows = len(mat)
# cols = len(mat[0])
# diagonals = {}  # Regular dictionary

# # Group elements by (i + j) without defaultdict
# for i in range(rows):
#     for j in range(cols):
#         key = i + j
#         if key not in diagonals:
#             diagonals[key] = []
#         diagonals[key].append(mat[i][j])

# # Print diagonals in order
# for k in sorted(diagonals.keys()):
#     for val in diagonals[k]:
#         print(val, end=" ")

# print(diagonals)

# Given an array of integers, find the indices of two numbers that add up to a specific target value (e.g., 8 or a dynamic value).

# singleton
# class Singleton():
#     _instance = None
    
#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
            
#         return cls._instance