
#     Object oriented programming OOP


# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def start_engine(self):
#         print(f"{self.make} {self.model} engine started.")
    
# my_car = Car("Toyota", "Corolla", 2001)
# my_car.start_engine()




# class Dog:
#     species = "Canine"  # Class variable

#     def __init__(self, name):
#         self.name = name  # Instance variable

#     def bark(self):
#         print(f"{self.name} says Woof!")


#   Encapsulation 

# class BankAccount:
#     def __init__(self, owner, balance = 0):
#         self.owner = owner
#         self._balance = balance

#     def deposit(self, amount):
#         self._balance += amount
    
#     def withdraw(self, amount):
#         if amount <= self._balance:
#             self._balance -= amount
#         else: 
#             print("Insufficient balance!")

#     def get_balance(self):
#         return self._balance

# account = BankAccount("Bahtiyorjon", 2000)
# print(account.get_balance())
# account.withdraw(2500)
# account.deposit(15000)
# print(account.get_balance())




##################################################
#          EXERCISES

#   Library management

# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         self.is_borrowed = False
    
#     def __str__(self):
#         return f"'{self.title}' by {self.author}"

#     def borrow(self):
#         if not self.is_borrowed:
#             self.is_borrowed = True
#             return True
#         else:
#             return False
        
#     def return_book(self):
#         if self.is_borrowed:
#             self.is_borrowed = False
#             return True
#         else:
#             return False


# class Member:
#     def __init__(self, name):
#         self.name = name
#         self.borrowed_books = []

#     def __str__(self):
#         return self.name
    
#     def borrow_book(self, book):
#         if book.borrow():
#             self.borrowed_books.append(book)
#             print(f"{self.name} borrowed {book}")
#         else:
#             print(f"{book} is already borrowed by someone else!")

#     def return_book(self, book):
#         if book in self.borrowed_books and book.return_book():
#             self.borrowed_books.remove(book)
#             print(f"{book} has successfully been returned!")
#         else:
#             print(f"{self.name} cannot return {book} because it has not been borrowed or you don't wanna return!")

#     def list_borrowed_books(self):
#         return [str(book) for book in self.borrowed_books]


# class Library:
#     def __init__(self, name):
#         self.name = name
#         self.books = []
#         self.members = []

#     def add_book(self, book):
#         self.books.append(book)
#         print(f"{book} is added to the library.")

#     def add_member(self, member):
#         self.members.append(member)
#         print(f"{member} has joined the library.")

#     def list_available_books(self):
#         available_books = [book for book in self.books if not book.is_borrowed]
#         if available_books:
#             print("Available books in the library: ")
#             for book in available_books:
#                 print(book)
#         else:
#             print("No book is available in the library now!")
    
#     def find_book(self, title):
#         for book in self.books:
#             if book.title.lower() == title.lower():
#                 return book
#         return None


# library = Library("Bobur library")

# book1 = Book("O'tkan kunlar", "Abdulla Qodiriy") 
# book2 = Book("Hadis va hayot", "Shayx Muhammad Sodiq Muhammad Yusuf")
# book3 = Book("Sahih Buxoriy", "Imom Al-Buxoriy")

# member = Member("Bahtiyorjon")
# member2 = Member("Otabek")

# # library.add_member(member)
# # library.add_member(member2)
# library.add_book(book1)
# library.add_book(book2)
# library.add_book(book3)


# # member.borrow_book(book3)
# member2.borrow_book(book2)
# # member.borrow_book(book1)
# # member2.return_book(book2)

# book_found = library.find_book("Hadis va hayot")
# if book_found:
#     print(f"Found the book: {book_found}")
# else:
#     print("The book was not found.")


# library.list_available_books()




##################################

#   Animal Kingdom


# class Animal:
#     def __init__(self, name, species, age, color):
#         self.name = name
#         self.species = species
#         self.age = age
#         self.color = color

#     def speak(self):
#         return "Sound"
    
#     def eat(self):
#         return f"{self.name} is eating"

