import numpy as np
import pandas as pd

class MenuManager:
    def __init__(self, warden_name, hostel_captain_name, mess_captain_name):
        self.warden_name = warden_name
        self.hostel_captain_name = hostel_captain_name
        self.mess_captain_name = mess_captain_name
        
        self.menu = pd.DataFrame({
            'Monday': {
                'Breakfast': ['Punjabi: Aloo Paratha, Raita'],
                'Lunch': ['South Indian: Dosa, Sambar, Chutney'],
                'Dinner': ['Non-Veg: Butter Chicken, Naan']
            },
            'Tuesday': {
                'Breakfast': ['Punjabi: Chole Bhature'],
                'Lunch': ['South Indian: Idli, Vada, Coconut Chutney'],
                'Dinner': ['Non-Veg: Biryani, Chicken Curry']
            },
            'Wednesday': {
                'Breakfast': ['Punjabi: Rajma Chawal'],
                'Lunch': ['South Indian: Masala Dosa, Coconut Chutney'],
                'Dinner': ['Chinese: Fried Rice, Manchurian']
            },
            'Thursday': {
                'Breakfast': ['Punjabi: Sarson Ka Saag, Makki Ki Roti'],
                'Lunch': ['South Indian: Uttapam, Tomato Chutney'],
                'Dinner': ['Non-Veg: Tandoori Chicken, Roti']
            },
            'Friday': {
                'Breakfast': ['Punjabi: Paneer Tikka, Naan'],
                'Lunch': ['South Indian: Pongal, Medu Vada, Sambar'],
                'Dinner': ['Chinese: Noodles, Spring Rolls']
            },
            'Saturday': {
                'Breakfast': ['Punjabi: Kadhi Pakora, Jeera Rice'],
                'Lunch': ['South Indian: Masala Uttapam, Coconut Chutney'],
                'Dinner': ['Non-Veg: Fish Curry, Rice']
            },
            'Sunday': {
                'Breakfast': ['Punjabi: Butter Paneer Masala, Naan'],
                'Lunch': ['South Indian: Upma, Kesari Bath'],
                'Dinner': ['Chinese: Manchow Soup, Chili Chicken']
            }
        })

    def main(self):
        print("\nWelcome to Hostel Mess Menu Management System")
        print(f"Warden: {self.warden_name}")
        print(f"Hostel Captain: {self.hostel_captain_name}")
        print(f"Mess Captain: {self.mess_captain_name}\n")
        
        while True:
            try:
                self.print_menu_options()
                choice = input("Enter your choice: ")

                if choice not in ['1', '2', '3', '4', '5', '6', '7']:
                    raise ValueError("Invalid choice. Please enter a number between 1 and 7.")

                self.execute_choice(choice)

            except ValueError as ve:
                print(ve)

    def print_menu_options(self):
        print("1. Display Menu for a Day and Meal Time")
        print("2. Update Menu for a Day and Meal Time")
        print("3. Add Menu for a New Day and Meal Time")
        print("4. Delete Menu for a Day and Meal Time")
        print("5. Find Average Menu Length")
        print("6. Find Most Popular Dish")
        print("7. Exit")

    def execute_choice(self, choice):
        if choice == '1':
            day = input("Enter the day: ")
            meal_time = input("Enter the meal time (Breakfast, Lunch, Dinner): ")
            self.display_menu(day, meal_time)
        elif choice == '2':
            day = input("Enter the day: ")
            meal_time = input("Enter the meal time (Breakfast, Lunch, Dinner): ")
            meals = input("Enter the menu items separated by commas: ").split(',')
            self.update_menu(day, meal_time, meals)
        elif choice == '3':
            day = input("Enter the new day: ")
            meal_time = input("Enter the meal time (Breakfast, Lunch, Dinner): ")
            meals = input("Enter the menu items separated by commas: ").split(',')
            self.add_day_menu(day, meal_time, meals)
        elif choice == '4':
            day = input("Enter the day to delete: ")
            meal_time = input("Enter the meal time (Breakfast, Lunch, Dinner): ")
            self.delete_menu(day, meal_time)
        elif choice == '5':
            self.average_menu_length()
        elif choice == '6':
            self.most_popular_dish()
        elif choice == '7':
            print("Exiting program. Goodbye!")
            exit()

    def display_menu(self, day, meal_time):
        try:
            if day not in self.menu.columns:
                raise ValueError("Invalid day. Please enter a valid day of the week.")
            if meal_time not in self.menu.index:
                raise ValueError("Invalid meal time. Please enter Breakfast, Lunch, or Dinner.")

            print(f"Menu for {day} - {meal_time}:")
            print(self.menu[day][meal_time])

        except ValueError as ve:
            print(ve)

    def update_menu(self, day, meal_time, meals):
        try:
            if day not in self.menu.columns:
                raise ValueError("Invalid day. Please enter a valid day of the week.")
            if meal_time not in self.menu.index:
                raise ValueError("Invalid meal time. Please enter Breakfast, Lunch, or Dinner.")

            self.menu[day][meal_time] = meals
            print(f"Menu for {day} - {meal_time} updated successfully.")

        except ValueError as ve:
            print(ve)

    def add_day_menu(self, day, meal_time, meals):
        try:
            if day in self.menu.columns:
                raise ValueError("Menu for this day already exists. Use update_menu to modify.")
            if meal_time not in ['Breakfast', 'Lunch', 'Dinner']:
                raise ValueError("Invalid meal time. Please enter Breakfast, Lunch, or Dinner.")

            self.menu[day][meal_time] = meals
            print(f"Menu for {day} - {meal_time} added successfully.")

        except ValueError as ve:
            print(ve)

    def delete_menu(self, day, meal_time):
        try:
            if day not in self.menu.columns:
                raise ValueError("Invalid day. Please enter a valid day of the week.")
            if meal_time not in self.menu.index:
                raise ValueError("Invalid meal time. Please enter Breakfast, Lunch, or Dinner.")

            del self.menu[day][meal_time]
            print(f"Menu for {day} - {meal_time} deleted successfully.")

        except ValueError as ve:
            print(ve)

    def average_menu_length(self):
        menu_lengths = [len(meal) for day in self.menu.columns for meal_time in self.menu.index for meal in self.menu[day][meal_time]]
        avg_length = np.mean(menu_lengths)
        print(f"The average menu length is: {avg_length:.2f} items.")

    def most_popular_dish(self):
        all_meals = [meal for day in self.menu.columns for meal_time in self.menu.index for meal in self.menu[day][meal_time]]
        unique_meals, counts = np.unique(all_meals, return_counts=True)

        if len(unique_meals) == 0:
            print("No menu items available.")
        else:
            most_popular_index = np.argmax(counts)
            print(f"The most popular dish is: {unique_meals[most_popular_index]}")

if __name__ == "__main__":
    hostel_menu_manager = MenuManager("Ms. Manju", "Ms. Hershi", "Ms. Anchal")
    hostel_menu_manager.main()
