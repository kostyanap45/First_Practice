first_member = float(input('Введите первый член операции >>> ')) 
operate_simbol = input('Введите знак операции (+, -, *, /, ^) >>> ')
second_member = float(input('Введите второй член операции >>> '))
res = 0
inf_flag = False

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
            inf_flag = True
        else:
            res = first_member ** second_member

    if int(res) == res:
        res = int(res)

    if not(inf_flag):
        print('Ваш результат = ', res)

else: #обработка неправильного ввода знака операции
    print('Введён неправильный знак операции')
    while True:
        operate_simbol = input('Введите знак операции (+, -, *, /, ^) >>> ')
        if operate_simbol in '+-*/^':
            break
if not(inf_flag):
    #обработка конца/продолжения работы кода
    continue_flag = input('Хотите продолжить с нынешним результатом \
                          или закончить работу? (Y/N) >>> ')
#бесконечное продолжение работы с результатом до получения команды
    while True and not(inf_flag):
        if (continue_flag == 'Y') or (continue_flag == 'y'):

            operate_simbol = input('Введите знак операции (+, -, *, /, ^) >>> ')
            second_member = float(input('Введите второй член операции >>> '))

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
                        inf_flag = True
        
                elif operate_simbol == '*':
                    res = res * second_member
        
                elif operate_simbol == '^':
                    res = res ** second_member
        
                if int(res) == res:
                    res = int(res)
        
                if not(inf_flag):
                    print('Ваш результат = ', res)    
                continue_flag = input('Хотите продолжить с нынешним результатом\
                                       или закончить работу? (Y/N) >>> ')
        
        elif (continue_flag == 'N') or (continue_flag == 'n') or (inf_flag):
            break
        
        elif not(operate_simbol in '+-/*^'):
            while True:
                operate_simbol = input('Введён неверный знак операции, попробуйте снова (+, -, *, /, ^) >>> ')
                if operate_simbol in '+-*/^':
                    break
        
        else:
            continue_flag = input('Введён неправильный символ, попробуйте снова (Y/N) >>> ')