# class Bird(Animal):
#     def __init__(self, name, age, color, wing_span, can_fly=True):
#         super().__init__(name, "Bird", age, color)
#         self.wing_span = wing_span
#         self.can_fly= can_fly
    
#     def fly(self):
#         if self.can_fly:
#             print(f"{self.name} is flying")
#         else:
#             print(f"{self.name} cannot fly")
    
#     def speak(self):
#          return "Chirp!" if self.can_fly else "Cannot chirp"
    
#     def lay_eggs(self):
#         return f"{self.name} is laying eggs"


# class Fish(Animal):
#     def __init__(self, name, age, color, fin_count, habitat):
#         super().__init__(name, "Fish", age, color)
#         self.fin_count = fin_count
#         self.habitat = habitat

#     def swim(self):
#         return f"{self.name} is swimming"
    
#     def speak(self):
#         return "Blub blub"

#     def breathe_underwater(self):
#         return f"{self.name} can breathe underwater"


# class Mammal(Animal):
#     def __init__(self, name, age, color, fur_type, domestic):
#         super().__init__(name, "Mammal", age, color)
#         self.fur_type = fur_type
#         self.domestic = domestic

#     def walk(self):
#         return f"{self.name} is walking"

#     def nurse(self):
#         return f"{self.name} is nursing its young"
    
#     def speak(self):
#         return "Roar"



# sparrow = Bird(name="Sparrow", age=2, color="Gray", wing_span=0.3)
# goldfish = Fish(name="Goldie", age=1, color="Gold", fin_count=4, habitat="freshwater")
# lion = Mammal(name="Leo", age=5, color="Golden", fur_type="mane", domestic=False)



# print(sparrow.speak())        # Output: Chirp!
# print(sparrow.fly())          # Output: Sparrow is flying with a wingspan of 0.3 meters.

# print(goldfish.speak())       # Output: Blub blub
# print(goldfish.swim())        # Output: Goldie is swimming in freshwater.

# print(lion.speak())           # Output: Roar!
# print(lion.walk())



###################################3

#    Shopping Cart


# class Product:
#     def __init__(self, name, price, quantity):
#         if price < 0 or quantity < 0:
#             raise ValueError("Price and quantity cannot be negative")
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def get_price(self):
#         return self.price
    
#     def update_stock(self, quantity):
#         if self.quantity >= quantity:
#             self.quantity -= quantity
#             return f"Stock updated! {self.quantity} units left!"
#         else:
#             return "Not enough stock available!"
    
#     def restock(self, quantity):
#         self.quantity += quantity
#         return f"Stock restocked! {self.quantity} units available"

    

# class Cart:
#     def __init__(self):
#         self.items = []

#     def add_product(self, product, quantity):
#         if product.quantity >= quantity:
#             self.items.append({"product": product, "quantity": quantity})
#             product.update_stock(quantity)
#             return f"{quantity} {product.name}(s) added to the cart!"
#         else:
#             return "Not enough stock available!"
    
#     def remove_product(self, product, quantity):
#         for item in self.items:
#             if item["product"] == product:
#                 if item['quantity'] >= quantity:
#                     item['quantity'] -= quantity
#                     product.quantity += quantity
#                     if item['quantity'] == 0:
#                         self.items.remove(item)  # Remove the entire item when quantity reaches 0
#                     return f"{quantity} {product.name}(s) removed from the cart!"
#                 else:
#                     return "Not enough quantity in the cart to remove!"
#         return f"{product.name} is not in the cart!"

#     def cal_total(self):
#         total = 0
#         for item in self.items:
#             total += item["product"].get_price() * item["quantity"]
#         return total

#     def show_cart(self):
#         if not self.items:
#             return "Your shopping cart is empty!"
#         card_details = "Cart: details:\n"
#         for item in self.items:
#             card_details += f"{item['quantity']} x {item['product'].name} = {item['quantity'] * item['product'].get_price()}\n"
#         return card_details


# class Customer:
#     def __init__(self, name, balance):
#         self.name = name
#         self.cart = Cart()
#         self.balance = balance
    
