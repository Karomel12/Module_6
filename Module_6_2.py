class Vehicle:
    def __init__(self,owner,__model,__color,__engine_power): #Кхм, в задании параметр __engine_power стоит на 3 месте, а должен __color
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color
        self.__COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def get_model(self):
        print(f'Модель: {self.__model}')
    def get_horsepower(self):
        print(f'Мощность двигателя: {self.__engine_power}')
    def get_color(self):
        print(f'Цвет: {self.__color}')
    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f'Владелец: {self.owner}')
    def set_color(self, new_color):
        for color in self.__COLOR_VARIANTS:
            if color.lower() == new_color.lower():
                print(f'Цвет поменен на: {new_color}')
                self.__color = new_color
                return
        else:
            print(f'Нельзя сменить цвет на {new_color}')
            return
class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Пример результата выполнения программы:
#
# Исходный код:

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства

vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)

vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
# Проверяем что поменялось

vehicle1.print_info()
