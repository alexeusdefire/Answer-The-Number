import random

print('Добро пожаловать в числовую угадайку!')


def is_border_right(x: str) -> bool:

    if x.isdigit() != True:
        return False

    elif int(x) < 2:
        return False

    else:
        return True

def is_answer_right(n: str) -> bool:

    if n.isdigit() != True:
        return False

    elif int(n) > int(right) or int(n) < 1:
        return False

    else:
        return True

def the_game():

    global right
    right = input('Загадываем число от 1 до ...\n')

    while is_border_right(right) != True:
        right = input('Напишите, пожалуйста, число от 2 до... скольки хотите)\n')

    randnumb = random.randint(1, int(right))
    counter = 0

    while True:
        n = input('Введите число от 1 до ' + right + '.\n')

        while is_answer_right(n) != True:
            n = input('А может быть всё-таки введём целое число от 1 до ' + right + '?\n')

        n = int(n)
        counter += 1

        if n < randnumb:
            print('Ваше число меньше, чем то, которое я загадал\n')

        elif n > randnumb:
            print('Ваше число больше, чем то, которое я загадал\n')

        elif n == randnumb:
            restart = input('Вы угадали, поздравляю! Количество попыток: ' + str(counter) + '. Не хотите попробовать ещё? Напишите "да" или "нет"\n')

            while restart.lower() != 'да' and restart.lower() != 'нет':
                 restart = input('Я вас не понимаю. Напишите, пожалуйста, "да" или "нет"\n')

            if restart.lower() == 'да':
                the_game()

            elif restart.lower() == 'нет':
                print('Спасибо, что сыграли со мной! Ещё увидимся!')

            break

the_game()
