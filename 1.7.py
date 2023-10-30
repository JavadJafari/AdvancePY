text=input("Enter Your Text :")
words=""
for i in text:
    if i not in words:
        words+=i
print(words)