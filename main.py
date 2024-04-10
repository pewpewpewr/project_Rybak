from datetime import datetime

class User:
    def __init__(self, name, email, payment_info):
        self.name = name
        self.email = email
        self.payment_info = payment_info
        self.history = []

    def make_order(self, start_location, end_location):
        order = Order(start_location, end_location, self)
        return order

class Driver:
    def __init__(self, name, vehicle, rating):
        self.name = name
        self.vehicle = vehicle
        self.rating = rating
        self.history = []

    def accept_order(self, order):
        order.assign_driver(self)
        return "Замовлення прийнято."

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
    def __init__(self, start_location, end_location, user):
        self.start_location = start_location
        self.end_location = end_location
        self.user = user
        self.status = "В очікуванні"
        self.time = datetime.now()

    def assign_driver(self, driver):
        self.driver = driver
        self.status = "Призначений"

    def complete(self, cost):
        self.cost = cost
        self.status = "Виконано"
        self.time_completed = datetime.now()

    def validate_datetime(self, datetime_str):
        try:
            datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
            return True
        except ValueError:
            return False

    def validate_payment(self, user):
        if user.payment_info:
            return True
        else:
            return False

def main():
    print("Ласкаво просимо до системи замовлення таксі!")
    user_name = input("Введіть своє ім'я: ")
    user_email = input("Введіть свій email: ")
    user_payment_info = input("Введіть свою платіжну інформацію: ")

    user = User(user_name, user_email, user_payment_info)

    while True:
        print("\n1. Зробіть нове замовлення таксі")
        print("2. Вихід")
        choice = input("Введіть свій вибір: ")

        if choice == "1":
            start_location = input("Введіть місце початку: ")
            end_location = input("Введіть кінцеве місце: ")

            order = user.make_order(start_location, end_location)
            print("Замовлення таксі виконано успішно.")
            print("Статус:", order.status)
        elif choice == "2":
            print("Дякуємо за використання системи замовлення таксі!")
            break
        else:
            print("Невірний вибір. Будь ласка спробуйте ще раз.")

if __name__ == "__main__":
    main()
