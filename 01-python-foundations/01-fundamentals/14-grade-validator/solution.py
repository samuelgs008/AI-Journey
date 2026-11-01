# 14 - Grade Validator
average = 0
filled = False
valid_grade_task = False
grade_calculation = False


while grade_calculation == False:
    n = float(input())

    if float(0) > n or n > float(10):
        print("invalid grade")
        continue

    if filled == False: 
        average = n
        filled = True

    else: 
        average = (average + n) / 2
        valid_grade_task = True
        print(f"AVERAGE = {average:.2f}")

    while valid_grade_task == True:
        print("new calculation (1-yes 2-no)")
        answer = input()
        if(answer == '1'):
            average = 0
            filled = False
            valid_grade_task = False
        elif(answer == '2'):
            grade_calculation = True
            valid_grade_task = False