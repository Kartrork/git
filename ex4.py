# Ex4: Enter text and display reverse text

text = input("Please enter your text ")
for i in range(len(text)):
    print(text[len(text)-1-i])