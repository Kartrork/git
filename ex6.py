# Ex6 Enter text and display counter of lowercase letter "B" and uppercase letter "B"

text = input("Please enter your text ")
countB = 0
for i in range(len(text)):
    if text[i] == "B" or text[i] == "b":
        countB +=i
print(countB)