#     def add_to_cart(self, product, quantity):
#         return self.cart.add_product(product, quantity)
        
    
#     def remove_from_cart(self, product, quantity):
#         return  self.cart.remove_product(product, quantity)

#     def view_cart(self):
#         return self.cart.show_cart()
    
#     def checkout(self):

#         total_cost = self.cart.cal_total()
#         if total_cost > 500:
#             discount_percentage = 20  # 20% discount for total > 500
#         elif total_cost > 100:
#             discount_percentage = 10  # 10% discount for total > 100
#         else:
#             discount_percentage = 0  # No discount for total <= 100
        
#         if discount_percentage > 0:
#             total_cost -= total_cost * (discount_percentage / 100)  # Apply the discount

#         if self.balance >= total_cost:
#             self.balance -= total_cost
#             self.cart.items.clear()
#             return f"Purchase successful! Total cost after discount: {total_cost} $. Balance left: {self.balance} $"
#         else:
#             return "Not enough balance to complete the purchase!"

   


# miswak = Product("Miswak", 2, 20000)
# laptop = Product("Lenovo", 1000, 20)
# shampoo = Product("Shampoo", 5, 100)


# customer = Customer("Bahtiyorjon", 2000)
# customer2 = Customer("Otabek", 1500)

# print(customer.add_to_cart(laptop, 1))
# print(customer.add_to_cart(miswak, 100))
# print(customer.view_cart())
# print(customer.checkout())

# print(customer.balance)
# print(customer.add_to_cart(shampoo, 100))






##########################################


#        School   system

# class Course:
#     def __init__(self, name, code, teacher=None):
#         self.name = name
#         self.code = code
#         self.teacher = teacher
#         self.enrolled_students = []
#         self.grades = {}

#     def enroll_student(self, student):
#         if student not in self.enrolled_students:
#             self.enrolled_students.append(student)
#             student.enroll(self)
#             return f"{student.name} has been enrolled in {self.name}"
#         return f"{student.name} is already enrolled in {self.name}"

#     def assign_grade(self, student, grade):
#         if student not in self.enrolled_students:
#             return f"{student.name} is not enrolled in {self.name}!"
#         valid_grades = ['A', 'B', 'C', 'D', 'F']
#         if grade not in valid_grades:
#             return f"Invalid grade! Please assign a valid grade: {', '.join(valid_grades)}"
#         self.grades[student] = grade
#         return f"Grade {grade} assigned to {student.name} by {self.teacher.name} for the course '{self.name}' "

#     def view_grades(self):
#         return {student.name: grade for student, grade in self.grades.items()}

# class Student:
#     def __init__(self, name, age, student_id):
#         self.name = name
#         self.age = age
#         self.student_id = student_id
#         self.enrolled_courses = []

#     def enroll(self, course):
#         if course not in self.enrolled_courses:
#             self.enrolled_courses.append(course)
#             return f"{self.name} is now enrolled in '{course.name}'"
#         else:
#             return f"Already enrolled in {course.name}"

#     def view_courses(self):
#         if not self.enrolled_courses:
#             return f"{self.name} is not enrolled in any courses."
#         return [course.name for course in self.enrolled_courses]

#     def view_grades(self):
#         grades = {}
#         for course in self.enrolled_courses:
#             grades[course.name] = course.grades.get(self, "No grade assigned")
#         return grades

# class Teacher:
#     def __init__(self, name, subject):
#         self.name = name
#         self.subject = subject
#         self.assigned_courses = []

#     def assign_course(self, course):
#         if course not in self.assigned_courses:
#             self.assigned_courses.append(course)
#             course.teacher = self
#             return f"{self.name} has been assigned to teach {course.name}"
#         return f"{self.name} is already teaching {course.name}"

#     def assign_grade(self, student, course, grade):
#         if course.teacher != self:
#             return f"{self.name} is not assigned to {course.name}!"
#         return course.assign_grade(student, grade)

# # Example Usage
# teacher1 = Teacher("Shahnozaxon", "English")
# teacher2 = Teacher("Xamidullo", "History")

# course1 = Course("History", 1234, teacher2)
# course2 = Course("English", 2345, teacher1)

