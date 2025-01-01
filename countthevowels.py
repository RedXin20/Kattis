vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
count = 0
input = str(input("Enter a string: "))

for i in input:
    if i in vowels:
        count += 1
print(count)
