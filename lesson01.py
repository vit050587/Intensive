# Реализуйте проверку ввода на число.
# Программа должна выводить “Correct”, если введено целое или вещественное число (в качестве разделителя
# должна использоваться одна точка).
# Во всех остальных случаях должно выводиться “Wrong”.
# Для выполнения задания необходимо изучить методы строк
# Практическое задание
#    5      3.4   3.4.1   1a    a3   -123   -5.321
# Correct Correct Wrong Wrong Wrong Correct Correct
# https://pythonworld.ru/tipy-dannyx-v-python/stroki-funkcii-i-metody-strok.html

number = input('Пожалуйста введите число: ')
test = number.replace('.', '', 1).replace('-', '', 1)
if test.isdigit():
    print('Верно')
else:
    print('Не верно')
