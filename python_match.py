bangla = int(input("Enter your Result: "))
grade = ""
match bangla:
    case 80:
        grade = "A+"
    case 70:
        grade = "A-"
    case 60:
        grade = "B"
    case 50:
        grade = "C"
    case 40:
        grade = "D"
    case _:
        grade = "fail"
print(grade)
    