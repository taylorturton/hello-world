class TennisPlayer:
    def __init__(self, name, age, height_cm, nationality):
        self.name = name
        self.age = age
        self.height_cm = height_cm
        self.nationality = nationality

# Create a list of player information (name, age, height in cm, and nationality)
players_info = [
    ("Michael Klein", 27, 196, "USA"),
    ("Jordyn Miller", 24, 175, "Canada"),
    ("Seb Williamson", 22, 185, "UK"),
    ("Habib Camara", 20, 189, "France"),
    ("Ekatarina Voronin", 26, 168, "Russia")
    # Add more players here as needed
]

# Create player objects and store them in a list
players = [TennisPlayer(name, age, height_cm, nationality) for name, age, height_cm, nationality in players_info]

# Print player information
for player in players:
    print(f"{player.name} is {player.age} years old, {player.height_cm} cm tall, and from {player.nationality}.")
