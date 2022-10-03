# 1) Создать переменную типа String
StringX = "pi"
# 2) Создать переменную типа Integer
IntegerX = 3
# 3) Создать переменную типа Float
FloatX = 3.14
# 4) Создать переменную типа Bytes
BytesX = bytes([3])
# 5) Создать переменную типа List
ListX = [3,1,4]
# 6) Создать переменную типа Tuple
TupleX = (3,1,4)
# 7) Создать переменную типа Set
SetX = set('pi')
# 8) Создать переменную типа Frozen set
Frozen_setX = frozenset('pi')
# 9) Создать переменную типа Dict
DictX = {"1":"Сижу за решеткой в темнице сырой",
"2":"Вскормленный в неволе орел молодой",
"3":"Мой грустный товарищ, махая крылом",
"4":"Кровавую пищу клюет под окном"
}
# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
print("String: ", StringX)
print("Integer: ", IntegerX)
print("Float: ", FloatX)
print("Bytes: ", BytesX)
print("List: ", ListX)
print("Tuple: ", TupleX)
print("Set: ", SetX)
print("Frozen_set: ", Frozen_setX)
print("DictX: ", DictX)
# 11) Создать 2 переменные String, создать переменную в которой суммируете эти переменные. Вывести в консоль.
String1 = "Pi "
String2 = "3,14 "
String3 = String1 + String2
print("String3: ", String3)
# 12) Создать 2 переменные Integer, создать переменную в которой суммируете эти переменные. Вывести в консоль.
Integer1 = 7
Integer2 = 770
IntegerSum = Integer1 + Integer2
print("IntegerSum: ", IntegerSum)
# 13) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
print(StringX, IntegerX)
# 14) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
print(StringX + " " + str(IntegerX))
# 15) Создать переменную в которой Разделите эти переменные Int. Вывести в консоль.
IntegerDiv1 = Integer1 / Integer2
IntegerDiv2 = Integer2 / Integer1
print("IntegerDiv1: ", IntegerDiv1, " IntegerDiv2: ", IntegerDiv2)
# 16) Создать переменную в которой Умножите эти переменные Int. Вывести в консоль.
IntegerMult = Integer1 * Integer2
print("IntegerMult: ", IntegerMult)
# 17) Создать переменную в которой Разделите без остатка эти переменные Int. Вывести в консоль.
IntegerDivWR1 = Integer1 // Integer2
IntegerDivWR2 = Integer2 // Integer1
print("IntegerDivWR1: ", IntegerDivWR1, " IntegerDivWR2: ", IntegerDivWR2)
# 18) Создать переменную в которой надо присвоить остаток от деления этих переменных Int. Вывести в консоль.
IntegerRemDiv1 = Integer1 % Integer2
IntegerRemDiv2 = Integer2 % Integer1
print("IntegerRemDiv1: ", IntegerRemDiv1, " IntegerRemDiv2: ", IntegerRemDiv2)

# Цилы While
# 1. Создать переменную count со значением 0
count = 0
# 2. Создать переменную range_count со значением 10
range_count = 10
# 3. Создать переменную for_count со значением 0
for_count = 0
# 4. Создать переменную run  со значением True
run = True
# 5. Сделать цикл while который будет работать пока run
i=0
while run:
    # Тело цикла:
    # 5.1 Выводить в консоль “Hello Cycle”
    print("Hello Cycle")
    i += 1
    if(i==10):
        break
# 6. Сделать цикл while который будет работать пока run
while run:
    # Тело цикла:
    # 6.1 Выводить в консоль (“Step =”, count)
    # 6.2 Переменной count прибавлять 1 с присвоением.
    print("Step=", count)
    count+=1
    if(count==10):
        break
# 7. Сделать цикл while который будет работать пока count < range_count
count=0
while count<range_count:
    # Тело цикла:
    # 7.1 Выводить в консоль (“Step =”, count)
    # 7.2 Переменной count прибавлять 1 с присвоением.
    print("Step=", count)
    count+=1
