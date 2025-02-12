import random  # Импортируем модуль random для случайного выбора
import functools

# Класс аттракциона
class Attraction():
    def __init__(self, year_limit: int, name: str, dangerous: str, price: int):
        self.name = name  # Имя аттракциона
        self.year_limit = year_limit  # Минимальный возраст для посещения
        self.dangerous = dangerous  # Класс опасности аттракциона
        self.price = price  # Цена билета на аттракцион
        self._visitors = []  # Список посетителей, посетивших аттракцион
        self.tickets = []  # Список билетов, выданных посетителям

    def add_visitor(self, visitor: "Visitor"):
        '''Добавляет посетителя на аттракцион'''
        # Если у посетителя достаточно денег для билета
        if visitor._balance >= self.price:
            # Если возраст посетителя соответствует требованиям
            if visitor.age >= self.year_limit:
                visitor.withdraw(self.price)  # Снимаем стоимость билета с баланса посетителя
                self._visitors.append(visitor)  # Добавляем посетителя в список
                ticket = Ticket(self, visitor)  # Создаем билет для посетителя
                self.tickets.append(ticket)  # Сохраняем билет в списке аттракциона
                visitor.tickets.append(ticket)  # Добавляем билет к списку билетов посетителя
                print(f'Посетитель {visitor.name} записан на аттракцион {self.name}')
            else:
                print(f'Возраст посетителя {visitor.name} слишком мал для аттракциона {self.name}!')
        else:
            print(f'У посетителя {visitor.name} недостаточно денег, чтобы посетить аттракцион {self.name}')

    def list_visitors(self, indent=''):
        # Выводим список всех билетов (то есть посетителей), побывавших на аттракционе
        for i in range(1, len(self.tickets) + 1):
            print(f'{indent}{i}. {self.tickets[i-1]}')
        
    def __str__(self):
        # Возвращает строковое представление аттракциона
        return f'Название аттракциона: {self.name}\nЦена билета: {self.price}\nВозрастное ограничение: {self.year_limit}+\nКласс опасности: {self.dangerous}'

# Класс посетителя
class Visitor:
    def __init__(self, name: str, age: int, balance: int = 0):
        self._balance = balance  # Баланс посетителя
        self.name = name  # Имя посетителя
        self.age = age  # Возраст посетителя
        self.tickets = []  # Список билетов посетителя

    def withdraw(self, amount):
        # Уменьшаем баланс посетителя на заданную сумму
        self._balance -= amount

# Класс билета
class Ticket:
    def __init__(self, attraction: Attraction, visitor: Visitor):
        self.attraction = attraction  # Аттракцион, на который выдан билет
        self.visitor = visitor  # Посетитель, которому выдан билет

    def __str__(self):
        # Возвращает строковое представление билета
        return f'{self.visitor.name} был(а) на аттракционе {self.attraction.name}'

# Класс парка аттракционов
class Park():
    def __init__(self, name: str):
        self.name = name  # Название парка
        self._attractions = []  # Список аттракционов в парке

    def add_attraction(self, attraction: "Attraction"):
        # Добавляем аттракцион в парк
        self._attractions.append(attraction)

    def list_attractions(self):
        # Выводим список аттракционов и посетителей, побывавших на каждом из них
        for i, attraction in enumerate(self._attractions, start=1):
            print(f'{i}. {attraction.name}')
            attraction.list_visitors(indent=' - ')

# Создаем парк аттракционов
park = Park('Луна-Парк')


american_hills = Attraction(year_limit=14, name='Американские горки', price=500, dangerous='R13')
water_hills = Attraction(16, 'Водные горки', "AF12", 200)
carting = Attraction(18, 'Картинг', "PR55", 2000)
batut_park = Attraction(8, 'Батутный парк', 'R5', 300)             
labyrinth = Attraction(10, 'Лабиринт', 'C10', 150)                 
house_of_fear = Attraction(16, 'Дом страха', 'H20', 400)           
ferris_wheel = Attraction(5, 'Колесо обозрения', 'Безопасный', 100)
zipline = Attraction(12, 'Зиплайн', 'Z15', 350)                    

# Добавляем аттракционы в парк
park.add_attraction(american_hills)
park.add_attraction(water_hills)
park.add_attraction(carting)
park.add_attraction(batut_park)
park.add_attraction(labyrinth)
park.add_attraction(house_of_fear)
park.add_attraction(ferris_wheel)
park.add_attraction(zipline)

# Создаем посетителей
stepa = Visitor('Степан', 12, 1500)
anna = Visitor('Анна', 15, 200)
billy = Visitor('Уильям', 75, 600)
igor = Visitor('Игорь', 17, 1500)
vlad = Visitor('Влад', 20, 1000)
maria = Visitor('Мария', 25, 1200)
sergey = Visitor('Сергей', 30, 800)
olga = Visitor('Ольга', 14, 500)
dmitry = Visitor('Дмитрий', 19, 1100)
elena = Visitor('Елена', 16, 700)
nikolay = Visitor('Николай', 22, 900)
irina = Visitor('Ирина', 13, 600)
aleksey = Visitor('Алексей', 18, 1300)
svetlana = Visitor('Светлана', 21, 1400)

# Объединяем всех посетителей в один список
potential_visitors = [
    stepa, anna, billy, igor, vlad, maria, sergey, olga, dmitry, elena,
    nikolay, irina, aleksey, svetlana
]

# Формируем список всех аттракционов из парка для случайного выбора
attr = park._attractions

# Случайным образом добавляем посетителей на аттракционы 100 раз
for i in range(100):
    random.choice(attr).add_visitor(random.choice(potential_visitors))

# Выводим список аттракционов и посетителей, которые их посетили
park.list_attractions()

# Выводим, сколько каждый посетитель потратил денег, и сколько у него осталось
for visitor in potential_visitors:
    print(f'{visitor.name} осталсь денег - {visitor._balance}, потратил денег {functools.reduce(lambda acc, ticket: acc + ticket.attraction.price, visitor.tickets, 0)}')