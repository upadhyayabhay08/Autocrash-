"""Basic validation tests for AutoCrash Test calculations."""

from calculations import (
    speed_to_ms,
    calculate_reaction_distance,
    calculate_braking_distance,
)
from crash_analysis import check_crash, classify_impact_speed
from person_impact import calculate_kinetic_energy, calculate_impact_force


def run_tests():
    print("AUTOMATIC TEST CASES")
    print("=" * 25)

    assert round(speed_to_ms(36), 2) == 10.00
    print("Test 1: Speed conversion - PASSED")

    assert round(calculate_reaction_distance(10, 2), 2) == 20.00
    print("Test 2: Reaction distance - PASSED")

    assert round(calculate_braking_distance(10, 5), 2) == 10.00
    print("Test 3: Braking distance - PASSED")

    assert check_crash(30, 20) is True
    print("Test 4: Crash detection - PASSED")

    assert check_crash(15, 20) is False
    print("Test 5: Safe detection - PASSED")

    assert round(calculate_kinetic_energy(70, 10), 2) == 3500.00
    print("Test 6: Kinetic energy - PASSED")

    assert round(calculate_impact_force(70, 10, 0.2), 2) == 3500.00
    print("Test 7: Impact force - PASSED")

    assert classify_impact_speed(15) == "LOW"
    assert classify_impact_speed(30) == "MODERATE"
    assert classify_impact_speed(50) == "HIGH"
    assert classify_impact_speed(70) == "VERY HIGH"
    print("Test 8: Impact classification - PASSED")

    print("\nAll tests passed successfully.")


if __name__ == "__main__":
    run_tests()
