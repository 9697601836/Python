# Python

HW_1

1) Создать переменную типа String
2) Создать переменную типа Integer
3) Создать переменную типа Float
4) Создать переменную типа Bytes
5) Создать переменную типа List
6) Создать переменную типа Tuple
7) Создать переменную типа Set
8) Создать переменную типа Frozen set
9) Создать переменную типа Dict
10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
11) Создать 2 переменные String, создать переменную в которой суммируете эти переменные. Вывести в консоль.
12) Создать 2 переменные Integer, создать переменную в которой суммируете эти переменные. Вывести в консоль.
12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
13) Создать переменную в которой Разделите эти переменные Int. Вывести в консоль.
14) Создать переменную в которой Умножите эти переменные Int. Вывести в консоль.
15) Создать переменную в которой Разделите без остатка эти переменные Int. Вывести в консоль.
16) Создать переменную в которой надо присвоить остаток от деления этих переменные Int. Вывести в консоль.
17) (7 + 12)  3 + 7 * 4 - 44 / 2  4 расставить точки так чтобы получилось 6884.25. Вывести в консоль.

HW_1*

Циклы While
1. Создать переменную count со значением 0
2. Создать переменную range_count со значением 10
3. Создать переменную for_count со значением 0
4. Создать переменную run  со значением True
5. Сделать цикл while который будет работать пока run

     Тело цикла:

5.1 Выводить в консоль “Hello Cycle”

6. Сделать цикл while который будет работать пока run

     Тело цикла:

6.1 Выводить в консоль (“Step =”, count)

6.2 Переменной count прибавлять 1 с присвоением.
  
7. Сделать цикл while который будет работать пока count < range_count

    Тело цикла:
    
7.1 Выводить в консоль (“Step =”, count)

7.2 Переменной count прибавлять 1 с присвоением.
 
8. Сделать цикл while который будет работать пока count < range_count
    
    Тело цикла:
    
8.1 Выводить в консоль (“Step =”, count)

8.2 Переменной count прибавлять 1 с присвоением.

8.3 Сделать if с условием, если count равен 3 то выводить в консоль (“Step =”, count, ‘If body’)
   
9. Сделать цикл while который будет работать пока run

    Тело цикла:
    
9.1 Выводить в консоль (“Step =”, count)

9.2 Переменной count прибавлять 1 с присвоением.

9.3 Сделать if с условием, если count равен range_count то цикл остановится.

9.4 В теле if вывести в консоль (“STOP”, count)
   
Цилы For

10. Сделать цикл for c переменной item который будет работать пока счётчик range досчитает от for_count  до range_count
11. Сделать цикл for c переменной item который будет работать пока счётчик range досчитает от 0 до 30
    
    Тело цикла:
    
11.1 Вывести в консоль (‘Step =’, item)
   
11.2 Сделать if с условием, если item равен  5, то вывести в консоль (‘Item =’, item).
    
11.3 Сделать if с условием, если item равен  10, то вывести в консоль (‘Item =’, item).
    
11.4 Сделать if с условием, если item меньше 4, то вывести в консоль (‘Item <’, item).
   
11.5 Сделать if с условием, если item больше или равно 27, то вывести в консоль (‘Item >=’, item).
  
12. Сделать цикл for c переменной item который будет работать пока счётчик range досчитает от 0 до range_count +1

    Тело цикла:
    
12.1 Вывести в консоль (‘Step =’, item)
    
12.2 Сделать if с условием, если item равен  7.
  
       - В теле if создать переменную inner_count равную 0
     
       - В теле if вывести в консоль (‘-- inner_count =’, inner_count)
       
       - В теле if сделать ещё одни цикл for с переменной inner_item который будет работать пока счётчик range досчитает от 0 до item.
        
            Тело внутреннего цикла For:
            
            - Вывести в консоль (‘-------- Inner_Step =’, inner_item)
            
            - Сделать if если inner_item равен 5, то в inner_count присвоить inner_item.
          
            - За пределами тела предыдущего цикла вывести в консоль (‘-- inner_count =’, inner_count)
        
