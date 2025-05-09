# st = "Su78*{*dipta Sa^{^lmal"

# res = ""

# l = '123456789@#$%^&8{}*'

# for i in st:
#     if i.isalpha() or i == " ":
#         res+=i 
        
# print(res)

li =[2,7,3,8,1,6,8]
target = 9 

temp_dic = {}

res = []
for i in li:
    diff = target - i 
    
    if diff not in temp_dic:
        temp_dic[diff] = i 
    
    
    if diff in temp_dic:
        res.append((diff,temp_dic[diff]))
        

res = [if j in (sorted(temp_dic)[:3]) for j in res ]
     
print(res)
