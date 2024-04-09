from datetime import datetime

class User:
    def __init__(self, name, email, balance=0):
        self.name = name
        self.email = email
        self.balance = balance
        self.trip_history = []

    def add_funds(self, amount):
        self.balance += amount

    def deduct_funds(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False

class Driver:
    def __init__(self, name, vehicle):
        self.name = name
        self.vehicle = vehicle
        self.rating = 0
        self.trip_history = []

class Ride:
    def __init__(self, start_location, end_location, cost, start_time, end_time, user, driver):
        self.start_location = start_location
        self.end_location = end_location
        self.cost = cost
        self.start_time = start_time
        self.end_time = end_time
        self.user = user
        self.driver = driver

class Order:
    def __init__(self, start_location, end_location, order_time, status):
        self.start_location = start_location
        self.end_location = end_location
        self.order_time = order_time
        self.status = status

    def validate_datetime(self, datetime_str):
        try:
            datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
            return True
        except ValueError:
            return False

    def validate_payment(self, user):
        return user.balance >= self.cost

user1 = User("Винник Вадим", "vadym@example.com", balance=300)
user2 = User("Аня Шкатуляк", "anya@example.com", balance=100)
user3 = User("Сем Вінчестер", "sem@example.com", balance=30)

driver1 = Driver("Ахмад", "Toyota Camry")
driver2 = Driver("Мухамед", "Honda Accord")
driver3 = Driver("Мизайло", "Ford Fusion")

order1 = Order("Довга ", "Коновальця", "2024-04-08 9:00:00", "в очікуванні")
order2 = Order("Берегова", "Мазепи", "2024-04-08 13:30:00", "підтверджено")
order3 = Order("Незалежності", "Чорновола", "2024-04-08 14:45:00", "підтверджено")

print("Доступні водії:")
for driver in [driver1, driver2, driver3]:
    print(f"Ім'я: {driver.name}, Автомобіль: {driver.vehicle}")

print("\nКористувачі, які можуть викликати таксі:")
for user in [user1, user2, user3]:
    print(f"Ім'я: {user.name}, Email: {user.email}, Баланс: {user.balance}")

print("\nІнформація про замовлення:")
for idx, order in enumerate([order1, order2, order3], start=1):
    print(f"Замовлення #{idx}:")
    print(f"Місце початку: {order.start_location}")
    print(f"Місце призначення: {order.end_location}")
    print(f"Час замовлення: {order.order_time}")
    print(f"Статус: {order.status}")
    print()
