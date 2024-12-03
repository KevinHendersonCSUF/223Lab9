#Kevin Henderson
#11/29/2024
from flights import *

flights = []

while True:
    menu = ["Add flight", "Print flight schedule", "Set flight schedule filename"]
    print("\n *** TUFFY TITAN FLIGHT SCHEDULE MAIN MENU")
    for i in range(len(menu)):
        print(f'{i+1}. {menu[i]}')
    print("9.", "Exit the program")
    choice = input("\nEnter menu choice: ")
    match choice:
        case "1":
            pass
        case "2":
            pass
        case "3":
            pass
        case "9":
            break
        case _:
            print("Please enter valid menu choice")