13. Сделать цикл for c переменной item который будет работать пока счётчик range досчитает от 0 до 20

13.1 Вывести в консоль (‘Step =’, item)
    
13.2 Сделать if с условием, если item больше  7 и item меньше 12.

        - В теле if вывести (‘If_item =’, item)
      
        - В теле if поставить continue
        
13.3 Выйти из if. Вывести в консоль (‘End_iteration =’, item)


HW_2

1) Создать 2 переменных типа String с разными значениями
2) Создать 4 переменных типа Integer с разными значениями
3) Создать 3 переменных типа Float с разными значениями
4) Реализовать 15 варианта сравнения int переменных с операторами >, <, >=, <=, !=. Pезультаты весвести в консоль.
5) Реализовать 9 варианта сравнения Float переменных с операторами >, <, >=, <=, !=. Pезультаты весвести в консоль.
6) Реализовать 10 варианта сравнения int переменных с операторами >, <, >=, <=, != и условными выражениями (end, or, not). Pезультаты весвести в консоль.
7) Сделать скрипт используя функцию input().
    1. Функция должна на вход принимать целое число.
    2. Выводить должна "Вы вели число = (введённое число) которое (меньше/больше/равно) 30"    
8) Сделать скрипт используя функцию input().
    1. Функция должна на вход принимать целое число.
    2. Внутри функции должно сгенерироваться рандомное целое число (import random)...(random.randint(1, 100))
    3. Выводить должна "Вы вели число = (введённое число) которое (меньше/больше/равно) сгенерированному числу" 
9) Сделать скрипт используя функцию input().
    1. Функция должна на вход принимать целое число.
    2. Внутри функции должно сгенерироваться рандомное 2 целых числа (import random)...(random.randint(1, 100))
    3. Выводить должна "Вы вели число = (введённое число) которое (меньше/больше/равно и меньше/больше/равно) сгенерированному числу"
----
В заданиях 7, 8, 9, сами выберите какие условные операторы и сравнения использовать.

Arithmetic
 1. Создать переменную item_1 типа integer.
 2. Создать переменную item_2 типа integer.
 3. Создать переменную result_sum в которой вы суммируете item_1 и item_2.
 4. Вывести result_sum в консоль.
 5. Создать переменную result_subtr в которой вы вычитаете большую по значению переменную из меньшей по значению.
 6. Вывести result_subtr в консоль.
 7. Создать переменную result_multi в которой вы умножаете item_1 на item_2.
 8. Вывести result_multi в консоль.
 9. Создать переменную result_exp в которой вы item_1 возводите в степень item_2.
 10. Вывести result_exp в консоль.
 11. Создать переменную result_m_exp в которой вы item_1 возводите в степень item_2 используя библиотеку math.
 12. Вывести result_m_exp в консоль.
 13. Создать переменную result_s_root в которой вы найдёте квадратный корень любой из переменной item 
 14. Вывести result_s_root в консоль.
 15. Создать переменную result_m_s_root в которой вы найдёте квадратный корень любой из переменной item используя библиотеку math.
 16. Вывести result_m_s_root в консоль.
 17. Создать переменную result_mp_s_root в которой вы найдёте квадратный корень любой из переменной item используя библиотеку math используя метод pow.
 18. Вывести result_mp_s_root в консоль.
 19. Присвоить переменной item_1 odd значение
 20. Присвоить переменной item_2 even значение
 21. Создать переменную result_division в которой вы разделите item_1 на item_2.
 22. Вывести result_division в консоль.
 23. Создать переменную result_m_floor и result_division округлить до ближайшего целого меньшего чем result_division.
 24. Вывести result_m_floor в консоль.
 25. Создать переменную result_m_ceil и result_division округлить до ближайшего целого большего чем result_division.
 26. Вывести result_m_ceil в консоль.
 27. Создать переменную result_int и result_division округлить до ближайшего целого через явное приведение.
 28. Вывести result_int в консоль.
 29. Создать переменную result_no_division_loss в которой вы разделите item_1 на item_2 без остатка.
 30. Вывести result_no_division_loss в консоль.
 31. Создать переменную result_division_loss в которой вы найдёте остаток от деления item_1 на item_2.
 32. Вывести result_division_loss в консоль.
