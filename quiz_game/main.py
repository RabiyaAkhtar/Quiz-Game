print()
print('.........................WELCOME TO THE QUIZ GAME.........................')
print()

questions = ['What is the national language of Pakistan?\nA. English\nB. Urdu\nC. Persian\nD. Hebrew',
             'Which is the largest country in the world?\nA. Russia\nB. China\nC. Turkey\nD. USA',
             'Where is Niagara falls located?\nA. USA\nB. Canada\nC. Germany\nD. Both A and B',
             'What is the national animal of Pakistan?\nA. Chakor\nB. Horse\nC. Peacock\nD. Markhor',
             'In which year did World War 1 start?\nA. 1920\nB. 1918\nC. 1914\nD. 1916']

questions_lifeline = ['What is the national language of Pakistan?\nA. English\nB. Urdu',
                      'Which is the largest country in the world?\nA. Russia\nB. China',
                      'Where is Niagara falls located?\nA. USA and Canada\nB. USA and Germany',
                      'What is the national animal of Pakistan?\nA. Chakor\nB. Markhor',
                      'In which year did World War 1 start?\nA. 1920\nB. 1914']

flip_questions = ['In which year Pakistan became a nuclear power?\nA. 1992\nB. 1996\nC. 1998\nD. 2000',
                  'When did Pakistan get independence?\nA. 1945\nB. 1947\nC. 1948\nD. 1950',
                  'Which Pakistani was a high altitude mountaineer?\nA. Sajid Sadpara\nB. Ali Sadpara\nC. Samina Baig'
                  '\nD. Hussain Ali',
                  'Who is the first governor general of Pakistan?\nA. Liaquat Ali Khan\nB. Sikandar Mirza'
                  '\nC. Quaid-e-Azam\nD. Fatima Jinnah',
                  'Which is the largest province of Pakistan?\nA. Sindh\nB. KPK\nC. Balochistan\nD. Punjab',
                  ]

correctAnswers = ['B', 'A', 'D', 'D', 'C']
correctAnswersLifeline = ['B', 'A', 'A', 'B', 'B']
correctAnswersFlipQuestions = ['C', 'B', 'B', 'C', 'C']

lifeline = 0
i = 0
prize = 0

for question in questions:
    print(question)
    print()
    userChoice = input('Choose between: A: Write Answer, B: Lifeline, C: FlipOn : ').upper()
    print()
    if userChoice == "A":
        userAnswer = input('Input for answer select: ').upper()

        if userAnswer == correctAnswers[i]:
            print('You got it right')
            print('You won $100')
            print()
            prize = prize + 100
        else:
            print("You got it wrong. Please try again.")
            break

    elif userChoice == "B":
        if lifeline < 2:
            print(questions_lifeline[i])
            print()
            userAnswer = input('Input for answer select: ').upper()

            if userAnswer == correctAnswersLifeline[i]:
                print('You got it right')
                print('You won $100')
                print()
                prize = prize + 100
            else:
                print('You got it wrong. Please try again.')
            lifeline += 1
        else:
            print("Out of line lines")

    else:
        print(flip_questions[i])
        print()
        userAnswer = input('Input for answer select: ').upper()

        if userAnswer == correctAnswersFlipQuestions[i]:
            print('You got it right')
            print('You won $100')
            print()
            prize = prize + 100
        else:
            print('You got it wrong. Please try again.')

    i = i + 1
    print(".......................................................")
    print()

print(f'You won total prize of ${prize}')
