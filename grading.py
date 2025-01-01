gradePercent = list(map(int, input().split()))
studentPercent = int(input())

A = gradePercent[0]
B = gradePercent[1]
C = gradePercent[2]
D = gradePercent[3]
E = gradePercent[4]

if studentPercent < E:
    grade = "F"
else:
    if studentPercent < D:
        grade = "E"
    else:
        if studentPercent < C:
            grade = "D"
        else:
            if studentPercent < B:
                grade = "C"
            else:
                if studentPercent < A:
                    grade = "B"
                else:
                    grade = "A"
print(grade)


# Alternative method, not kattis friendly

"""
A,B,C,D,E, studentPercent = list(map(int, input().split()))

if studentPercent < E:
    grade = "F"
else:
    if studentPercent < D:
        grade = "E"
    else:
        if studentPercent < C:
            grade = "D"
        else:
            if studentPercent < B:
                grade = "C"
            else:
                if studentPercent < A:
                    grade = "B"
                else:
                    grade = "A"
print(grade)
"""