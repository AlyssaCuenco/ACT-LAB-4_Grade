def assign_grade(score):
    if score > 100:
        print("Invalid score! Please enter a value between 0 and 100.")
    elif score < 0:
        print("Invalid score! Please enter a value between 0 and 100.")
    else:
        if score >= 90:
            print("Grade: A")
        elif score >= 80:
            print("Grade: B")
        elif score >= 70:
            print("Grade: C")
        elif score >= 60:
            print("Grade: D")
        elif score >= 0:
            print("Grade: F")
            
try:
    score = int(input("Please enter your score: "))
    assign_grade(score)
except:
    print("Invalid score! Please enter a value between 0 and 100.")
        
