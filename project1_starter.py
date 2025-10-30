"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Tavin Bailey
Date: 10/21/2025

AI Usage:
"""


def create_character(name, character_class):
    level = 1  # FIX: define level before using it

    strength, magic, health = calculate_stats(character_class, level)

    new_character = {
        "name": name,
        "class": character_class.lower(),
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": 100
    }
    return new_character


def calculate_stats(character_class, level):
    strength = 10
    magic = 4
    health = 10

    if character_class.lower() == "warrior":
        strength += 6
        magic += 0
        health += 2
    elif character_class.lower() == "mage":
        strength += 2
        magic += 10
        health += 4
    elif character_class.lower() == "rogue":
        strength += 2
        magic += 3
        health += 1
    elif character_class.lower() == "cleric":
        strength += 1
        magic += 4
        health += 1
    else:
        print("Invalid class! Defaulting to Warrior.")
        return calculate_stats("warrior", level)

    return strength, magic, health


def save_character(character, filename):
    import os

    # Check valid input
    if not isinstance(character, dict) or not filename:
        return False

    # Check directory validity (prevents FileNotFoundError)
    directory = os.path.dirname(filename)
    if directory and not os.path.exists(directory):
        return False

    # All checks passed — now safely write
    file = open(filename, "w")
    file.write(f"Character Name: {character['name']}\n")
    file.write(f"Class: {character['class']}\n")
    file.write(f"Level: {character['level']}\n")
    file.write(f"Strength: {character['strength']}\n")
    file.write(f"Magic: {character['magic']}\n")
    file.write(f"Health: {character['health']}\n")
    file.write(f"Gold: {character['gold']}\n")
    file.close()

    return True


def load_character(filename):
    import os

    if not os.path.exists(filename):
        return None

    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    character = {}
    for line in lines:
        parts = line.strip().split(": ")
        if len(parts) == 2:
            key, value = parts
            key = key.lower().replace("character name", "name")
            if key in ["level", "strength", "magic", "health", "gold"]:
                value = int(value)
            character[key] = value

    return character


def display_character(character):
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")
    print("=======================")


def level_up(character):
    character["level"] += 1
    strength, magic, health = calculate_stats(character["class"], character["level"])
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health


if __name__ == "__main__":
    name = input("Enter your character's name: ")
    character_class = input("Choose your class (Warrior, Mage, Rogue, Cleric): ")
    new_character = create_character(name, character_class)
    print("=== CHARACTER CREATOR ===")
    display_character(new_character)

    # Save to file
    save_character(new_character, "my_character.txt")

    # Load back
    loaded = load_character("my_character.txt")
    if loaded is not None:
        print("\nLoaded from file:")
        display_character(loaded)

    # Level up example
    print("\nLeveling up...")
    level_up(new_character)
    display_character(new_character)