Дальше будет реализация через арифметические действия с присваиванием.
 33. Создать переменную item_3 и присвоить ей целое число
 34. Прибавить 10 к item_3 с присвоением.
 35. Вывести item_3 в консоль.
 36. Отнять 5 от item_3 с присвоением.
 37. Вывести item_3 в консоль.
 38. Умножить item_3 на 3 с присвоением.
 39. Вывести item_3 в консоль.
 40. Разделить item_3 на 2 с присвоением.
 41. Вывести item_3 в консоль.
 42. Возвести в степень 2 item_3 с присвоением.
 43. Вывести item_3 в консоль.
 44. Найти квадратный корень item_3 с присвоением.
 45. Вывести item_3 в консоль.
 46. Присвоить остаток от деления item_3
 47. Вывести item_3 в консоль.

Boolean

 48. Создать переменную b_item_t и присвоить True
 49. Создать переменную b_item_f и присвоить False
 50. Создать переменную b_item_relult_sum и присвоить сумму b_item_t и b_item_f
 51. Вывести b_item_relult_sum в консоль.
 52. Создать переменную b_item_relult_subtr и присвоить разницу b_item_t и b_item_f
 53. Вывести b_item_relult_subtr в консоль.
 54. Создать переменную b_item_relult_multi и присвоить умножение b_item_t и b_item_f
 55. Вывести b_item_relult_multi в консоль.
 56. Создать переменную b_item_relult_division и присвоить деление b_item_t и b_item_f
 57. Вывести b_item_relult_division в консоль. (Получить ошибку)
 58. Создать переменную b_item_1_int и присвоить явное приведение b_item_t к int 
 59. Вывести b_item_1_int в консоль.
 60. Создать переменную b_item_2_int и присвоить явное приведение b_item_2 к int 
 61. Вывести b_item_2_int в консоль.
 
 HW_3

 1. Создать переменную int_item со значением 10
 2. Создать переменную comp_item со значением 18
 3. Создать переменную mult_int в которй умножите int_item на 2
 4. Создать переменную item_2 со значением True
 5. Создать переменную item_3 со значением False
 6. Создать переменную item_4 со значением 0
 7. Создать переменную item_5 со значением 1
 8. Создать переменную usd_item со значением ‘usd’
 9. Создать переменную usd_usd_rate со значением 1
 10. Создать переменную eur_item со значением ‘eur’
 11. Создать переменную usd_eur_rate со значением 0.86
 12. Создать переменную uah_item со значением ‘uah’
 13. Создать переменную usd_uah_rate со значением 26.23
 14. Создать переменную chf_item со значением ‘chf’
 15. Создать переменную usd_chf_rate со значением 0.91
 16. Создать переменную rub_item со значением ‘rub’
 17. Создать переменную usd_rub_rate со значением 71.88
 18. Создать переменную byn_item со значением ‘byn’
 19. Создать переменную usd_byn_rate со значением 2.46
 20. Сделать if в котором будет условие: если mult_int больше comp_item, то вывести в консоль (“Переменная mult_int больше”, comp_item)
 21. Создать переменную div_int в которй разделить int_item на 2
 22. Сделать if в котором будет условие: если div_int меньше comp_item, то вывести в консоль (“Переменная div_int меньше”, comp_item)
 23. Создать переменную item_1 в которй прибавить 10 к переменной int_item
 24. Сделать if в котором будет условие: если item_1 меньше comp_item, то вывести в консоль (“Переменная item_1 меньше”, comp_item), иначе, вывести в консоль (“Переменная item_1 больше или равна”, comp_item)
 25. Сделать if в котором будет условие: если item_2, то вывести в консоль (“Переменная item_2 = ”, item_2), иначе, вывести в консоль (“Переменная item_2 = ”, item_3)
 26. Сделать if в котором будет условие: если item_3, то вывести в консоль (“Переменная item_3 = ”, item_2), иначе, вывести в консоль (“Переменная item_3 = ”, item_3)
 27. Сделать if в котором будет условие: если item_5, то вывести в консоль (“Переменная item_5 = ”, item_5), иначе, вывести в консоль (“Переменная item_5 = ”, item_4)
 28. Сделать if в котором будет условие: если item_4, то вывести в консоль (“Переменная item_4 = ”, item_5), иначе, вывести в консоль (“Переменная item_4 = ”, item_4)
 29. Создать переменную currency_convertor со значением item_2
 30. Сделать if в котором будет условие: если currency_convertor, то выполнять следующие шаги задания, иначе, вывести в консоль (“Переменная currency_convertor = ”, item_3)
 31. Внутри if currency_convertor сделать следующие If условия :

