import datetime

class User:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.trips_history = []

    def register_car(self, car_model, license_plate):
        driver = Driver(self.name, car_model, license_plate)
        self.trips_history.append(driver)
        return driver

    def display_registered_cars(self):
        return [(trip.car_model, trip.license_plate) for trip in self.trips_history if isinstance(trip, Driver)]

    def display_ready_drivers(self):
        return [(driver.name, driver.car_model, driver.license_plate) for driver in self.trips_history if isinstance(driver, Driver)]


class Driver:
    def __init__(self, name, car_model, license_plate):
        self.name = name
        self.car_model = car_model
        self.license_plate = license_plate
        self.rating = 5.0
        self.trips_history = []

    def is_ready_for_order(self):
        # Check if the driver is ready for order, could implement more complex logic here
        return True


class Ride:
    def __init__(self, start_location, end_location, user, driver, fare, start_time, end_time=None):
        self.start_location = start_location
        self.end_location = end_location
        self.user = user
        self.driver = driver
        self.fare = fare
        self.start_time = start_time
        self.end_time = end_time


class Order:
    def __init__(self, start_location, end_location, user, timestamp):
        self.start_location = start_location
        self.end_location = end_location
        self.user = user
        self.timestamp = timestamp
        self.status = "Pending"

    def validate_timestamp(self):
        try:
            datetime.datetime.strptime(self.timestamp, '%Y-%m-%d %H:%M:%S')
            return True
        except ValueError:
            return False

    def calculate_fare(self):
        # Assuming a placeholder fare calculation
        base_rate_per_km = 0.1
        fare = base_rate_per_km * 10  # Assuming a fixed distance of 10 km
        return fare
    
    def validate_payment(self):
        return True  # Placeholder implementation assuming payment is always valid


user1 = User("John Doe", "john@example.com", "123-456-7890")
driver1 = Driver("Alice Smith", "Toyota Camry", "ABC123")
order1 = Order("123 Main St", "456 Elm St", user1, "2024-04-06 12:30:00")

user1.trips_history.append(order1)

# Adding four more cars and drivers
user2 = User("Діма", "dima@gmaile.com", "312-4123-5554")
car2 = user2.register_car("Honda Accord", "DEF456")
user3 = User("Назар", "nazar@gmaile.com", "547-124-2156")
car3 = user3.register_car("Ford Focus", "GHI789")
user4 = User("Андрій", "andey@example.com", "999-745-6782")
car4 = user4.register_car("Tesla Model S", "JKL012")
user5 = User("Артур", "artur@example.com", "126-145-1246")
car5 = user5.register_car("BMW X5", "MNO345")

driver2 = Driver("Максим", "Honda Accord", "DEF456")
driver3 = Driver("Микола", "Ford Focus", "GHI789")
driver4 = Driver("Дмитро", "Tesla Model S", "JKL012")
driver5 = Driver("Василь", "BMW X5", "MNO345")

print("Registered cars of user1:", user1.display_registered_cars())
print("Ready drivers:")
for driver in [driver2, driver3, driver4, driver5]:
    if driver.is_ready_for_order():
        print(driver.name, driver.car_model, driver.license_plate)
