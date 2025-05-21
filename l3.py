def extendList(val, list=[]):
    list.append(val)
    return list
 
list1 = extendList(10) --->  [10]
list2 = extendList(123,[]) ---> [123]
list3 = extendList('a') ---> ['a']
 
print ("list1 = %s" % list1) 
print ("list2 = %s" % list2)
print ("list3 = %s" % list3)

list1 = [10, 'a']
list2 = [123]
list3 = [10, 'a'



list = ['a', 'b', 'c', 'd', 'e']
print(list[10:])


def lowercase(func):
	def wrapper():
		input_str = func()
		print(input_str.lower())
	return wrapper



def get_input():
	st = input("Enter the string: ")
	return st
@lowercase
get_input()

l = [{name:abc,age:34},]
res = sorted(l,key = lambda x: x["age"])


my_list = [[10,20,30],[40,50,60],[70,80,90]]

trmp_list =[]
res = [ i for item in my_list for i in item]


res =[]
for item in my_list:
	res.extend(item)


class A:
    def __init__(self,a):
        self.a = a

class B:
    def __init__(self,b):
        self.b = b


class C(A,B):
    def __init__(self,c):
        self.c = c


Table 1: Emp
Columns :- EmpId, EmpName, DeptId, Salary, MgrId
 
Table 2: Dept
Columns: DeptId, DeptName
 
Query 1: - Write query to give list of Dept name along with total employees in it 
Query 2: - List employees having highest salary in each dept


SELECT COUNT(*) FROM Emp GROUP BY(DeptID)  

def read_line(""


with open("cutomer_log.log","r") as fp:
    line  =  cutomer_log.readine()
    if [ERROR]


d1 = dict(a=1, b=3, c=33, e=5) 
d2 = dict(a=2, b=4, c=3, d=2)

d3={"a":2, "b":4, "c":33, "d":2, "e":5}

d3 = {}
for i,j in zip(d1,d2):
    if i ==j:
    	if d1[i] > d2[j];
           d3[i] = d1[i]
         else:
            d3[i] = d2[j]
     d3[i] = d1[i]
     d3[j] = d2[j]






