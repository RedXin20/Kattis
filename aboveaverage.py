testCases = int(input())

containGrades = []

for i in range(testCases):
    studentGrades = list(map(int, input().split()))
    gradeCount = studentGrades[0]
    totalScore = 0
    aboveAverage = 0
    
    for j in range(gradeCount):
        totalScore += studentGrades[j + 1]
    average = totalScore / gradeCount
    
    for student in studentGrades[1:]:
        if student > average:
            aboveAverage += 1
    
    percentage = (aboveAverage / gradeCount) * 100
    containGrades.append(percentage)

for i in containGrades:
    print("{:.3f}%".format(i))
