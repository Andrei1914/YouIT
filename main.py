import random

try: #блок try-except для непредвиденных ошибок
    while True: #цикл для ограничений по данным в соответсвии с заданием
        n = int(input('Input long line: '))
        k = int(input('Input num : '))
        if 1 <= k <= n <= 2 * 10**5:
            break

    color_list = [random.choice(['B', 'W']) for _ in range(n)] #рандомная выборка цветов и занесение в список в соответствии длинны от пользователя

    max_poles = 0 #переменная для хранения числа максимальной последовательности
    poles = 0 #переменная для хранения числа текущей последовательности

    for color in color_list: #цикл который отбирает толькор "B" и вычиляет макситальную последовательность с помью сравнения  макисмальной и текущей последовательности
        if color == "B":
            poles += 1
        else:
            if poles >= max_poles:
                max_poles =  poles
            poles = 0
    
    print(color_list)
    print(0 if max_poles >= k  else k - max_poles)
except ValueError as e: #Вывод ошибки в терминал
    print("Пожалуйста, введите число\n", e)
