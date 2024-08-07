# Ex2: Enter text and display only uppercase letter

text = input("Please enter your text: ")
uppercase_letter = ""
for i in range(len(text)):
    if text[i].isupper():
        uppercase_letter += text[i]
print("Uppercase Letters: ", uppercase_letter)