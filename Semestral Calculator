def calculator():
    global result
    Fullname = input("Full Name: ")
    student_number = input("Student#: ")
    course = input("Course: ")
    prelims = input("Prelim: ")
    midterm = input("Midterm: ")
    finals = input("Finals: ")
    Final_average = (float(prelims) + float(midterm) + float(finals)) / 3
    Final_averages = round(Final_average, 2)
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
          ("\nMidterm Grade: " + midterm) +
          ("\nFinal Grade: " + finals) +
          ("\nFinal Average Grade on this course: " + str(Final_averages)) +
          ("\nResult: " + result) +
          '\n------------------------------------------------------')
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