# student1 = Student("Bahtiyorjon", 19, 12240219)
# student2 = Student("Otabek", 20, 12240220)

# teacher1.assign_course(course2)

# # Enroll students in courses
# print(course2.enroll_student(student1))
# print(course1.enroll_student(student2))

# # View enrolled courses for students
# print(student1.view_courses())  # View courses for Bahtiyorjon
# print(student2.view_courses())  # View courses for Otabek



# # Assign grades
# print(teacher1.assign_grade(student1, course2, "A"))
# print(course2.view_grades())

# # View grades for students

# print(course2.enroll_student(student2))

# print(teacher1.assign_grade(student2, course2, "B"))

# print(course1.enroll_student(student1))
# print(student1.view_grades())
# print(teacher2.assign_grade(student1, course1, "A"))
# print(student2.view_grades())





######################################################33

#             Banking application


# class BankAccount:
#     def __init__(self, account_num, balance = 0):
#         self.account_num = account_num
#         self.balance = balance
#         self.transactions = []

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             self.transactions.append(f"Deposited: {amount} $")
#             return f"{amount} $ is deposited to your account!"
#         else:
#             return "Please enter a positive amount!"

#     def withdraw(self, amount):
#         if amount <= 0:
#             return "Please enter a positive amount!"
#         elif amount <= self.balance:
#             self.balance -= amount
#             self.transactions.append(f"Withdrawn: {amount} $")
#             return f"{amount} $ has been withdrawn! Balance left: {self.balance} $"
#         else:   
#             return f"Insufficient funds in the balance!"

#     def transfer(self, amount, transfer_account):
#         if amount <= 0:
#             return "Please enter a positive amount!"
#         elif amount <= self.balance:
#             self.balance -= amount
#             transfer_account.balance += amount
#             self.transactions.append(f"Sent: {amount} $ to account {transfer_account.account_num}")
#             transfer_account.transactions.append(f"Received: {amount}$ from account {self.account_num}")
#             return f"{amount} has been transferred to account {transfer_account.account_num}. Balance left: {self.balance} $"
#         else:
#             return f"Insufficient funds to transfer!"

#     def check_balance(self):
#         return f"You balance is {self.balance} $!"

#     def view_transactions(self):
#         if not self.transactions:
#             return "No transactions made so far!"
#         else:
#             return "\n".join(self.transactions)


# def main():
#     print("Welcome to the Bank!")
    
#     # Example of creating bank accounts
#     account1 = BankAccount(120120, 2000)
#     account2 = BankAccount(120140, 300)

#     while True:
#         print("\nAvailable Options:")
#         print("1. Deposit")
#         print("2. Withdraw")
#         print("3. Transfer")
#         print("4. Check Balance")
#         print("5. View Transactions")
#         print("6. Exit")

#         choice = input("Enter your choice (1-6): ")

#         if choice == "1":
#             amount = float(input("Enter amount to deposit: "))
#             print(account1.deposit(amount))

#         elif choice == "2":
#             amount = float(input("Enter amount to withdraw: "))
#             print(account1.withdraw(amount))

#         elif choice == "3":
#             amount = float(input("Enter amount to transfer: "))
#             print(account1.transfer(amount, account2))

#         elif choice == "4":
#             print(account1.check_balance())

#         elif choice == "5":
#             print(account1.view_transactions())

#         elif choice == "6":
#             print("Thank you for using our Bank. Goodbye!")
#             break

#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()




#########################################################3


###         Weather app



# import requests
# import json
# import os
# from datetime import datetime

# class WeatherStation:
#     def __init__(self):
#         self.daily_data = []  # Stores daily readings as tuples: (temperature, humidity, wind_speed)
#         self.file_name = 'weather_data.json'

#     def get_weather_data(self, city="Incheon", api_key="dc8e29073239332c089f069d7bfc0a5c"):
#         """Fetches real-time weather data using OpenWeatherMap API."""
#         url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        
#         try:
#             response = requests.get(url)
#             data = response.json()

