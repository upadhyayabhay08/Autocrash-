"""Person impact calculations and input module."""


def get_person_details():
    """Collect basic information about the person in the vehicle."""
    person_name = input("Enter name of person in vehicle: ").strip()

    while True:
        try:
            age = int(input("Enter age of person: "))
            if age <= 0:
                print("Age must be greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid whole number.")

    while True:
        try:
            height_cm = float(input("Enter height in cm: "))
            if height_cm <= 0:
                print("Height must be greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            weight_kg = float(input("Enter weight in kg: "))
            if weight_kg <= 0:
                print("Weight must be greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    return person_name, age, height_cm, weight_kg


def calculate_kinetic_energy(weight_kg, speed_ms):
    """Calculate kinetic energy using E = 1/2 mv^2."""
    return 0.5 * weight_kg * (speed_ms ** 2)


def get_collision_time():
    """Get estimated collision time, using 0.2 s for invalid/non-positive input."""
    while True:
        try:
            collision_time = float(
                input("Enter estimated collision time in seconds: ")
            )
            if collision_time <= 0:
                print("Invalid collision time.")
                print("Using 0.2 seconds as default.")
                return 0.2
            return collision_time
        except ValueError:
            print("Please enter a valid number.")


def calculate_impact_force(weight_kg, speed_ms, collision_time):
    """Calculate approximate average impact force using F = m * change in velocity / time."""
    return (weight_kg * speed_ms) / collision_time
