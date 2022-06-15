from random import randint

a,b=int(input('Input first number ')), int(input('Input second number '))
try:
    if b==0:
        raise ZeroDivisionError
except:
   print("Деление на 0")
print("Исключений нет")

name = input('Enter first name ')
name_2 = input('Enter a second name ')
try:
    if len(name) <= 1:
        raise NameError('HiThere')
    
except NameError:
    print('An exception flew by!')
    raise

# определение пользовательских исключений
class Error(Exception):
    """Базовый класс для других исключений"""
    pass

class ValueTooSmallError(Error):
    """Вызывается, когда входное значение мало"""
    pass

class ValueTooLargeError(Error):
    """Вызывается, когда входное значение велико"""
    pass

# число, которое нужно угадать
number = randint(1, 6)

# игра продолжается до тех пор, 
# пока пользователь его не угадает
while True:
    try:
        i_num = int(input("Ввести число: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("Это число меньше загаданного, попробуйте еще раз!\n")
    except ValueTooLargeError:
        print("Это число больше загаданного, попробуйте еще раз!\n")

print("Поздравляю! Вы правильно угадали.")
