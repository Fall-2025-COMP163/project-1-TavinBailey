"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Tavin Bailey
Date: 10/21/2025

AI Usage:
"""

import os # Imports the 'OS' module so we can check if files or folders exist on the computer.

# CHARACTER STAT CALCULATOR
def calculate_stats(character_class, level):
    """Calculates base stats based on class and level."""
    if character_class is None: # If no class was provided, returns zeros for all stats.
        return (0, 0, 0)
    cls = character_class.lower() # Converts the class name to lowercase for easy comparison.
    # Checks which class was chosen and calculate stats based on level.
    if cls == "warrior":
        strength = 10 + level * 3 # Warriors gain strength quickly.
        magic = 2 + level # Warriors have low magic.
        health = 100 + level * 10 # Warriors have high health.
    elif cls == "mage":
        strength = 3 + level # Mages have low strength.
        magic = 15 + level * 3 # Mages have high magic power.
        health = 80 + level * 5 # Mages have lower health.
    elif cls == "rogue":
        strength = 7 + level * 2 # Rogues have a decent balance between strength and magic, gaining both steadily.
        magic = 7 + level * 2 # Rogues have a decent balance between strength and magic, gaining both steadily.
        health = 70 + level * 5 # Rogues have moderate health growth.
    elif cls == "cleric":
        strength = 6 + level * 2 # Clerics are slightly strong in terms of strength.
        magic = 12 + level * 2 # Clerics are magic users who heal, gaining balanced magic growth.
        health = 90 + level * 8 # Clerics have a solid health that increases quickly per level.
    else:
        strength = 5 + level # Default stats if the class name doesn't match known ones.
        magic = 5 + level
        health = 50 + level * 5
    return (strength, magic, health)

# CHARACTER CREATION
def create_character(name, character_class):
    """Creates a new character dictionary with calculated stats."""
    if name is None or name == "" or character_class is None: # Make sure both name and class exist.
        return None
    level = 1 # Start every new character at level 1.
    strength, magic, health = calculate_stats(character_class, level) # Calculate base stats.
    # Store all data in a dictionary.
    character = {
        "name": name, # Character's name.
        "class": character_class, # Character's chosen class.
        "level": level, # Character's level.
        "strength": strength, # Character's strength stat.
        "magic": magic, # Character's magic stat.
        "health": health, # Character's health stat.
        "gold": 100 # Starting gold amount.
    }
    return character # Return the completed dictionary.

# SAVE CHARACTER TO FILE
def save_character(character, filename):
    """Saves character to a text file in the required format."""
    if character is None or filename is None or filename == "": # Validate input.
        return False

    # Splits the filename into folder to check if the path exists.
    parts = filename.split("/")
    if len(parts) > 1: # USes len() to return the amount of items that are in "parts", making sure the amount is greater than 1.
        directory = "/".join(parts[:-1]) # Everything before the last slash.
        if directory != "" and not os.path.exists(directory): # If the folder is missing, returns False.
            return False

    file = open(filename, "w") # Opens the file for writing and setting "file" as the variable.
    file.write(f"Character Name: {character['name']}\n") # Writes the character's name on a newline.
    file.write(f"Class: {character['class']}\n") # Writes the character's class on a newline.
    file.write(f"Level: {character['level']}\n") # Writes the character's level on a newline.
    file.write(f"Strength: {character['strength']}\n") # Writes the character's strength on a newline.
    file.write(f"Magic: {character['magic']}\n") # Writes the character's magic on a newline.
    file.write(f"Health: {character['health']}\n") # Writes the character's health on a newline.
    file.write(f"Gold: {character['gold']}\n") # Writes the character's amount of gold on a newline.
    file.close() # Closes the file after writing.
    return True # Returns success/true.

# LOAD CHARACTER FROM FILE
def load_character(filename):
    """Loads a character from a text file and returns a dictionary."""
    if not os.path.exists(filename): # Stop if the file doesn't exist.
        return None

    file = open(filename, "r") # Opens the file for reading.
    lines = file.readlines() # Reads all the lines into a list.
    file.close() # Closes the file after reading.

    char = {} # Empty dictionary to fill with loaded data.
    for line in lines: # Goest through every line one by one.
        parts = line.strip().split(": ") # Splits into key and value.
        if len(parts) == 2: # Uses len() to check that the split resulted in exactly two parts (key and value)
            key, value = parts # Unpacks the two parts.
            if key == "Character Name": # If the key is the character's name.
                char["name"] = value
            elif key == "Class": # If the key is the character's class.
                char["class"] = value
            elif key == "Level": # If the key is the character's level.
                char["level"] = int(value)
            elif key == "Strength": # If the key is the character's strength.
                char["strength"] = int(value)
            elif key == "Magic": # If the key is the character's magic.
                char["magic"] = int(value)
            elif key == "Health": # If the key is the character's health.
                char["health"] = int(value)
            elif key == "Gold": # If the key is the character's gold.
                char["gold"] = int(value)
    return char # Returns the fully loaded character dictionary.

# DISPLAY CHARACTER
def display_character(character):
    """Prints formatted character info."""
    print("=== CHARACTER SHEET ===") # Header title.
    print(f"Name: {character['name']}") # Outputs the chracter's name.
    print(f"Class: {character['class']}") # Outputs the character's class.
    print(f"Level: {character['level']}") # Outputs the character's level.
    print(f"Strength: {character['strength']}") # Outputs the character's strength.
    print(f"Magic: {character['magic']}") # Outputs the character's magic.
    print(f"Health: {character['health']}") # Outputs the character's health.
    print(f"Gold: {character['gold']}") # Outputs the character's gold.
    return None # Returns nothing; just displays info.

# LEVEL-UP FUNCTION
def level_up(character):
    """Increases level and recalculates stats."""
    character["level"] = character["level"] + 1 # Adds one to the chracter's level.
    s, m, h = calculate_stats(character["class"], character["level"]) # Recalculates stats.
    character["strength"] = s # Updates to the new strength value.
    character["magic"] = m # Updates to the new magic value.
    character["health"] = h # Updates to the new health value.
    return None # Returns no value; modifies the dictionary directly.

# MAIN TEST BLOCK
# Optional test block
if __name__ == "__main__": # Only runs if this file is executed directly.
    char = create_character("TestHero", "Warrior") # Creates a simple Warrior character as the test character.
    display_character(char) # Prints the character's initial stats.
    save_character(char, "testhero.txt") # Saves the character to a file.
    loaded = load_character("testhero.txt") # Loads the same character from the file.
    print("\nLoaded:") # Outputs the section title (lavel) for the loaded data.
    display_character(loaded) # Shows the loaded character info.
    level_up(loaded) # Increases the level and stats.
    print("\nAfter level up:") # Outputs the section title (label) for the leveled-up character.
    display_character(loaded) # Shows the updated stats.
