# Problem statement
# You are given an integer N, you need to find the number of trailing zeroes in N! (N factorial).

# Note:

# 1. Trailing zeros in a number can be defined as the number of continuous suffix zeros starting from the zeroth place of a number.
# 2. For example, if a number X = 1009000, then the number of trailing zeros = 3 where the zeroth place is 0, the tenth place is 0, the hundredth place is 0.
# 3. ! means “FACTORIAL”. Factorial of a number is calculated by the product of the integer and all integers below it till 1.
# 4. Value of 0! is 1.

def count_trailing_zeros(n):
    count = 0
    while n > 5:
        n //= 5
        count += n 
        
    return count 
    
# Fibonacci series or convert 

# def create_fibo(n):
#     # 0,1,1,2,3,5,8,...
#     start = 0
#     end = 1
    
#     if n<= 0:
#         return []
#     elif n == 1:
#         return [start]
    
    
#     res = [start,end]
    
#     for i in range(2,n):
#         next_val  = start + end
#         res.append(next_val)
#         start = end
#         end = next_val
        
#     return res

def create_fibo(n):
    # 0,1,1,2,3,5,8,...    
    if n<= 0:
        return 0
    elif n == 1:
        return 1
    
    return create_fibo(n-1) + create_fibo(n-2)
    
def create_fibo_sequence(n):
    return [create_fibo(i) for i in range(n)]

# print(create_fibo_sequence(10))


# nested list to a plain list.

def flatten(arr):
    
    res = []
    for i in arr:
        if isinstance(i,list):
            res.extend(flatten(i))
        else:
            res.append(i)
    return res

nested_list = [
    1,
    [2, 3],
    [4, [5, 6], 7],
    [[8, 9], [10, [11, 12]]],
    13
]

# print(flatten(nested_list))



# differnce between extend and append 

# Method	Behavior	Example Input	Result
# append()	Adds the object as a single item	[3, 4]	[1, 2, [3, 4]]
# extend()	Adds each element from iterable	[3, 4]	[1, 2, 3, 4]

# In Python, both append() and extend() are used to add elements to a list, but they behave differently.
# append() adds its argument as a single element to the end of the list. So if you append a list, the entire list becomes a nested element.
# extend() takes an iterable and adds each of its elements individually to the list.




# git merging
# describe about merge conficts
# Merge (Fast-Forward and No Fast-Forward)
# Squash Merging
# Rebase and Merge



# memory allocation
# In Python, memory management is handled automatically by the Python Memory Manager
# Stack(LIFO): Stores local variables and function calls.
# Heap: Stores dynamically allocated objects and data (e.g., lists, dictionaries).
# Global Namespace: Stores global variables and function definitions.


# How to do many to many relation using django ORM




# Add common key values of 2 Dict
# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'b': 3, 'c': 4, 'd': 5}

# # Merge common keys
# common_keys = dict1.keys() & dict2.keys()  
# merged_dict = {key: dict1[key] + dict2[key] for key in common_keys}

# print(merged_dict)  # Output: {'b': 5, 'c': 7}





# swalllow copy vs deep copy
# Shallow Copy: Copies references for nested objects.
# Deep Copy: Recursively copies everything, making the original and copy independent.



# How memory is managed in Python ?
    # Memory Management in Python:
    #       Python uses a private heap space for storing objects and data structures.The Python memory manager handles the allocation and deallocation of this memory space. There are a few key aspects of memory management in Python:
    # Automatic Memory Management: 
    #       Python automatically allocates and frees memory when variables and objects are created and destroyed.
    # Reference Counting: 
    #       Python tracks the number of references to each object. When the reference count drops to zero (i.e., no variables point to the object), the memory is deallocated.
    # Garbage Collection (GC): 
    #       Python uses garbage collection to handle cyclic references (where objects reference each other in a loop). The garbage collector detects and removes objects that are no longer in use.





# What is lambda function ?
# map, filter,slice
# Write a program to generate prime numbers from 50-100 .
# Write a program to reverse a string ?
# Difference between loc n iloc?
# Asked questions on python data types
# differnt types of method



# Difference between pass continue and break in python
# pass:	Does nothing (a placeholder), allows the code to be syntactically correct without performing an action.	Defining empty functions, classes, or loops.
# continue:	Skips the rest of the current iteration and proceeds to the next iteration of the loop.	Skipping specific iterations in a loop.
# break: Exits the loop completely, and the program continues with the next statement after the loop.	Exiting a loop early based on a condition.



# Write a function to typecaste float to int
# tuple and list 
# decorators 



# generator
# def even_num_gen():
#     start = 0
#     while True:
#         yield start
#         start +=2
    

# res = even_num_gen()

# print(next(res))
# print(next(res))
# print(next(res))

# # how to terminate a Generator? return,gen.close(),certain number of yield,break
# GeneratorExit
    
# iterator, 
# oops , 
# threading, 
# multiprocessing



