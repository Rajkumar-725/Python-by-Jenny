'''
#WRITE A PROGRAM TO CONVERT GIVEN MARKS INTO GRADES.

student marks= jenny:92
                sakshi:91
                geeta:93
                prachi:78
                priti:62
                sita:34

        marks       grades
        91-100      A+
        81-90       A
        71-80       B+
        61-70       B
        51-60       C
        41-50       D
        below 40    F
'''

#dictionary
stud_marks={
    "jenny":92,
    "sakshi":91,
    "geeta":93,
    "prachi":78,
    "priti":62,
    "sita":34
}
"""
for i in stud_marks:
    marks=stud_marks[i]     #accessing value of key inside dictionary
    if marks>90 and marks<=100:
        print("Grade A+")

    if marks>80 and marks<=90:
        print("Grade A")

    if marks>70 and marks<=80:
        print("Grade B+")

    if marks>60 and marks<=70:
        print("Grade B")

    if marks>50 and marks<=60:
        print("Grade C")

    if marks>40 and marks<=50:
        print("Grade D")

    if marks<40:
        print("Grade F")
"""

print('\n\n\n')
grade_dict={}   #assigning a blank dictionary.

for i in stud_marks:    #1st = jenny
    marks=stud_marks[i]     #accessing value of key inside dictionary
    if marks>90:
        grade_dict[i] = "A+"     #adding the string (A+) with the key in new blank_dictionary

    elif marks>80:
        grade_dict[i] = "A"

    elif marks>70:
        grade_dict[i] = "B+"

    elif marks>60:
        grade_dict[i] = "B"

    elif marks>50:
        grade_dict[i] = "C"

    elif marks>40:
        grade_dict[i] = "D"

    elif marks<40:
        grade_dict[i] = "F"

print(grade_dict)
