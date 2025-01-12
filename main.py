```python
# babysleep-tracker program

def record_sleep():
    # Get input from user for sleep duration
    try:
        sleep_duration = float(input("Enter how many hours your baby slept: "))
    except ValueError:
        print("Please enter a valid number for sleep duration.")
        return

    # Append sleep duration to sleep log file
    with open("sleep_log.txt", "a") as file:
        file.write(str(sleep_duration) + "\n")
    print("Sleep duration recorded successfully.")

def view_sleep_log():
    # Read and display sleep log from file
    try:
        with open("sleep_log.txt", "r") as file:
            print("Sleep Log:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No sleep data recorded yet.")

def menu():
    print("Welcome to Baby Sleep Tracker!")
    print("1. Record Sleep")
    print("2. View Sleep Log")
    print("3. Exit")
    choice = input("Enter your choice: ")
    return choice

def main():
    while True:
        choice = menu()

        if choice == "1":
            record_sleep()
        elif choice == "2":
            view_sleep_log()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Please enter a valid choice.")

if __name__ == "__main__":
    main()
```

This program allows users to record their baby's sleep duration and view the sleep log. The sleep durations are stored in a file called "sleep_log.txt". The program includes error handling for invalid input and file not found errors. Users can interact with the program through a simple menu system.