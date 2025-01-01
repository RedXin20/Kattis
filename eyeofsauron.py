userInput = str(input())

if len(userInput) < 4 or len(userInput) > 100:
    exit()

eye = "("
counter1 = 0
counter2 = 0

for position in userInput:
    index = userInput.index(position)
    if position in eye:
        leftEye = index
        while leftEye > -1:
            leftEye -= 1
            counter1 += 1

        rightEye = index + 1
        while rightEye < len(userInput):
            rightEye += 1
            counter2 += 1 

if counter1 == counter2:
    print("correct")
else:
    print("fix")