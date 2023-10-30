#Answer 1 :
User_input=input("Enter YOur Text :")
words =[]
counts=[]
for char in User_input:
    if char in words:
        index=words.index(char)
        counts[index]+=1
    else:
        words.append(char)
        counts.append(1)
for i in range(len(words)):
    print(words[i] , ":" , counts[i])



#Answer 2 :
user_input=input("Enter Your Text:")
count = {}
for char in user_input:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

for char , count in count.items():
    print(char , ":" , count)
