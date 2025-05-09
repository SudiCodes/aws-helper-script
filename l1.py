Publicis Sapient

a = [1,2,3,4]
b = [3,4,5,6]

# print(set(a).intersection(set(b)))

res = [i+j for i,j in zip(a,b)]

# print(res)

import time

def decorator(func):
    def wrapper(*arg):
        t1 = time.time()
        func(*arg)
        t2 = time.time()
        t = t2 - t1
        
        print(f"time elapsed {t}")
    
    return wrapper

@decorator
def count(num):
	for i in range(1,num):
		print(i)
		

# count(5)

class A: pass  

class B(A): pass  

class C(A): pass  

class D(B, C): pass

# D -> B -> A -> C -> A
# print(D.mro())
 
def flatten(arr):
    # if len(arr) == 1:
    #     return arr
     
    res = []
    
    for i in arr:
        if type(i) == list:
            flatten(i)
        res
    return res
    
         
    
 
flatten([1, [2, [3, 4], 5]]) #→ [1, 2, 3, 4, 5]
 
 


 