#             if response.status_code == 200:
#                 # Extracting the relevant data from the API response
#                 temperature = data['main']['temp']
#                 humidity = data['main']['humidity']
#                 wind_speed = data['wind']['speed']

#                 # Display the real-time data
#                 print(f"Real-time Weather in {city}:")
#                 print(f"Temperature: {temperature}°C, Humidity: {humidity}%, Wind Speed: {wind_speed} m/s")
#                 return temperature, humidity, wind_speed
#             else:
#                 print(f"Error fetching weather data for {city}: {data.get('message', 'Unknown error')}")
#                 return None

#         except Exception as e:
#             print(f"Error fetching data: {e}")
#             return None

#     def save_data_to_file(self):
#         """Saves daily weather data to a JSON file."""
#         try:
#             # Create or update the JSON file with the daily data
#             with open(self.file_name, 'w') as file:
#                 json.dump(self.daily_data, file, indent=4)
#             print(f"Weather data saved to {self.file_name}!")
#         except Exception as e:
#             print(f"Error saving data: {e}")

#     def load_data_from_file(self, file_name="weather_data.json"):
#         """Loads weather data from the JSON file."""
#         if os.path.exists(file_name):  # Check if the file exists
#             try:
#                 with open(file_name, 'r') as file:
#                     data = file.read().strip()  # Read the file and strip any excess whitespace
#                     if data:  # If the file is not empty
#                         self.daily_data = json.loads(data)
#                         print(f"Weather data loaded from {file_name}!")
#                     else:
#                         print(f"{file_name} is empty, no data to load.")
#             except Exception as e:
#                 print(f"Error loading data: {e}")
#         else:
#             print(f"{file_name} not found, starting with an empty dataset.")

#     def display_data(self):
#         """Displays the saved weather data."""
#         if not self.daily_data:
#             print("No weather data available.")
#         else:
#             print("Saved weather data:")
#             for entry in self.daily_data:
#                 if isinstance(entry, dict):  # Check if entry is a dictionary
#                     # Handle the dictionary format with keys
#                     print(f"Timestamp: {entry['timestamp']}, Temperature: {entry['temperature']}°C, "
#                           f"Humidity: {entry['humidity']}%, Wind Speed: {entry['wind_speed']} m/s")
#                 elif isinstance(entry, list):  # Check if entry is a list (tuple format)
#                     # Handle the list format (tuple format)
#                     print(f"Temperature: {entry[0]}°C, Humidity: {entry[1]}%, Wind Speed: {entry[2]} m/s")
#                 else:
#                     print(f"Unknown entry format: {entry}")

#     def update_data(self, city="Incheon"):
#         """Update weather data by fetching real-time data and saving it."""
#         weather = self.get_weather_data(city)
#         if weather:
#             temperature, humidity, wind_speed = weather
#             # Add the current data to the daily data list
#             self.daily_data.append({
#                 'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#                 'temperature': temperature,
#                 'humidity': humidity,
#                 'wind_speed': wind_speed
#             })
#             self.save_data_to_file()

#     def delete_file(self):
#         """Deletes the JSON file after exiting."""
#         if os.path.exists(self.file_name):
#             try:
#                 os.remove(self.file_name)
#                 print(f"{self.file_name} deleted after exit!")
#             except Exception as e:
#                 print(f"Error deleting file: {e}")


# def main():
#     # Initialize WeatherStation object
#     station = WeatherStation()
#     station.load_data_from_file()

#     while True:
#         print("\nWeather Station Menu")
#         print("1. Fetch and record current weather")
#         print("2. Fetch and record weather for a specific city")
#         print("3. View saved weather data")
#         print("4. Exit")
#         choice = input("Enter your choice: ")

#         if choice == '1':
#             # Update weather data by fetching from the API and save it (default city: Incheon)
#             station.update_data()
#         elif choice == '2':
#             # Ask for a city and update weather data for that city
#             city = input("Enter the city name: ")
#             station.update_data(city)
#         elif choice == '3':
#             # Display the saved weather data
#             station.display_data()
#         elif choice == '4':
#             # Delete the JSON file before exiting
#             station.delete_file()
#             print("Exiting the application.")
#             break
#         else:
#             print("Invalid choice! Please select a valid option.")

