"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Tavin Bailey
Date: 10/21/2025

AI Usage:
"""

def calculate_stats(character_class, level):
    """
    Return character stats based on class name and level.
    Each class has different strengths in strength, agility, and intelligence.
    """
    if character_class == "Warrior":
        base = {"strength": 15, "agility": 8, "intelligence": 5}
    elif character_class == "Mage":
        base = {"strength": 5, "agility": 10, "intelligence": 15}
    elif character_class == "Rogue":
        base = {"strength": 8, "agility": 15, "intelligence": 7}
    elif character_class == "Cleric":
        base = {"strength": 7, "agility": 7, "intelligence": 14}
    else:
        return None  # invalid class

    # increase slightly with level
    for key in base:
        base[key] += (level - 1) * 2

    return base


def create_character(name, character_class):
    """
    Create and return a character dictionary with:
      - name
      - class
      - level
      - strength, agility, intelligence
    """
    level = 1
    stats = calculate_stats(character_class, level)

    if stats is None:
        return None

    character = {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": stats["strength"],
        "agility": stats["agility"],
        "intelligence": stats["intelligence"]
    }

    return character


def save_character(character, filename):
    """
    Save a character dictionary to a file.
    Returns True if successful, False otherwise.
    """
    if not isinstance(character, dict) or not filename:
        return False

    required = ["name", "class", "level", "strength", "agility", "intelligence"]
    for key in required:
        if key not in character:
            return False

    file = open(filename, "w")
    for key in required:
        file.write(f"{key}: {character[key]}\n")
    file.close()

    return True


def load_character(filename):
    """
    Load a character from a file.
    """
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
            if key in ["level", "strength", "agility", "intelligence"]:
                value = int(value)
            character[key] = value

    return character


def display_character(character):
    """
    Print character info neatly.
    """
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Agility: {character['agility']}")
    print(f"Intelligence: {character['intelligence']}")
    print("=======================")


if __name__ == "__main__":
    name = input("Enter your character's name: ")
    char_class = input("Choose your class (Warrior, Mage, Rogue, Cleric): ")

    character = create_character(name, char_class)

    if character is None:
        print("Invalid class entered.")
    else:
        display_character(character)
        saved = save_character(character, "my_character.txt")
        if saved:
            print("Character saved to my_character.txt")
