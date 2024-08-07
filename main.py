# Ex1: Enter the string and display all letter one by one

# text = input("Enter your text: ")
# countLetter = 0
# for i in range(len(text)):
#     if text[i] > str(len(text)):
#         countLetter += 1
#     print(countLetter)

# Ex2: Enter text and display only uppercase letter

# text = input("Please enter your text: ")
# uppercase_letter = ""
# for i in range(len(text)):
#     if text[i].isupper():
#         uppercase_letter += text[i]
# print("Uppercase Letters: ", uppercase_letter)

# Ex3: Enter text and display only letter in odd index

# text = input("Please enter your text: ")
# countOdd = 0
# for i in range(len(text)):
#     if i % 2 == 1: 
#         print(text[i])

# Ex4: Enter text and display reverse text

# text = input("Please enter your text ")
# for i in range(len(text)):
#     print(text[len(text)-1-i])

# Ex5 Enter text and display only letter "A" index

# text = input("Please your text ")
# indexA=0
# for i in range(len(text)):
#     if text[i]=="A":
#         indexA=i
# print("Index A:", indexA)

# Ex6 Enter text and display counter of lowercase letter "B" and uppercase letter "B"

text = input("Please enter your text ")
countB = 0
for i in range(len(text)):
    if text[i] == "B" or text[i] == "b":
        countB +=i
print(countB)