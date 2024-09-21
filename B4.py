#dictionary
d={}
s=input("Enetr a sentence :\n")
words=s.split(" ")
for w in words:
    if w in d:
        c=d.get(w)
        c+=1
        c=d.update({w:c})
    else:
        d.update({w:1})
print("the words present in sentence")
print(d.keys())
print("the words and it counts prsent in sentence")
for key,value in d.items():
    print(f"the word {key} precent {value} times in sentence")