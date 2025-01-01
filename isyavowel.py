userInput = str(input())
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
count = 0
count2 = 0

for i in userInput:
    if i in vowels:
        count += 1

for i in userInput:
    if i in vowels or i == "y" or i == "Y":
        count2 += 1
        
print(count, count2)
