#Реализовать класс с конструктором. Определить значения по умолчанию для некоторых аргументов, 
#чтобы их можно было не указывать в тех случаях, когда какие-то определенные значения недоступны 
#или бессмысленны.
class Person:
    def __init__(self, n, s, age=18):
        self.name = n
        self.surname = s
        self.age = age
 
@property #Используем аннотацию для создания геттера
def get_age(self):  
         print("getter method")  
         return self._age  
       # using the set function

@property # Используем аннотацию для создания cеттера
def set_age(self, y):  
         print("setter method")  
         self._age = y  
  # using the del function 

def age(self, age):
    if age in range(18, 120):
        self.__age = age
    else:
        print('You have not passed the age limit')

#Реализовать с помощью свойств инкапсуляцию.

#Добавить в класс методы, определяющие поведение.
#Реализовать производные классы (не менее двух) и методы, характерные для них.
#Реализовать отношение композиции.
#Реализовать для базового класса перегрузку двух любых стандартных операторов, например, 
#сложения и вычитания. Методы перегрузки должны возвращать новый объект того же класса

p1 = Person("Sam", "Baker")
print(p1.name, p1.surname, 'Age: ', p1.age)
