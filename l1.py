Cybage
'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''


# Sort the data by age

persons = [

	{

	 "id": 1,

	 "fname": "Albert",

	 "age": 35

	},

	{

	 "id": 2,

	 "fname": "Issac",

	 "age": 32

	},

	{

	 "id": 3,

	 "fname": "James",

	 "age": 33

	},

	{

	 "id": 4,

	 "fname": "Edison",

	 "age": 32

	}

]


res =  sorted(persons,key = lambda x:x["age"])
# print(res)


# Given a list 

persons = [

    {

        "id": 1,

        "name": "Alice Johnson",

        "gender": "Female",

        "date_of_birth": "1985-07-23",

        "salary": 75000,

        "department": "Engineering"

    },

    {

        "id": 2,

        "name": "Bob Smith",

        "gender": "Male",

        "date_of_birth": "1978-11-15",

        "salary": 68000,

        "department": "Sales"

    },

    {

        "id": 3,

        "name": "Carol Williams",

        "gender": "Female",

        "date_of_birth": "1992-04-08",

        "salary": 72000,

        "department": "Engineering"

    },

    {

        "id": 4,

        "name": "David Brown",

        "gender": "Male",

        "date_of_birth": "1989-11-30",

        "salary": 80000,

        "department": "Sales"

    },

    {

        "id": 5,

        "name": "Emma Davis",

        "gender": "Female",

        "date_of_birth": "1975-12-20",

        "salary": 90000,

        "department": "Sales"

    },

    {

        "id": 6,

        "name": "Frank Miller",

        "gender": "Male",

        "date_of_birth": "1982-07-14",

        "salary": 85000,

        "department": "Operations"

    }

]

# 1) Group together persons that have birthdays in the same month

user_grp = {}

for i in persons:
    
    if i["date_of_birth"].split("-")[1] not in user_grp:
        user_grp[i["date_of_birth"].split("-")[1]] = []
    
    user_grp[i["date_of_birth"].split("-")[1]].append(i["name"])

print(user_grp)
        
 

