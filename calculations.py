"""Physics calculations used by the AutoCrash Test project."""


def speed_to_ms(speed_kmh):
    """Convert speed from km/h to m/s."""
    return speed_kmh * 1000 / 3600


def calculate_reaction_distance(speed_ms, reaction_time):
    """Calculate distance travelled during driver's reaction time."""
    return speed_ms * reaction_time


def calculate_braking_distance(speed_ms, deceleration):
    """Calculate braking distance using v^2 = u^2 - 2as."""
    return (speed_ms ** 2) / (2 * deceleration)


def calculate_braking_time(speed_ms, deceleration):
    """Calculate the approximate time required to stop during braking."""
    return speed_ms / deceleration


def calculate_total_stopping_distance(reaction_distance, braking_distance):
    """Calculate total stopping distance."""
    return reaction_distance + braking_distance


def calculate_total_stopping_time(reaction_time, braking_time):
    """Calculate total stopping time."""
    return reaction_time + braking_time
