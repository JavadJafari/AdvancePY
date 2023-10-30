text=input("Please Enter a list of Word and seprate with a space :")
tlist=text.split()
longes_word =""
max_len =0
for word in tlist:
    if len(word) > max_len:
        longes_word = word
        max_len = len(word)


print(f" Longest Charecter is :" , longes_word , "And lenth of this char is :" , max_len)
