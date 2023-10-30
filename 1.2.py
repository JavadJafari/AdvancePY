a =input("Enter a text include Text & Num :")
numerial =0
non_numberial =0
for i in a:
    if i.isdigit():
        numerial += 1
    else:
        non_numberial += 1

print(f"Count of Numberial is :" , numerial)
print(f"Count of Non_numberial is :" , non_numberial)