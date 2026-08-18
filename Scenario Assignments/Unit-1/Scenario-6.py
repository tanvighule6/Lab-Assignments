class Vehicle:
    def __init__(self, vehicle_number, brand, price, category):
        self.vehicle_number = vehicle_number
        self.brand = brand
        self.price = price
        self.category = category


class Showroom:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def display_vehicles(self):
        print("\n--- Vehicle Showroom ---")
        for vehicle in self.vehicles:
            print("Vehicle Number:", vehicle.vehicle_number)
            print("Brand:", vehicle.brand)
            print("Price:", vehicle.price)
            print("Category:", vehicle.category)
            print("------------------------")


# Create showroom
showroom = Showroom()

# Add vehicles
showroom.add_vehicle(Vehicle("MH12AB1234", "BMW", 7500000, "Luxury"))
showroom.add_vehicle(Vehicle("MH14CD5678", "Maruti", 800000, "Economy"))
showroom.add_vehicle(Vehicle("MH12EF9012", "Mercedes", 9500000, "Luxury"))
showroom.add_vehicle(Vehicle("MH14GH3456", "Tata", 1200000, "Economy"))

# Display all vehicles
showroom.display_vehicles()

--- Vehicle Showroom ---
Vehicle Number: MH12AB1234
Brand: BMW
Price: 7500000
Category: Luxury
------------------------
Vehicle Number: MH14CD5678
Brand: Maruti
Price: 800000
Category: Economy
------------------------
Vehicle Number: MH12EF9012
Brand: Mercedes
Price: 9500000
Category: Luxury
------------------------
Vehicle Number: MH14GH3456
Brand: Tata
Price: 1200000
Category: Economy
------------------------
