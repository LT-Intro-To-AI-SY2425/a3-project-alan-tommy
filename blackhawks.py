players = [
#list of players and their number, points from the season, height, weight and age 
{"name": "Andreas Athanasiou", "number": 89, "points": 24, "height": "6'0\"", "weight": 180},
{"name": "Conor Bedard", "number": 98, "points": 45, "height": "5'10\"", "weight": 175},
{"name": "Craig Smith", "number": 12, "points": 30, "height": "6'0\"", "weight": 205},
{"name": "Jason Dickinson", "number": 18, "points": 20, "height": "6'1\"", "weight": 200},
{"name": "Phillip Kurashev", "number": 23, "points": 35, "height": "6'0\"", "weight": 185},
{"name": "Ryan Donato", "number": 16, "points": 27, "height": "6'0\"", "weight": 200},
{"name": "Lukas Reichel", "number": 47, "points": 22, "height": "5'11\"", "weight": 185},
{"name": "Nick Foligno", "number": 17, "points": 19, "height": "6'0\"", "weight": 225},
{"name": "Pat Maroon", "number": 14, "points": 18, "height": "6'3\"", "weight": 250},
{"name": "Taylor Hall", "number": 18, "points": 38, "height": "6'1\"", "weight": 205},
{"name": "Teuvo Teravainen", "number": 86, "points": 33, "height": "5'10\"", "weight": 180},
{"name": "Tyler Bertuzzi", "number": 59, "points": 30, "height": "6'0\"", "weight": 190},
{"name": "Ilya Mikheyev", "number": 65, "points": 25, "height": "6'0\"", "weight": 190},
{"name": "Joey Anderson", "number": 75, "points": 12, "height": "6'1\"", "weight": 205},
{"name": "Artyom Levshunov", "number": 77, "points": 10, "height": "6'2\"", "weight": 215},
{"name": "Alex Vlasic", "number": 44, "points": 15, "height": "6'3\"", "weight": 205},
{"name": "Alec Martinez", "number": 27, "points": 22, "height": "6'0\"", "weight": 210},
{"name": "Connor Murphy", "number": 5, "points": 24, "height": "6'4\"", "weight": 220},
{"name": "Nolan Allan", "number": 44, "points": 8, "height": "6'3\"", "weight": 200},
{"name": "Seth Jones", "number": 4, "points": 35, "height": "6'4\"", "weight": 210},
{"name": "TJ Brodie", "number": 78, "points": 29, "height": "6'1\"", "weight": 205},
{"name": "Wyatt Kaiser", "number": 6, "points": 15, "height": "6'0\"", "weight": 185},
{"name": "Arvid Soderblom", "number": 32, "points": 0, "height": "6'3\"", "weight": 210},  # Placeholder for Goalie points
{"name": "Laurent Brossoit", "number": 40, "points": 0, "height": "6'2\"", "weight": 205},  # Placeholder for Goalie points
{"name": "Petr Mrazek", "number": 34, "points": 0, "height": "6'0\"", "weight": 200}  # Placeholder for Goalie points
]
# Function to retrieve player stats based on the player's name
def get_player_stats(player_name):
    # Loop through each player in the players list
    for player in players:
        # Check if the player's name matches the input (case insensitive)
        if player['name'].lower() == player_name.lower():
            return player  # Return the player's stats if found
    return None  # Return None if the player is not found

def players_within_height(height):
    """Returns a list of player names within 2 inches of the given height."""
    height_inches = convert_height_to_inches(height)
    if height_inches is None:
        return []  # Return an empty list if the height conversion failed

    matching_players = []
    for player in players:
        player_height_inches = convert_height_to_inches(player['height'])
        if player_height_inches is not None and abs(player_height_inches - height_inches) <= 2:
            matching_players.append(player['name'])
    
    return matching_players


def players_within_weight(weight):
    """Returns a list of player names within 10 pounds of the given weight."""
    matching_players = []

    for player in players:
        if abs(player['weight'] - weight) <= 10:
            matching_players.append(player['name'])
    
    return matching_players

