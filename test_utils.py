import random


def generate_test_timestamps(count=10):
    """
    Generates a list of random timestamps for testing.
    """
    return [f"{random.randint(0,23):02}:{random.randint(0,59):02}:{random.randint(0,59):02}" for _ in range(count)]


def load_timestamps(file_path):
    """
    Loads timestamps from a given file.
    """
    try:
        with open(file_path, "r") as file:
            return [line.strip() for line in file.readlines() if line.strip()]
    except FileNotFoundError:
        return []
