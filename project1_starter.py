"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Tavin Bailey
Date: 10/21/2025

AI Usage:
"""


def calculate_stats(character_class):
    """
    Return character stats based on class name.
    Each class has different strengths in strength, agility, and intelligence.
    """
    if character_class == "Warrior":
        return {"strength": 15, "agility": 8, "intelligence": 5}
    elif character_class == "Mage":
        return {"strength": 5, "agility": 10, "intelligence": 15}
    elif character_class == "Rogue":
        return {"strength": 8, "agility": 15, "intelligence": 7}
    elif character_class == "Cleric":
        return {"strength": 7, "agility": 7, "intelligence": 14}
    else:
        # Invalid class → return None so tests detect it properly
        return None


def create_character(name, character_class):
    """
    Create and return a character dictionary with:
      - name: character's name (string)
      - class: character's class (string)
      - stats: dictionary of stats (from calculate_stats)
    Returns None if the class is invalid.
    """
    stats = calculate_stats(character_class)

    if stats is None:
        return None

    character = {
        "name": name,
        "class": character_class,  # must match test key exactly
        "stats": stats
    }

    return character

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