def convert_height_to_inches(height_str):
    """Converts a height string (e.g., '6\'1"') to inches."""
    try:
        feet, inches = height_str.split("'")
        inches = inches.replace('"', '')  # Remove the double quote if present
        return int(feet) * 12 + int(inches)
    except ValueError:
        print("Error: Please enter a valid height format (e.g., '6'1').")
        return None

# Example usage
height_input = input("Enter a height (e.g., '6'1'): ")
matching_height_players = players_within_height(height_input)
print("Players within 2 inches of height:", matching_height_players)

weight_input = int(input("Enter a weight (in pounds): "))
matching_weight_players = players_within_weight(weight_input)
print("Players within 10 pounds of weight:", matching_weight_players)

# Main function for the chatbot interaction
def chatbot():
    print("Welcome to the Blackhawks Player Stats Chatbot!")  # Welcome message
    while True:  # Infinite loop for continuous interaction
        # Prompt user for input
        user_input = input("Enter a player's name (or type 'exit' to quit): ")
        # Check if the user wants to exit
        if user_input.lower() == 'exit':
            print("Goodbye!")  # Farewell message
            break  # Exit the loop

        # Retrieve player stats based on user input
        player_stats = get_player_stats(user_input)
        # Check if player stats were found
        if player_stats:
            # Print the player's stats
            print(f"Name: {player_stats['name']}, Number: {player_stats['number']}, "
                  f"Points: {player_stats['points']}, Height: {player_stats['height']}, "
                  f"Weight: {player_stats['weight']}")
        else:
            # Inform the user that the player was not found
            print("Player not found. Please try again.")

def test_get_player_stats():
    # Test cases
    assert get_player_stats("Conor Bedard") == {"name": "Conor Bedard", "number": 98, "points": 45, "height": "5'10\"", "weight": 175}
    assert get_player_stats("Andreas Athanasiou") == {"name": "Andreas Athanasiou", "number": 89, "points": 24, "height": "6'0\"", "weight": 180}
    assert get_player_stats("Bob") is None
    assert get_player_stats("Ryan Donato") == {"name": "Ryan Donato", "number": 16, "points": 27, "height": "6'0\"", "weight": 200}
    assert get_player_stats("Nick Foligno") == {"name": "Nick Foligno", "number": 17, "points": 19, "height": "6'0\"", "weight": 225}
    # Test for case insensitivity
    assert get_player_stats("conor bedard") == {"name": "Conor Bedard", "number": 98, "points": 45, "height": "5'10\"", "weight": 175}

def test_players_within_height():
    # Update expected results based on the actual player data
    assert players_within_height("6'0") == [
        "Andreas Athanasiou", "Craig Smith", "Phillip Kurashev", 
        "Ryan Donato", "Ilya Mikheyev", "Alec Martinez", "Wyatt Kaiser"
    ]
    assert players_within_height("5'10") == ["Conor Bedard", "Teuvo Teravainen"]
    assert players_within_height("6'1") == ["Jason Dickinson", "Taylor Hall", "TJ Brodie"]
    assert players_within_height("6'3") == ["Pat Maroon", "Alex Vlasic", "Connor Murphy", "Nolan Allan"]
    assert players_within_height("5'9") == []

def test_players_within_weight():
    # Test cases for weight
    assert players_within_weight(180) == ["Andreas Athanasiou", "Teuvo Teravainen", "Ilya Mikheyev", "Tyler Bertuzzi"]
    assert players_within_weight(200) == ["Jason Dickinson", "Ryan Donato", "Joey Anderson", "Artyom Levshunov", "Connor Murphy", "Petr Mrazek"]
    assert players_within_weight(225) == ["Nick Foligno", "Pat Maroon"]
    assert players_within_weight(250) == ["Pat Maroon"]
    assert players_within_weight(100) == []

    print("All weight tests passed!")

# Call the test function
test_get_player_stats()
test_players_within_height()
test_players_within_weight()