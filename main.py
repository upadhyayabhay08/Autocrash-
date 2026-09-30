"""AUTOCRASH TEST - main program.

A Python project that checks whether a vehicle can stop
before an obstacle and, in a crash case, estimates impact information.
"""

from vehicle import get_vehicle_details
from calculations import (
    speed_to_ms,
    calculate_reaction_distance,
    calculate_braking_distance,
    calculate_braking_time,
    calculate_total_stopping_distance,
    calculate_total_stopping_time,
)
from crash_analysis import (
    check_crash,
    calculate_impact_speed,
    classify_impact_speed,
)
from person_impact import (
    get_person_details,
    get_collision_time,
    calculate_kinetic_energy,
    calculate_impact_force,
)


def main():
    print("             AUTOCRASH TEST")
    print("This is a simple crash and stopping test")

    (
        vehicle_name,
        speed,
        reaction_time,
        obstacle_distance,
        brake_type,
        deceleration,
    ) = get_vehicle_details()

    speed_ms = speed_to_ms(speed)

    print("\nVehicle Information")
    print("Vehicle:", vehicle_name)
    print("Speed:", speed, "km/h")
    print("Brake Type:", brake_type)
    print("Braking Deceleration:", deceleration, "m/s^2")

    reaction_distance = calculate_reaction_distance(speed_ms, reaction_time)
    braking_distance = calculate_braking_distance(speed_ms, deceleration)
    total_stopping_distance = calculate_total_stopping_distance(
        reaction_distance, braking_distance
    )
    braking_time = calculate_braking_time(speed_ms, deceleration)
    total_stopping_time = calculate_total_stopping_time(
        reaction_time, braking_time
    )

    print("\nReaction distance =", round(reaction_distance, 2), "metres")
    print("Braking distance =", round(braking_distance, 2), "metres")
    print(
        "Total stopping distance =",
        round(total_stopping_distance, 2),
        "metres",
    )
    print("Total stopping time =", round(total_stopping_time, 2), "seconds")

    print("\n              FINAL RESULT")

    if not check_crash(total_stopping_distance, obstacle_distance):
        print("RESULT : SAFE")
        print("The vehicle will stop before the obstacle.")

        extra_distance = obstacle_distance - total_stopping_distance
        print(
            "Distance remaining before obstacle =",
            round(extra_distance, 2),
            "metres",
        )
        print("No crash occurred.")
        print("Person impact calculation is not required.")

    else:
        print("RESULT : CRASH")
        print("The vehicle will not stop before the obstacle.")

        crash_distance = total_stopping_distance - obstacle_distance
        print(
            "Vehicle would need another",
            round(crash_distance, 2),
            "metres to completely stop.",
        )

        impact_speed_ms, crash_stage = calculate_impact_speed(
            speed_ms,
            reaction_distance,
            obstacle_distance,
            deceleration,
        )
        print("\n" + crash_stage)

        impact_speed_kmh = impact_speed_ms * 3.6
        print(
            "Approximate speed at impact =",
            round(impact_speed_kmh, 2),
            "km/h",
        )

        print("\n          PERSON CRASH INFORMATION")
        person_name, age, height_cm, weight_kg = get_person_details()

        print("\nPerson details entered:")
        print("Name:", person_name)
        print("Age:", age)
        print("Height:", height_cm, "cm")
        print("Weight:", weight_kg, "kg")

        impact_energy = calculate_kinetic_energy(weight_kg, impact_speed_ms)

        print(
            "\nApproximate kinetic energy at impact =",
            round(impact_energy, 2),
            "Joules",
        )

        print("\nFor approximate impact force,")
        print("we need an estimated collision time.")

        collision_time = get_collision_time()
        impact_force = calculate_impact_force(
            weight_kg,
            impact_speed_ms,
            collision_time,
        )

        print(
            "Approximate average impact force =",
            round(impact_force, 2),
            "Newtons",
        )

        impact_level = classify_impact_speed(impact_speed_kmh)

        print("\n              IMPACT ANALYSIS")
        if impact_level == "LOW":
            print("Impact speed is relatively low.")
        elif impact_level == "MODERATE":
            print("Impact speed is moderate.")
        elif impact_level == "HIGH":
            print("Impact speed is high.")
        else:
            print("Impact speed is very high.")

        print("Impact level :", impact_level)

    print("\n             TEST COMPLETED")


if __name__ == "__main__":
    main()
