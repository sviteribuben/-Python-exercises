#FIZZBUZZ

#Напишите программу, которая выводит числа 
#от 1 до 100. При этом вместо чисел кратных трем, 
#программа должна выводить слово FIZZ, 
#а вместо чисел кратных пяти - BIZZ. 
#Если число кратно 15 то программа должна выводить слово FIZZBIZZ.

for number in range(1, 101):
    result = ''
    if number % 3 == 0:
        result += 'FIZZ'
    if number % 5 == 0:
        result += 'BIZZ'
    print(result or number)