class BikeShop:
    def __init__(self, stock):
        self.stock = stock

    def displayBike(self):
        print("Total Bikes available:", self.stock)

    def rentBike(self, quantity):
        if quantity <= 0:
            print("Enter a positive value greater than zero.")
        elif quantity > self.stock:
            print("Enter a value less than or equal to the stock available.")
        else:
            total_price = quantity * 100
            self.stock -= quantity  # Decrease stock by rented bikes
            print(f"Total Price: {total_price}")
            print(f"Total Present Bikes: {self.stock}")

# Main program loop
if __name__ == "__main__":
    obj = BikeShop(1000)  # Starting stock of 1000 bikes
    while True:
        UserChoice = int(input('''
1. Display Stock
2. Rent a Bike
3. Exit                       
        '''))

        if UserChoice == 1:
            obj.displayBike()

        elif UserChoice == 2:
            try:
                n = int(input("Enter the number of bikes you want to rent: "))
                obj.rentBike(n)
            except ValueError:
                print("Please enter a valid number.")

        elif UserChoice == 3:
            print("Exiting the program. Have a great day!")
            break

        else:
            print("Invalid choice. Please select a valid option.")
