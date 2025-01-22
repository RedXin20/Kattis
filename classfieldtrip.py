input1 = str(input())
input2 = str(input())

word = []

for i in range(len(input1)):
    word.append(input1[i])

for i in range(len(input2)):
    word.append(input2[i])

finalVersion = "".join(word)
finalVersion = sorted(finalVersion)

for i in finalVersion:
    print(i, end="")