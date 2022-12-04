#Вводим с клавиатуры целое число - это зарплата.
#Нужно вывести в консоль -  Минимальное кол-во  купюр, которыми можно выдать ЗП.
#И сколько, и каких бухгалтер выдаст 25 рублевых купюр,  10 рублевых, 3 рублевых и 1 рублевых

salary = int(input('Введите зарплату: '))
count = 0
while salary>0:
    if salary>25:
        print(f'25 рублевых купюр - {salary // 25}')
        count += salary//25
        salary %= 25
    elif salary>=10:
        print(f'10 рублевых купюр - {salary // 10}')
        count += salary // 10
        salary %= 10
    elif salary >= 3:
        print(f'3 рублевых купюр - {salary // 3}')
        count += salary // 3
        salary %= 3
    else:
        print(f'1 рублевых купюр - {salary // 1}')
        count += salary // 1
        salary %= 1
print(f'Колличество купюр -', count)
