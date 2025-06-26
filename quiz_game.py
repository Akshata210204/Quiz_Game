print("Wellcome to quiz game !!")
print('NOTE: if your spelling is incorrect then it is considered as wrong answer')
score = 0
question_no = 0
playing = input('Do you want to play ? ').lower()
if playing == 'yes':
    question_no += 1
    ques = input(f'\n{question_no}. which is the most abundant gas in the atmoasphere? ').lower()
    if ques == 'nitrogen':
        score += 1
        print('correct! you got 1 point')

    else:
        print('Incorrect!')
        print(f'correct answer is --> nitrogen')

    # ------1
    question_no += 1
    ques = input(f'\n{question_no}. How many elements are present in periodic table ? ').lower()

    if ques == '118':
        score += 1
        print('correct! you got 1 point')

    else:
        print('Incorrect!')
        print(f'correct answer is --> 118')

    # -----2
    question_no += 1
    ques = input(f'\n{question_no}. Who is prime minister of India? ').lower()

    if ques == 'narendra modi':
        score += 1
        print('correct! you got 1 point')

    else:
        print('Incorrect!')
        print(f'correct answer is --> narendra modi')

    # -----3
    question_no += 1
    ques = input(f'\n{question_no}. Which is the largest planet of solar system? ').lower()

    if ques == 'jupiter':
        score += 1
        print('correct! you got 1 point')

    else:
        print('Incorrect!')
        print(f'correct answer is --> jupiter')

    # -----4
    question_no += 1
    ques = input(f'\n{question_no}. what is unit of resistance? ').lower()

    if ques == 'ohm':
        score += 1
        print('correct! you got 1 point')

    else:
        print('Incorrect!')
        print(f'correct answer is --> ohm')


# ------5

else:
    print('thankyou you are out of a game.')
    quit()

print(f'\nnumber of question is {question_no}')
print(f'your score is {score}')
try:
    percentage = (score * 100) / question_no
except ZeroDivisionError:
    print('0% quetions are correct')

print(f'{percentage}% questions are correct.')
