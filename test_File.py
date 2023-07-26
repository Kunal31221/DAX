from enum import Enum
from datetime import datetime


class CarCategory(Enum):
    COMPACT = 1
    PREMIUM = 2
    MINIVAN = 3


class CarRentalSystem:
    baseDayRental = 50
    kilometerPrice = 10

    def __init__(self):
        self.bookings = {}

    def register_rental(self, booking_number, customer_name, car_category, rental_time, mileage_at_pickup):
        if booking_number in self.bookings:
            return "Booking number already exists. Please use a unique booking number."

        if car_category not in CarCategory:
            return "Invalid car category."

        self.bookings[booking_number] = {
            "customer_name": customer_name,
            "car_category": car_category,
            "rental_time": rental_time,
            "mileage_at_pickup": mileage_at_pickup
        }

        return "Rental registration successful."

    def calculate_price(self, booking_number, return_time, current_mileage):
        if booking_number not in self.bookings:
            return "Booking number not found. Please provide a valid booking number."

        rental_info = self.bookings[booking_number]
        car_category = rental_info["car_category"]
        rental_time = rental_info["rental_time"]
        mileage_at_pickup = rental_info["mileage_at_pickup"]

        days_rented = (return_time - rental_time).days
        kilometers_driven = current_mileage - mileage_at_pickup

        if car_category == CarCategory.COMPACT:
            price = self.baseDayRental * days_rented
        elif car_category == CarCategory.PREMIUM:
            price = self.baseDayRental * days_rented * 1.2 + self.kilometerPrice * kilometers_driven
        elif car_category == CarCategory.MINIVAN:
            price = self.baseDayRental * days_rented * 1.7 + (self.kilometerPrice * kilometers_driven * 1.5)
        else:
            return "Invalid car category."

        return price


def run_test_cases():
    car_system = CarRentalSystem()

    print(car_system.register_rental(1, "John Doe", CarCategory.COMPACT, datetime(2023, 7, 26, 10, 0), 10000))
    print(car_system.register_rental(2, "Jane Smith", CarCategory.PREMIUM, datetime(2023, 7, 27, 12, 0), 12000))
    print(car_system.register_rental(3, "Bob Johnson", CarCategory.MINIVAN, datetime(2023, 7, 28, 15, 0), 15000))

    print(car_system.calculate_price(1, datetime(2023, 7, 28, 10, 0), 11000))  # Compact car
    print(car_system.calculate_price(2, datetime(2023, 7, 29, 12, 0), 13000))  # Premium car
    print(car_system.calculate_price(3, datetime(2023, 7, 30, 15, 0), 16000))  # Minivan car


run_test_cases()
