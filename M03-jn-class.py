# Defining the super class Vehicle
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

# Defining the Automobile class which inherits from Vehicle
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)  # Initializing the superclass
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    # Method to display all the information in a formatted way
    def display_info(self):
        print(f"Vehicle type: {self.vehicle_type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof}")

# Function to collect user input and create an Automobile object
def main():
    # Collecting user input
    vehicle_type = "car"  # Storing "car" in the vehicle_type
    year = input("Enter the year of the car: ")
    make = input("Enter the make of the car: ")
    model = input("Enter the model of the car: ")
    doors = input("Enter the number of doors (2 or 4): ")
    roof = input("Enter the type of roof (solid or sun roof): ")

    # Creating an Automobile object with the user input
    car = Automobile(vehicle_type, year, make, model, doors, roof)

    # Displaying the information
    print("\nHere is the information about your car:")
    car.display_info()

# Running the main function
if __name__ == "__main__":
    main()