31.1 Создать переменную currency_usd со значением usd_item

31.2 Создать переменную target_currency со значением eur_item

31.3 Создать переменную target_currency_amount значением 50

31.4 Создать переменную currency_result со значением 0

31.5 Сделать if в котором будет условие: если target_currency равен ‘eur’, то в теле этого if в значении переменной currency_result высчитать сколько долларов получится при target_currency_amount и usd_eur_rate. Результат вывести в консоль (target_currency_amount, eur_item, “=”, currency_result, usd_item)

31.6 Сделать elif в котором будет условие: если target_currency равен ‘uah’, то в теле этого if в значении переменной currency_result высчитать сколько долларов получится при target_currency_amount и usd_uah_rate. Результат вывести в консоль (target_currency_amount, uah_item, “=”, currency_result, uah_item)

31.7 Сделать elif с остальными валютами

31.8 Последним оставить else, при выполнений которого в консоль выведется (“Unknow currency”)

HW_4

Задачи 3 и 4 выполнить в 2-х вариантах:
1) В процедурном виде (весь код в одной процедуре).
2) В виде функций - код разбит на функции. Отдельные функции можно вынести в другие .py файлы и вызывать их в main.py предвварительно импортируя в main.py.

Задача №1
Обменник. Создать скрипт который будет запускаться из консоли 1 раз из консоли, выдавать результат и зарываться.
1. На вход обменнику вводишь количество денег int.
2. На выходе в консоль выводится отввет в таком виде:
"Ты ввёл int (Валюта)"
"конвертированная сумма в USD = int"
3. Валюту пользователя определите сами.

Задача №2
Обменник. Создать скрипт который будет запускаться из консоли 1 раз из консоли, выдавать результат и зарываться.
1. На вход обменнику вводишь количество денег int.
2. На выходе в консоль выводится отввет в таком виде:
"Ты ввёл int (Валюта)"
"Конвертированная сумма в USD = int"
"Конвертированная сумма в EUR = int"
"Конвертированная сумма в CHF = int"
"Конвертированная сумма в GBP = int"
"Конвертированная сумма в CNY = int"
3. Валюту пользователя определите сами.

Задача №3
Обменник. Создать скрипт который будет запускаться из консоли 1 раз из консоли, выдавать результат и зарываться.
1. На вход обменнику вводишь количество денег int.
2. На выходе в консоль выводится отввет в таком виде:
"Ты ввёл int (Валюта)"
"конвертированная сумма в USD = int"
"конвертированная сумма в EUR = int"
"конвертированная сумма в CHF = int"
"конвертированная сумма в GBP = int"
"конвертированная сумма в CNY = int"
3. Скрипт должен выдать сообщение
"Введите положительное число." Если число меньше 0.
"Вы ввели не число. Введите число." Если введены буквы.
"Вы ввели пустое поле. Введите число." Если введено пустое значение.
4. Валюту пользователя определите сами.

