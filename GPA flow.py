grade_point_avg = float(input("What was the applicants GPA?"))
inst_app = input("Is the student going to be educated at a vetted institution?")

if grade_point_avg >= 3.7:
    if inst_app == "yes":
        print("The applicant qualifies for a low APR student loan.")
    else:
        print("The applicant doesn't qualify since they have not been accepted into an approved institution")
else:
    print("The applicant did not have a high enough GPA to qualify")
    