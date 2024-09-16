class Vehicle:
    """Interface with common method move"""
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


class Car(Vehicle):
    """Concrete class car"""
    def move(self):
        return "Driving a car!"


class Bike(Vehicle):
    """Concrete class bike"""
    def move(self):
        return "Riding a bike!"


class VehicleFactory:
    """
    Creator class
    """
    @staticmethod
    def create_vehicle(vehicle_type):
        if vehicle_type == 'car':
            return Car()
        elif vehicle_type == 'bike':
            return Bike()
        else:
            raise ValueError(f"Unknown vehicle type: {vehicle_type}")


if __name__ == "__main__":
    vehicle_type = input("Enter vehicle type (car/bike): ").lower()
    try:
        vehicle = VehicleFactory.create_vehicle(vehicle_type)
        print(vehicle.move())
    except ValueError as e:
        print(e)
