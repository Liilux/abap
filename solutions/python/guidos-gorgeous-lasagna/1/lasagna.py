"""
Functions used in preparing Guido's gorgeous lasagna.
"""

# Task 1: constants
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


# Task 2: bake time remaining
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining."""
    return EXPECTED_BAKE_TIME - elapsed_bake_time


# Task 3: preparation time
def preparation_time_in_minutes(number_of_layers):
    """Calculate preparation time based on layers."""
    return number_of_layers * PREPARATION_TIME


# Task 4 (noch leer lassen, wenn du willst)
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate total elapsed cooking time."""
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time