# 8. Сделать цикл while который будет работать пока count < range_count
count=0
while count<range_count:
    # Тело цикла:
    # 8.1 Выводить в консоль (“Step =”, count)
    # 8.2 Переменной count прибавлять 1 с присвоением.
    # 8.3 Сделать if с условием, если count равен 3 то выводить в консоль (“Step =”, count, ‘If body’)
    print("Step=", count)
    count+=1
    if(count==3):
        print("Step=", count, "If body")
# 9. Сделать цикл while который будет работать пока run
count=0
while run:
    # Тело цикла:
    # 9.1 Выводить в консоль (“Step =”, count)
    # 9.2 Переменной count прибавлять 1 с присвоением.
    # 9.3 Сделать if с условием, если count равен range_count то цикл остановится.
    # 9.4 В теле if вывести в консоль (“STOP”, count)
    print("Step=", count)
    count+=1
    if(count==range_count):
        print("STOP", count)
        break
# Цилы For
# 10. Сделать цикл for c переменной item который будет работать пока счётчик range досчитает от for_count  до range_count
for item in range(for_count, range_count):
    # Тело цикла:
    # 10.1 Вывести в консоль (‘Step =’, item)
    print("FOR Step=", item)
# 11. Сделать цикл for c переменной item который будет работать пока счётчик range досчитает от 0 до 30
for item in range(0,30):
    # Тело цикла:
    # 11.1 Вывести в консоль (‘Step =’, item)
    print("Step=", item)
    # 11.2 Сделать if с условием, если item равен  5, то вывести в консоль (‘Item =’, item).
    if(item==5):
        print("Item=", item)
    # 11.3 Сделать if с условием, если item равен  10, то вывести в консоль (‘Item =’, item).
    if(item==10):
        print("Item=", item)
    # 11.4 Сделать if с условием, если item меньше 4, то вывести в консоль (‘Item <’, item).
    if(item<4):
        print("Item <", item)
    # 11.5 Сделать if с условием, если item больше или равно 27, то вывести в консоль (‘Item >=’, item).
    if(item>27):
        print("Item >=", item)
# 12. Сделать цикл for c переменной item который будет работать пока счётчик range досчитает от 0 до range_count +1
for item in range(0,range_count+1):
    # Тело цикла:
    # 12.1 Вывести в консоль (‘Step =’, item)
    print("Step=", item)
    # 12.2 Сделать if с условием, если item равен  7.
    if(item==7):
        # - В теле if создать переменную inner_count равную 0
        inner_count=0
        # - В теле if вывести в консоль (‘-- inner_count =’, inner_count)
        print("-- inner_count =", inner_count)
        # - В теле if сделать ещё одни цикл for с переменной inner_item который будет работать пока счётчик range досчитает от 0 до item.
        for inner_item in range (0, item):
            # Тело внутреннего цикла For:
            # - Вывести в консоль (‘-------- Inner_Step =’, inner_item)
            print("-------- Inner_Step =", inner_item)
            # - Сделать if если inner_item равен 5, то в inner_count присвоить inner_item.
            if (inner_item==5):
                inner_count=inner_item
            # - За пределами тела предыдущего цикла вывести в консоль (‘-- inner_count =’, inner_count)
        print("-- inner_count =", inner_count)
# 13. Сделать цикл for c переменной item который будет работать пока счётчик range досчитает от 0 до 20
for item in range(0,20):
    # Тело цикла:
    # 13.1 Вывести в консоль (‘Step =’, item)
    print("Step=", item)
    # 13.2 Сделать if с условием, если item больше  7 и item меньше 12.
    if(item>7 and item<12):
        # - В теле if вывести (‘If_item =’, item)
        print("If_item =", item)
        # - В теле if поставить continue
        continue
    # 13.3 Выйти из if. Вывести в консоль (‘End_iteration =’, item)
    print("End_iteration =", item)