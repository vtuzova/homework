import datetime

#ЗАДАЧА_1
#вариант1, с рукописным вводом
def NewYear (year, month, day):
    # создаем список содержащий количество дней в каждом месяце
    d_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # сюда будем общее количество прошедших с начала года дней
    all_days = 0

    days_in_year = 365

    # прописываем особенности високосного года
    if year % 4 == 0:
        d_month[1] = 29
        days_in_year = 366

    # считаем дни в полностью прошедших месяцах
    for i in range(month - 1):
        all_days += d_month[i]
    
    answ = days_in_year - all_days - day
    return('До нового года осталось ',answ)

#проверка
print(NewYear(2017, 5, 26))
print(NewYear (2012, 1, 26))
print(NewYear (2017, 1, 26))

#ЗАДАЧА_1
# вариант 2. автоматический, только на сегодняшнюю дату
def NewYear():
    my_date = datetime.date.today()
    print ('Сегодня - ', my_date)
    d_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    all_days = 0

    days_in_year = 365
    if my_date.year % 4 == 0:
        days_in_year = 366
        d_month[1] = 29

    for i in range(my_date.month - 1):
        all_days += d_month[i]
    
    answ = days_in_year - all_days - my_date.day
    return('До нового года осталось ',answ)


print(NewYear())


#ЗАДАЧА_2
'''
Написать модуль для перевода числа из одной системы счисления в другую.
'''

#модуль, для перевода из десятичной в другие системы
def export_from_10(num, system):
    a = str('')
    sh = str('ABCDEF') #добавляем библиотеку символов для 16й системы
    
    while num / system > (system - 1):
        i = num % system
        if system == 16 and i >= 10:
            if i >= 16:
                i = i - 6
            else:
                i = sh[i-10]
        
        a  += str(i)
        num = num // system
        
        
    i = num % system
    if system == 16 and i >= 10:
            if i >= 16:
                i = i - 6
            else:
                i = sh[i-10]
    a += str(i) + str(num // system)
    print(a)
    
    return (a[::-1])


print(export_from_10(22, 2))
print(export_from_10(571, 8))
print(export_from_10(7467, 16))
print('-----------------')

#модуль для перевода в десятичную систему из других
def export_to_10(num, system):
    
    num = str(num)
    k = len(num) - 1
    x = 0
    sh = ('ABCDEF')
    sh2 = [10, 11, 12, 13, 14, 15]

    
    for i in range (len(num)):
        # замена символов для 16й системы. чтобы можно было заменить, работаем не со строкой, а со списком
        if system == 16:
            num = list(num)
            for p in range(6):
                if num[i] == sh[p]:
                    num[i] = str(sh2[p])
                           
        x += int(num[i]) * pow(system, k)
        k -= 1
    return x

print(export_to_10(num = 11101000, system = 2))
print(export_to_10(num = 75013, system = 8))
print(export_to_10(num = 'FDA1', system = 16))

    


