import random

try:  # блок try-except для непредвиденных ошибок
    while True:  # цикл для ограничений по данным в соответствии с заданием
        n = int(input('Input long line: '))
        k = int(input('Input num: '))
        if 1 <= k <= n <= 2 * 10**5:
            break

    color_list = [random.choice(['B', 'W']) for _ in range(n)]  # рандомная выборка цветов и занесение в список в соответствии длины от пользователя

    # Для хранения количества 'B' окне
    current_count = 0
    for color in color_list[:k]:
        if color == 'B':
            current_count += 1

            
    min_b_count = current_count  # Минималное количество 'B' в окне

    for i in range(k, n):
        # Убираем цвет, который выходит из окна
        if color_list[i - k] == 'B':
            current_count -= 1
        # Добавляем цвет, который входит в окно
        if color_list[i] == 'B':
            current_count += 1
        
        # Обновляем минимальное количество 'B' в окне
        min_b_count = min(min_b_count, current_count)

    print(color_list)
    print(min_b_count)  # Выводим минимальное количество 'B' в окнах длиной k

except ValueError as e:  # Вывод ошибки в терминал
    print("Пожалуйста, введите число\n", e)