# if __name__ == "__main__":
#     main()




###################################################################

#####      Hotel Reservation system

# from datetime import datetime

# class Room:
#     def __init__(self, number, room_type, price_per_night, is_available=True):
#         self.number = number
#         self.type = room_type
#         self.is_available = is_available
#         self.price_per_night = price_per_night

#     def check_availability(self):
#         return self.is_available
    
#     def reserve_room(self):
#         if self.is_available:
#             self.is_available = False
#             return f"{self.type} room with number {self.number} is reserved now!"
#         else:
#             return f"{self.type} room with number {self.number} is already reserved!"

#     def release_room(self):
#         if not self.is_available:
#             self.is_available = True
#             return f"{self.type} room with number {self.number} is available now!"
#         else:
#             return f"{self.type} room with number {self.number} is already available!"

#     def __str__(self):
#         return f"Room {self.number} - {self.type} - {'Available' if self.is_available else 'Reserved'}"

# class Guest:
#     def __init__(self, name, guest_id, contact):
#         self.name = name
#         self.id = guest_id
#         self.contact = contact
#         self.bookings = []

#     def add_booking(self, booking):
#         self.bookings.append(booking)

#     def get_booking_history(self):
#         history = [f"Booking ID: {b.booking_id}, Room: {b.room.number}, Check-in: {b.check_in_date}, Check-out: {b.check_out_date}" for b in self.bookings]
#         return history if history else "No booking history available!"

#     def __str__(self):
#         return f"Guest {self.name} - ID: {self.id}"

# class Booking:
#     def __init__(self, booking_id, guest, room, check_in_date, check_out_date):
#         self.booking_id = booking_id
#         self.guest = guest
#         self.room = room
#         self.total_cost = 0  
#         self.check_in_date = check_in_date
#         self.check_out_date = check_out_date
#         self.guest.add_booking(self)
#         self.calc_cost()
        
#     def calc_cost(self):
#         if self.check_out_date <= self.check_in_date:
#             raise ValueError("Check-out date must be after check-in date.")
#         nights = (self.check_out_date - self.check_in_date).days
#         self.total_cost = nights * self.room.price_per_night

#     def confirm_booking(self):
#         if self.room.is_available:
#             self.room.is_available = False
#             return f"Booking {self.booking_id} confirmed for {self.guest.name}."
#         else:
#             return f"Room {self.room.number} is not available for booking."

#     def show_booking_details(self):
#         return (f"Booking ID: {self.booking_id}\n"
#                 f"Guest: {self.guest.name}\n"
#                 f"Room Number: {self.room.number}, Type: {self.room.type}\n"
#                 f"Check-in: {self.check_in_date}, Check-out: {self.check_out_date}\n"
#                 f"Total Cost: {self.total_cost}")
    
#     def cancel_booking(self):
#         # Set room availability back to True
#         if not self.room.is_available:
#             self.room.is_available = True
#             # Optionally, remove this booking from guest’s booking history
#             if self in self.guest.bookings:
#                 self.guest.bookings.remove(self)
#             return f"Booking {self.booking_id} for room {self.room.number} has been canceled."
#         else:
#             return f"Booking {self.booking_id} is already canceled or room is available."

#     def __str__(self):
#         return f"Booking {self.booking_id} - Room {self.room.number} - Guest: {self.guest.name}"

# # Creating room and guest objects
# room = Room(100, "villa", 200)
# guest = Guest("Bahtiyorjon", 12201, "+8210210")

# # Define check-in and check-out dates
# check_in = datetime(2024, 12, 1)
# check_out = datetime(2024, 12, 5)

# # Create booking object
# booking = Booking("B001", guest, room, check_in, check_out)

# # Confirm booking and print details
# print(booking.confirm_booking())
# booking.cancel_booking()
# print(booking.booking_id)
# # Print the total cost of the booking
# print(f"Total cost: ${booking.total_cost}")




#########################################################


#         chat bot with api with class   













