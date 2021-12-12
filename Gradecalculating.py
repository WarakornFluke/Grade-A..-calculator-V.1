def gradecalculating(score, grade):
    
    if (score >= 80):
        grade = str("A")
    elif (score >= 70 and score <= 79):
        grade = str("B")
    elif (score >= 60 and score <= 69):
        grade = str("C")
    elif (score >= 50 and score <= 59):
        grade = str("D")
    elif (score <50):
        grade = str("F")
    else:
        grade = str("Bad score")

    return str(grade)

ss = input("Enter score: ")

strGrade = str()

try:
    fs = float(ss)
except:
    print("Bad score")
    quit()
sg = gradecalculating(fs, strGrade)

print(sg)