# Pickling , Unpickling
# Pickling and Unpickling are terms associated with serialization and deserialization in Python.
# Pickling:
# Pickling refers to the process of serializing a Python object into a byte stream, so that it can be stored on disk, sent over a network, or saved into a database.
# The Python pickle module is used for this purpose
# Unpickling:
# Unpickling refers to the process of deserializing a byte stream back into a Python object. It essentially converts the byte stream back into a usable object in the Python environment.
# import pickle

# data = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# with open("data.pkl","wb") as fp:
#     pickle.dump(data,fp)

# with open('data.pkl', 'rb') as file:
#     loaded_data = pickle.load(file)
    
# print(loaded_data)




# First Class object in python? 
# First-Class Objects in Python: Python treats functions, classes, 
# and other entities as first-class objects, meaning they can be assigned to variables, passed as arguments, and returned from other functions.



# Object initialization in python?
 
# How to create empty class in python? 
# class Placeholder:
#     pass



# Does python support multiple inheritance? 
# Django vs Flask vs fastapi? 
# Multithreading in Python? 
# Counter in python? 


# Reverse a list Python?
# l=[1,2,3,4]
# print(l[::-1])

# def rev_list(arr):
#     n = len(arr)
#     for i in range(n//2):
#         arr[i],arr[n-i-1] = arr[n-i-1],arr[i]
#     return arr
        
# print(rev_list(l))



 
# Global and local variables? 
# dynamic typing? 




# PEP? 
# PEP 8 (Python Enhancement Proposal 8) style guide rules you should follow when writing clean, readable, and professional Python code
# Use 4 spaces per indentation level (not tabs).
# Limit lines to 79 characters.
# Use 2 blank lines before top-level functions and classes.Use 1 blank line between methods in a class.
# Imports should be:
#     On separate lines
#     Grouped in the following order:
#         Standard library imports
#         Third-party imports
#         Local application imports
# Variables, functions: snake_case
#     Constants: UPPER_CASE
#     Classes: PascalCase or CapWords





# List comprehension? 
# Lambda function? 





# range vs xrange? 
# | Feature         | `range` (Python 3)                                           | `xrange` (Python 2 only)                       |
# | --------------- | ------------------------------------------------------------ | ---------------------------------------------- |
# | Type            | Returns an immutable **range object**                        | Returns an **xrange object** (generator-like)  |
# | Memory usage    | Stores entire sequence in memory (in Python 2)               | Generates numbers on the fly (lazy evaluation) |
# | Performance     | Slower for large ranges (in Python 2)                        | Faster and more memory-efficient               |
# | Indexing        | Supports indexing and slicing                                | Supports indexing only                         |
# | Python 3 status | `xrange()` is removed, and `range()` behaves like `xrange()` | Still used in Python 2 for memory efficiency   |




# Explain different sequences supported in python
# mmutable Sequences: tuple,str,range
# mutable Sequences : list,bytearray
# special Sequences: bytes




# Closure and its uses
# def outer(msg):
#     def inner():
#         print(f"Message: {msg}")
#     return inner

# my_func = outer("Hello, Capgemini!")
# my_func()  # Output: Message: Hello, Capgemini!



# def counter():
#     count = 0
#     def increment():
#         nonlocal count
#         count += 1
#         return count
#     return increment

# my_counter = counter()

# print(my_counter())  # 1
# print(my_counter())  # 2
# print(my_counter())  # 3




# What is the use of else block in try except?
# Execution Flow:
# try: Run this code — may raise an exception.
# except: Handle the exception if one occurs.
# else: Run this only if the try block didn’t raise any exception.
# finally: (Optional) Run no matter what — success or failure.




# implment a context manager
# class CustomContext:
#     def __init__(self,op_mode):
#         self.op_mode = op_mode
        
#     def __enter__(self):
#         print("Entering the context ...")
#         return self

#     def __exit__(self,exec_type,exec_value, traceback):
#         print("Exiting the context ...")
        
#         if exec_type:
#             print(f"Exception handled : {exec_type}")
        
#         return False
    
# with CustomContext("wb") as ctx:
#     print(f"Inside the with block with {ctx.op_mode} mode")


 
# implement an itertor ?
class EvenIterator:
    def __init__(self,max_val):
        self.max_val = max_val
        self.num = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num > self.max_val :
            raise StopIteration
        current = self.num
        self.num += 2
        return current
    
evens =  EvenIterator(10)
for num in evens:
    print(num)
    
    
# implemet a descriptor?



# namespace in python
# LEGB Rule -  Local, Enclosing , Global, builtin 
# Namespaces in Python are implemented as dictionaries. When you define a variable, Python internally stores it as a key-value pair in the corresponding namespace.
# print(globals())
# print(locals())



# Write Python code to check the given sequence of number is a palindrome or not?

# def check_palindorm_num(num):
#     original_num = num
#     rev_num = 0
#     c = 1
#     while num>0:
#         rev_num = rev_num*10  + num%10
#         num //= 10 
    
#     return  original_num == rev_num

# print(check_palindorm_num(22522))
        
