#A - 0101
#B - 1101
#C - 0011
#D - 1011
#E - 0111
#F - 1111

print(' ')
print('1: Из букв в цифры')
print('2: Из цифр в буквы')
print(' ')

type = int(input('Введите число: '))
print(' ')

if type == 1:
    code = input('Введите буквы: ')
    answer = []
    for i in range(len(code)):
        if code[i] == 'A':
            answer.append('0101')
        elif code[i] == 'B':
            answer.append('1101')
        elif code[i] == 'C':
            answer.append('0011')
        elif code[i] == 'D':
            answer.append('1011')
        elif code[i] == 'E':
            answer.append('0111')
        elif code[i] == 'F':
            answer.append('1111')
    print(' ')
    print('Ответ:', end=' ')
    for i in range(len(answer) - 1):
        print(answer[i], end=' ')
    print(answer[len(answer) - 1])
    print(' ')
elif type == 2:
    print('!!ВВОДИТЬ С ПРОБЕЛАМИ!!')
    print(' ')
    code = []
    code = input('Введите цифры: ')
    code = code.split()
    answer = []
    for i in range(len(code)):
        if code[i] == '0101':
            answer.append('A')
        elif code[i] == '1101':
            answer.append('B')
        elif code[i] == '0011':
            answer.append('C')
        elif code[i] == '1011':
            answer.append('D')
        elif code[i] == '0111':
            answer.append('E')
        elif code[i] == '1111':
            answer.append('F')
    print(' ')
    print('Ответ:', end=' ')
    for i in range(len(answer)):
        print(answer[i], end='')
    print('')
    print(' ')
else:
    print('!!ЧИСЛО ВВЕДЕНО НЕВЕРНО!!')
    print(' ')
a = input('Нажмите enter чтобы закрыть')
print(' ')