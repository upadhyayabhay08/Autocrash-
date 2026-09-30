"""Vehicle and brake input module for AutoCrash Test."""


def get_vehicle_details():
    """Collect basic vehicle information from the user."""
    vehicle_name = input("Enter vehicle name: ").strip()

    while True:
        try:
            speed = float(input("Enter vehicle speed in km/h: "))
            if speed < 0:
                print("Speed cannot be negative.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            reaction_time = float(
                input("Enter driver's reaction time in seconds: ")
            )
            if reaction_time < 0:
                print("Reaction time cannot be negative.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            obstacle_distance = float(
                input("Enter distance of obstacle in metres: ")
            )
            if obstacle_distance < 0:
                print("Obstacle distance cannot be negative.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    print("\nSelect type of brakes")
    print("1. Disc Brakes")
    print("2. Drum Brakes")

    while True:
        try:
            brake_choice = int(input("Enter your choice: "))
            break
        except ValueError:
            print("Please enter 1 or 2.")

    if brake_choice == 1:
        brake_type = "Disc Brakes"
        deceleration = 9.0
    elif brake_choice == 2:
        brake_type = "Drum Brakes"
        deceleration = 7.0
    else:
        print("Wrong choice entered.")
        print("Disc brakes will be used by default.")
        brake_type = "Disc Brakes"
        deceleration = 9.0

    return vehicle_name, speed, reaction_time, obstacle_distance, brake_type, deceleration
