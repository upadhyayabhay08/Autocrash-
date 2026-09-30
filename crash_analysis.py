"""Crash and impact-speed analysis module."""

import math


def check_crash(total_stopping_distance, obstacle_distance):
    """Return True when the vehicle cannot stop before the obstacle."""
    return total_stopping_distance > obstacle_distance


def calculate_impact_speed(
    speed_ms, reaction_distance, obstacle_distance, deceleration
):
    """Calculate approximate speed at the point of impact."""
    if obstacle_distance <= reaction_distance:
        return speed_ms, "Crash happened during reaction time."

    distance_after_reaction = obstacle_distance - reaction_distance

    # From v^2 = u^2 - 2as.
    speed_square = (speed_ms ** 2) - (2 * deceleration * distance_after_reaction)

    # This avoids a negative value caused by small floating-point errors.
    speed_square = max(speed_square, 0)

    return math.sqrt(speed_square), "Crash happened while braking."


def classify_impact_speed(impact_speed_kmh):
    """Classify impact speed using the project's simple categories."""
    if impact_speed_kmh < 20:
        return "LOW"
    elif impact_speed_kmh < 40:
        return "MODERATE"
    elif impact_speed_kmh < 60:
        return "HIGH"
    else:
        return "VERY HIGH"
