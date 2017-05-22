import math


# ЗАДАЧА_1
area = 1000 # площадь участка

beds_wide = 15 # ширина грядки
beds_length = 25 # длина грядки

"""
мы исходим из того, что грядки прямоугольной правильной формы
поэтому смотрим сколько входит грядок по длине и по ширине, а не просто
сколько их влезет по площади
"""
beds_number = math.sqrt(area)//15 * math.sqrt(area)//25
free_area = area - (beds_number * beds_wide * beds_length) 
print ("Осталось ", free_area, "незанятых метров")




# ЗАДАЧА_2
plates = int(input("Количество тарелок = "))
cleanser = int (input("Количество моющего средства = "))

while cleanser >= 0.5 and plates >= 1:
    plates -= 1
    cleanser -= 0.5    
    if cleanser < 0.5 or plates < 1:
        print ("Не вымытые тарелки = ", plates)
        print ("Осталось моющего средства", cleanser)



# ЗАДАЧА_3

A = [input('x1 = '), input('y1 = ')]
B = [input('x2 = '), input('y2 = ')]
C = [input('x3 = '), input('y3 = ')]

for i in range(2):
    A[i] = int(A[i])
    B[i] = int(B[i])
    C[i] = int(C[i])



# Координаты векторов

AB = [(B[0] - A[0]), (B[1] - A[1])]
BC = [(C[0] - B[0]), (C[1] - B[1])]
CA = [(A[0] - C[0]), (A[1] - C[1])]
print ('AB = ', AB, 'BC = ', BC, 'CA = ', CA)

    
"""
метод 1.
Исходим из того, что косинус прямого угла равен нулю
Если косинус угла между одним из отрезков между даными точками равен 0, то прямоугольник прямоугольный
Добавляем сообщение об ошибке, если обнаружен угол 180 или 360 градусов
"""
test_AB_BC = (AB[0] * BC [0] + AB[1] * BC[1]) / (math.sqrt(AB[0]**2 + AB[1]**2) * math.sqrt(BC[0]**2 + BC[1]**2))
test_BC_CA = (BC[0] * CA [0] + BC[1] * CA[1]) / (math.sqrt(BC[0]**2 + BC[1]**2) * math.sqrt(CA[0]**2 + CA[1]**2))
test_CA_AB = (CA[0] * AB [0] + CA[1] * AB[1]) / (math.sqrt(CA[0]**2 + CA[1]**2) * math.sqrt(AB[0]**2 + AB[1]**2))

if test_AB_BC == 1 or test_BC_CA == 1 or test_CA_AB == 1 or test_AB_BC == -1 or test_BC_CA == -1 or test_CA_AB == -1:
    print ("Error")
elif test_AB_BC == 0 or test_BC_CA == 0 or test_CA_AB == 0:
    print ("треугольник прямоугольный")
else:
    print ("треугольник НЕ прямоугольный")


"""
метод 2.
Находим длины отрезков и проверяем треугольник по теореме Пифагора
"""
length_AB = round(math.sqrt(AB[0]**2 + AB[1]**2))
length_BC = round(math.sqrt(BC[0]**2 + BC[1]**2))
length_CA = round(math.sqrt(CA[0]**2 + BC[1]**2))
print ('AB = ', length_AB, 'BC = ', length_BC, 'CA =', length_CA)

if length_AB**2 == length_BC**2 + length_CA**2 or length_BC**2 == length_AB**2 + length_CA or length_CA**2 == length_BC**2 + length_AB**2:
    print ("треугольник прямоугольный")
else:
    print ("треугольник не прямоугольний")
