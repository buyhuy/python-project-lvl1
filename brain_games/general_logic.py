import prompt


def logic(manual, q_a):
    """general logic of project is here"""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(manual)
    count = 0
    while count < 3:
        question, answer = q_a()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == str(answer):
            print('Correct!')
            count += 1
        elif user_answer != str(answer):
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{answer}'.\nLet's try again, {name}!")
            break
    if count == 3:
        print(f'Congratulations, {name}!')


def main():
    logic()


if __name__ == '__main__':
    main()
