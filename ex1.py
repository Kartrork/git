# Ex1: Enter the string and display all letter one by one

text = input("Enter your text: ")
countLetter = 0
for i in range(len(text)):
    if text[i] > str(len(text)):
        countLetter += 1
    print(countLetter)