Задача №4
Обменник. Скрипт запускается в консоли и работает постоянно. Остановится нажатием ctrl+c.
1. Скрипт сначала выводит "Выберите валюту из ['USD','EUR','CHF','GBP','CNY']"
2. Пользователь вводит один из 5 вариантов ['USD','EUR','CHF','GBP','CNY']
3. Потом Скрипт выводит "Введите сумму"
4. Пользователь вводит сумму int
5. Скрипт выводит:
"Вы ввели сумму int и валюту "Валюта" "
"конвертированная сумма в "Валюта" = int"
6. Скипт должен выдать сообщение
"Введите положительное число." Если число меньше 0.
"Вы ввели не число. Введите число." Если введены буквы.
"Вы ввели пустое поле. Введите число." Если введено пустое значение.
7. После сообщеня об ошибке, скрипт должен автоматом вернуться к шагу 1.
8. Валюту пользователя определите сами.

HW_5

(Functions, Lists) - Любой начальный список минимум 70 элементов.(Есть задания где можно меньше, по усмотрению) - Все результаты выводить в консоль.

1. Написать скрипт который в создаст список целых чисел. 
2. Написать скрипт который в создаст список целых чётных чисел.
3. Написать скрипт который в создаст список целых нечётных чисел.
4. Написать скрипт который из списка целых чисел выведет чётные числа.
5. Написать скрипт который из списка целых чисел выведет нечётные числа.
6. Написать скрипт который из списка целых чисел выведет чётные числа которые делятся на 5 без остатка.
7. Написать скрипт который из списка целых чисел выведет количество  чётных чисел которые делятся на 5 без остатка.
8. Написать скрипт который в создаст список целых рандомных чисел.
9. Написать функцию которая, получив на вход любой из выше созданных списков, разобьёт его списки по 5 элементов.
10. Написать функцию которая, получив на вход список целых чисел, вернёт 2 списка, список чётных и список нечётных чисел. 
11. Написать скрипт который сгенерирует список под названием 5_stars из списков по 5 элементов целых чисел.
12. Написать скрипт который выведет список из сумм каждого внутреннего списка из  5_stars 
13. Написать функцию которая на вход получает список 5_stars, а вернёт 2 списка. В одном списке внутренние списки из 5_stars сумма чисел которых >= 100, а другой сумма чисел которых < 100. Если какого-то списка не получится, то вместо него вернуть текст “No lists”
14. Написать функцию которая получив на вход ваш возраст, выведет вам через какой срок вы сумеете отложить 10 000$, 20 000$, 30 000$, 50 000$, 100 000$ в кубышку.
15. Написать функцию которая получив на вход стартовую ЗП Junior QA и количество лет стажа выведет в консоль прогресс роста ЗП по каждому году из введенного количества лет стажа. Внутри функция учитывает дорожную карту развития скилов QA и список, полезных для компании, активностей которые может делать QA. Free implementation of function body logic
16. Написать скрипт который сгенерирует список имён пользователей. Список имён вывести в консоль.
17. Написать скрипт который сгенерирует список имён файлов. К каждому имени  файла надо прикрепить номер итерации цикла как порядковый номер. 
18.  Написать скрипт который сгенерирует список списков. Каждый элемент списка это список в котором 0-й элемент - это имя пользователя, а 1-й - элемент это дата регистрации.
19. Написать скрипт который сгенерирует список Employees списков . Каждый элемент списка - это список в котором: 0-й - элемент - это имя пользователя, 1-й - элемент - это логин, 2-й - элемент - это пароль, 3-й - элемент - это email (email тоже генерировать), 4-й - элемент - это дата регистрации
20. Написать скрипт который сгенерирует список family списков. Каждый элемент списка - это список в котором: 0-й - элемент - это логин, 1-й - элемент - это имя, 2-й - элемент - семейный статус (True, False - генерировать рандомно),
21. Написать скрипт который сгенерирует список gender списков. Каждый элемент списка - это список в котором: 0-й - элемент - это логин, 1-й - элемент - это имя, 2-й - элемент - гендер (1-м, 0-ж)
22. Написать скрипт который сгенерирует список salary списков. Каждый элемент списка - это список в котором: 0-й - элемент - это логин, 1-й - элемент - это имя, 2-й - элемент - зарплата (генерироовать от 300$ до 5000$)
23. Написать скрипт который создаст список мён работников из salary у которых ЗП от 1500$ до 3000$
24. Написать скрипт который создаст список имён мужчин из gender.
25. Написать скрипт который создаст список имён женщин из gender.
26. Написать скрипт который создаст список имён неженатых мужчин из family.
27. Написать скрипт который создаст список имён незамужних женщин из family.
28. Написать скрипт который создаст список имён неженатых мужчин с ЗП больше или равной 1500$. Используйте Employees, family, gender, salary. Реализуйте как скрипт, без функций
29. Реализуйте пункт 28 через через функции.
30. Поешьте и выспитесь)

