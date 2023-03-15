
def Task1():
    print('Введите два числа')
    numbers = list(map(int, input().split()))
    print(f"Наибольшее число {numbers[1]}" if numbers[0] > numbers[1] else f"Наименьшее число {numbers[0]}" )
    print(f"Наибольшее число {numbers[1]}" if numbers[0] < numbers[1] else f"Наименьшее число {numbers[0]}" )
def Task2():
    print('Введите четыре числа')
    numbers = list(map(int, input().split()))
    max = numbers[0]
    for i in numbers:
        if i > max:
            max = i
    print('Наибольшее число', max)
def Task3():
    a = int(input('Возраст Антона'))
    b = int(input('Возраст Бориса'))
    c = int(input('Возраст Виктора'))
    if a > b and a > c:
        print("Антон старше всех")
    elif b > a and b > c:
        print("Борис старше всех")
    elif c > a and c > b:
        print("Виктор старше всех")
    elif a == b and a > c:
        print("Антон и Борис старше Виктора")
    elif b == c and b > a:
        print("Борис и Виктор старше Антона")
    elif a == c and a > b:
        print("Антои и Виктор старше Бориса")
    elif a == b and b == c:
        print('Все ровестники')