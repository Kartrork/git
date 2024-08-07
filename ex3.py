# Ex3: Enter text and display only letter in odd index

text = input("Please enter your text: ")
countOdd = 0
for i in range(len(text)):
    if i % 2 == 1: 
        print(text[i])