CRUD

Доделать то, что начали на занятии по CRUD
На занятии мы сделали Create, Read
Теперь надо доделать Update, Delete.

 1. Сделать функционал для проверки уникальности Email (существует ли такой пользователь) перед добавлением нового пользователя.
 2. Добавить возможность обновления информации о существующем пользователе.
 3. Добавить возможность удалить существующего пользователя
 4. Сделать -- Help для просмотра списка возможных команд с комментариями к ним

Постарайтесь всё сделать через функции.

CSV

Вариант 1: Генерировать данные на лету, не создавая предварительных списков. Вариант 2: Генерировать предварительные списки с данными, итерируя которые вы будите записывать данные в создаваемый файл.
1. Создать пустой empty.csv файл.
2. Вариант 1. Создать digits.csv файл с 1-м полем, в котором будут 150 строк с числами от 0 до 150
3. Вариант 1. Создать names.csv файл с 1-м полем, в котором будут 100 строк с разными именами
4. Вариант 1. Создать emals.csv файл с 1-м полем, в котором будут 100 строк с разными имейлами что-то@gmail.com
5. Вариант 1. Создать nne.csv файл с 3-мя полями(Number, Name, Email ), в котором будут 100 строк. Имя и часть email до @ должны совпадать.
6. Вариант 2. Создать digits_2.csv файл с 1-м полем которое называется number, в котором будут 300 строк с числами от 10 до 310
7. Вариант 2. Создать names_2.csv файл с 1-м полем которое называется name, в котором будут 400 строк с разными именами
8. Вариант 2. Создать emals_2.csv файл с 1-м полем которое называется email, в котором будут 400 строк с разными имейлами что-то @gmail.com
9. Вариант 2. Создать nne_2.csv файл с 3-мя полями(Number, Name, Email ), в котором будут 450 строк. Имя и часть email до @ должны совпадать.
10. Добавить в файл nne_2.csv столбец Date и заполнить каждую строку текущей датой и временем. Поле даты заполнить следующим образом:
 
a) Первые 50 строк даты по годам от 1980 - 1990 (паспределие рандомно)

b) Следующие 100 строк даты по годам от 1991 - 2000 (паспределие рандомно)

с) Следующие 150 строк даты по годам от 2001 - 2010 (паспределие рандомно)

d) Следующие 150 строк даты по годам от 2011 - 2021 (паспределие рандомно) 

11. Создать файл combo.csv с полями Name, Emaill, Date. 1000 строк.

a) Соберите имена из файла nne_2.csv.

b) недостающие 550 строк имён сгенерируйте.

с) Имена расположите в алфавитном порядке.

d) Для имён из файла nne_2.csv забрать даты из nne_2.csv которые были с этими именами в nne_2.csv.

e) Остальные даты генерировать рандомно.

f) Добавить и заполнить (можно рандомно) столбы Email, Phone, Gender, Salary.

P.S. Задания специально написаны немного запутанно)) Привыкайте. Реализация и порядок выполнения каждого задания и внутренних подпунктов заданий любая, особенно в 10 и 11 задании. )) Главное чтобы работало.
