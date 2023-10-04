first_member = input('Введите первый член операции >>> ')
while True: 
    try:
        first_member = float(first_member)
    except ValueError:
        first_member = input('Пожалуйста, введите число >>> ')
    if type(first_member) is float:
        break

operate_simbol = input('Введите знак операции (+, -, *, /, ^) >>> ')

if not(operate_simbol in '+-*^/') or (len(operate_simbol) != 1): #обработка неправильного ввода знака операции
    while True:
        operate_simbol = input('Введён неправильный знак операции,\
 попробуйте снова (+, -, *, /, ^) >>> ')
        if operate_simbol in '+-*/^':
            break


second_member = input('Введите второй член операции >>> ')

while True:
    try:
        second_member = float(second_member)
    except ValueError:
        second_member = input('Пожалуйста, введите число >>> ')
    if type(second_member) is float:
        break

res = 0
inf_flag = True
val_flag = True
'''
Обработка операции методом switch - case
'''

if (operate_simbol in '+-*/^') and (len(operate_simbol) == 1) :

    if operate_simbol == '+':
        res = first_member + second_member

    elif operate_simbol == '-':
        res = first_member - second_member

    elif operate_simbol == '/':
        if second_member != 0:
            res = first_member / second_member

        else:
            print('Ваш ответ - бесконечность')
            inf_flag = True

    elif operate_simbol == '*':
        res = first_member * second_member

    elif operate_simbol == '^':
        if (first_member == 0) and (second_member < 0):
            print('Ваш ответ - Бесконечность')
            inf_flag = False
        else:
            try:
                res = first_member ** second_member
            except Exception:
                print('Ваш компьютер не поддерживает такие вычисления')
                val_flag = False

    if int(res) == res:
        res = int(res)

    if inf_flag and val_flag:
        print('Ваш результат = ', res)
    else:
        input('Нажмите любую клавишу для завершения работы')

if inf_flag and val_flag:
    #обработка конца/продолжения работы кода
    continue_flag = input('Хотите продолжить с нынешним результатом \
или закончить работу? (Y/N) >>> ')
#бесконечное продолжение работы с результатом до получения команды
    while True and inf_flag and val_flag:
        if (continue_flag == 'Y') or (continue_flag == 'y'):

            operate_simbol = input('Введите знак операции (+, -, *, /, ^) >>> ')

            if not(operate_simbol in '+-/*^') or (len(operate_simbol) != 1):
                while True:
                    operate_simbol = input('Введён неверный знак операции, \
попробуйте снова (+, -, *, /, ^) >>> ')
                    if (operate_simbol in '+-*/^') and (len(operate_simbol) == 1):
                        break

            second_member = input('Введите второй член операции >>> ')
            while True:
                try:
                    second_member = float(second_member)
                except ValueError:
                    second_member = input('Пожалуйста, введите число >>> ')
                if type(second_member) is float:
                    break
            if operate_simbol in '+-/*^':
                if operate_simbol == '+':
                    res = res + second_member
        
                elif operate_simbol == '-':
                    res = res - second_member
        
                elif operate_simbol == '/':
                    if second_member != 0:
                        res = res / second_member
                    else:
                        print('Ваш ответ - Бесконечность')
                        inf_flag = False
        
                elif operate_simbol == '*':
                    res = res * second_member
        
                elif operate_simbol == '^':
                    if (res == 0) and (second_member == 0):
                        print('Ваш ответ - Бесконечность')
                    else:
                        try:
                            res = res ** second_member
                        except Exception:
                            print('Ваш компьютер не поддерживает \
такие вычисления')
                            val_flag = False
                if int(res) == res:
                    res = int(res)
        
                if inf_flag:
                    print('Ваш результат = ', res)    
                    continue_flag = input('Хотите продолжить с нынешним результатом\
 или закончить работу? (Y/N) >>> ')
                if not(inf_flag):
                    input('Нажмите любую клавишу для завершения работы программы')
                    break
        elif (continue_flag == 'N') or (continue_flag == 'n') or not(inf_flag) or not(val_flag):
            break     
        else:
            continue_flag = input('Введён неправильный символ, попробуйте снова (Y/N) >>> ')