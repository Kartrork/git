# Ex5 Enter text and display only letter "A" index

text = input("Please your text ")
indexA=0
for i in range(len(text)):
    if text[i]=="A":
        indexA=i
print("Index A:", indexA)