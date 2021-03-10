def calculator():
    global result

    Fullname        = input("Full Name: ")
    student_number  = input("Student#: ")
    course          = input("Course: ")
    prelims         = input("Prelim: ")
    midterms        = input("Midterm: ")
    finals          = input("Finals: ")


    Final_average = (int(prelims) + int(midterms) + int(finals)) / 3
    Happy = "\U0001F600"
    Laugh = "\U0001F606"
    Sad   = "\U0001F62D"
    if Final_average > 70:
        result = Happy
    elif Final_average == 70:
        result = Laugh
    elif Final_average < 70:
        result = Sad
    print("")
    print("Hello {},({})!!! your semestral grade in {} is: {:.2f} {} "
          .format(Fullname, student_number, course, Final_average, result))
    calculateagain()


def calculateagain():
    print("")
    answer = input("DO YOU WANT TO TRY AGAIN?:Y/N ")
    print("")
    if   answer == "Y" or answer == "y":
        calculator()
    elif answer == "N" or answer == "n":
        quit()


calculator()
