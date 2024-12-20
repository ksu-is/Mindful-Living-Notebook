import csv
import os
import datetime

# Define file path
file_path = "wellness_journal.csv"

# Check if the CSV file exists, if not, create it with headers
def initialize_journal():
    if not os.path.exists(file_path):
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Physical Activity', 'Sleep Quality', 'Diet', 'Energy Level', 'Mood', 'Stress Level', 'Mental Well-Being'])

# Function to log a new entry
def log_entry():
    print("\n--- New Wellness Entry ---")
    
    # Collect date and time
    date_today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Collect physical health details
    physical_activity = input("Physical Activity (e.g., Exercise, Steps, etc.): ")
    sleep_quality = input("Sleep Quality (1-10): ")
    diet = input("Diet (e.g., Healthy, Balanced, etc.): ")
    energy_level = input("Energy Level (1-10): ")
    
    # Collect mental health details
    mood = input("Mood (1-10, 1=Very Low, 10=Very High): ")
    stress_level = input("Stress Level (1-10, 1=Very Low, 10=Very High): ")
    mental_well_being = input("Overall Mental Well-Being (Good, Neutral, Bad): ")
    
    # Save the entry to the CSV file
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date_today, physical_activity, sleep_quality, diet, energy_level, mood, stress_level, mental_well_being])
    
    print("Entry logged successfully!")

# Function to view previous entries
def view_entries():
    print("\n--- Wellness Journal Entries ---")
    
    if os.path.exists(file_path):
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            headers = next(reader)  # Skip the header row
            for row in reader:
                print(f"\nDate: {row[0]}")
                print(f"Physical Activity: {row[1]}")
                print(f"Sleep Quality: {row[2]}")
                print(f"Diet: {row[3]}")
                print(f"Energy Level: {row[4]}")
                print(f"Mood: {row[5]}")
                print(f"Stress Level: {row[6]}")
                print(f"Mental Well-Being: {row[7]}")
                print("-" * 40)
    else:
        print("No journal entries found.")

# Function to display the main menu
def display_menu():
    print("\n--- Wellness Journal ---")
    print("1. Log a new entry")
    print("2. View past entries")
    print("3. Exit")

def main():
    # Initialize the journal file with headers if it doesn't exist
    initialize_journal()

    # Main loop for the journal application
    while True:
        display_menu()
        choice = input("Please choose an option (1, 2, or 3): ")
        
        if choice == "1":
            log_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            print("Goodbye! Stay well.")
            break
        else:
            print("Invalid choice, please select again.")
# Function to search entries by date
def search_entries():
    print("\n--- Search Journal Entries ---")
    search_date = input("Enter the date to search for (YYYY-MM-DD): ")
    
    if os.path.exists(file_path):
        found = False
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            headers = next(reader)  # Skip the header row
            for row in reader:
                if row[0].startswith(search_date):
                    found = True
                    print(f"\nDate: {row[0]}")
                    print(f"Physical Activity: {row[1]}")
                    print(f"Sleep Quality: {row[2]}")
                    print(f"Diet: {row[3]}")
                    print(f"Energy Level: {row[4]}")
                    print(f"Mood: {row[5]}")
                    print(f"Stress Level: {row[6]}")
                    print(f"Mental Well-Being: {row[7]}")
                    print("-" * 40)
        if not found:
            print(f"No entries found for {search_date}.")
    else:
        print("No journal file found. Please log an entry first.")

# Update the menu to include search functionality
def display_menu():
    print("\n--- Wellness Journal ---")
    print("1. Log a new entry")
    print("2. View past entries")
    print("3. Search entries by date")
    print("4. Exit")

# Update the main loop to handle the new option
def main():
    # Initialize the journal file with headers if it doesn't exist
    initialize_journal()

    # Main loop for the journal application
    while True:
        display_menu()
        choice = input("Please choose an option (1, 2, 3, or 4): ")
        
        if choice == "1":
            log_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            search_entries()
        elif choice == "4":
            print("Goodbye! Stay well.")
            break
        else:
            print("Invalid choice, please select again.")

if __name__ == "__main__":
    main()

