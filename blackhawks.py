players = [
    # list of players and their number, points from the season, height, weight and age 
    {"name": "Andreas Athanasiou", "number": 89, "points": 24, "height": "6'0\"", "weight": 180},
    {"name": "Conor Bedard", "number": 98, "points": 45, "height": "5'10\"", "weight": 175},
    {"name": "Craig Smith", "number": 12, "points": 30, "height": "6'0\"", "weight": 205},
    {"name": "Jason Dickinson", "number": 18, "points": 20, "height": "6'1\"", "weight": 200},
    {"name": "Phillip Kurashev", "number": 23, "points": 35, "height": "6'0\"", "weight": 185},
    {"name": "Ryan Donato", "number": 16, "points": 27, "height": "6'0\"", "weight": 200},
    {"name": "Lukas Reichel", "number": 47, "points": 22, "height": "5'11\"", "weight": 185},
    {"name": "Nick Foligno", "number": 17, "points": 19, "height": "6'0\"", "weight": 225},
    {"name": "Pat Maroon", "number": 14, "points": 18, "height": "6'3\"", "weight": 250},
    {"name": "Taylor Hall", "number": 71, "points": 38, "height": "6'1\"", "weight": 205},
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
    {"name": "Laurent Brossoit", "number": 40, "points": 0, "height": "6'2 \"", "weight": 205},  # Placeholder for Goalie points
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
    height_in_inches = convert_height_to_inches(height)
    lower_limit = height_in_inches - 2
    upper_limit = height_in_inches + 2
    result =[]
    for player in players:
        player_height_inches = convert_height_to_inches(player['height'])
        if player_height_inches >= lower_limit and player_height_inches <= upper_limit:
            result.append(player['name'])
    print(result)
    return result
    
def players_within_weight(weight):
    """Returns a list of player names within 10 pounds of the given weight."""
    matching_players = []

    for player in players:
        if abs(player['weight'] - weight) <= 10:
            matching_players.append(player['name'])
    print(matching_players)
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
    # Players with heights within ±2 inches of "6'0" (range 5'10" to 6'2")
    assert players_within_height("6'0") == [
        "Andreas Athanasiou", "Conor Bedard", "Craig Smith", "Jason Dickinson",
        "Phillip Kurashev", "Ryan Donato", "Lukas Reichel", "Nick Foligno",
        "Taylor Hall", "Teuvo Teravainen", "Tyler Bertuzzi", "Ilya Mikheyev",
        "Joey Anderson", "Alec Martinez", "TJ Brodie", "Wyatt Kaiser"
    ]

    # Players within ±2 inches of "5'10" (range 5'8" to 6'0")
    assert players_within_height("5'10") == [
        "Conor Bedard", "Phillip Kurashev", "Ryan Donato", "Lukas Reichel", 
    "Nick Foligno", "Teuvo Teravainen", "Tyler Bertuzzi", "Ilya Mikheyev", 
    "Alec Martinez", "Wyatt Kaiser", "Petr Mrazek"
    ]

    # Players within ±2 inches of "6'1" (range 5'11" to 6'3")
    assert players_within_height("6'1") == [
         "Jason Dickinson", "Lukas Reichel", "Nick Foligno", "Taylor Hall", 
    "Tyler Bertuzzi", "Ilya Mikheyev", "Alec Martinez", "TJ Brodie", 
    "Artyom Levshunov", "Laurent Brossoit", "Petr Mrazek"
    ]

    # Players within ±2 inches of "6'3" (range 6'1" to 6'5")
    assert players_within_height("6'3") == [
        "Jason Dickinson", "Taylor Hall", "Artyom Levshunov", "Connor Murphy",
    "Seth Jones"
    ]

    # No players within 2 inches of "5'9" (since lowest height is 5'10")
    assert players_within_height("5'9") == []

    # Players within ±2 inches of "6'4" (range 6'2" to 6'6")
    assert players_within_height("6'4") == [
        "Artyom Levshunov", "Connor Murphy", "Seth Jones"
    ]
    
    print("All height tests passed!")


def test_players_within_weight():
    # Players within ±10 pounds of 180 lbs (range 170 to 190)
    assert players_within_weight(180) == [
        "Andreas Athanasiou", "Conor Bedard", "Teuvo Teravainen", 
        "Tyler Bertuzzi", "Ilya Mikheyev", "Lukas Reichel", 
        "Phillip Kurashev", "Wyatt Kaiser"
    ]

    # Players within ±10 pounds of 200 lbs (range 190 to 210)
    assert players_within_weight(200) == [
        "Jason Dickinson", "Ryan Donato", "Joey Anderson", 
        "Alec Martinez", "TJ Brodie", "Nick Foligno", "Petr Mrazek"
    ]

    # Players within ±10 pounds of 220 lbs (range 210 to 230)
    assert players_within_weight(220) == [
        "Connor Murphy", "Seth Jones", "Artyom Levshunov"
    ]

    # Players within ±10 pounds of 250 lbs (range 240 to 260)
    assert players_within_weight(250) == ["Pat Maroon"]

    # No players near 100 lbs
    assert players_within_weight(100) == []

    # Players within ±10 pounds of 205 lbs (range 195 to 215)
    assert players_within_weight(205) == [
        "Craig Smith", "Taylor Hall", "Alec Martinez", 
        "Joey Anderson", "TJ Brodie", "Seth Jones", 
        "Laurent Brossoit", "Artyom Levshunov"
    ]

    print("All weight tests passed!")

# Call the test functions