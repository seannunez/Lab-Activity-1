def calculator():
    global result

    Fullname = input("Full Name: ")
    student_number = input("Student#: ")
    course = input("Course: ")
    prelims = input("Prelim: ")
    midterms = input("Midterm: ")
    finals = input("Finals: ")

    prelim, midterm, final = 0.3, 0.3, 0.4
    Final_average = prelim + midterm + final
    Final_grade = round(Final_average, 2)
    Happy = "\U0001F600"
    Laugh = "\U0001F606"
    Sad = "\U0001F62D"
    if Final_average > 70:
        result = Happy
    elif Final_average == 70:
        result = Laugh
    elif Final_average < 70:
        result = Sad

    print(("\nFull name: " + Fullname) +
          ("\nStudent#: " + student_number) +
          ("\nCourse: " + course) +
          ("\nPrelim Grade: " + prelims) +
          ("\nMidterm Grade: " + midterms) +
          ("\nFinal Grade: " + finals) +
          ("\nFinal Average Grade on this course: " + str(Final_grade)) +
          ("\nResult: " + result) +
           "\n------------------------------------------------------")
    calculateagain()

def calculateagain():
    print("")
    answer = input("DO YOU WANT TO TRY AGAIN?:Y/N ")
    print("")
    if answer == "Y" or answer == "y":
        calculator()
    elif answer == "N" or answer == "n":
        quit()


calculator()
