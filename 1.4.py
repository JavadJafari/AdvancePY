a = input("Enter Text :")
alist=[]

for char in a:
    if char not in alist:
        result =alist.append(char)
    else:
        result=alist.append("$")
        
print("".join(alist))
