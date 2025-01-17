def distance(loc1, loc2):
    """Calculate Manhattan distance between two locations."""
    return abs(loc1[0] - loc2[0]) + abs(loc1[1] - loc2[1])

class MalfunctioningDrone:
    def __init__(self, location, energy=100):
        self.location = location
        self.energy = energy

    def move_towards(self, target_location):
        if self.energy >= 10:
            self.location = target_location
            self.energy -= 10
            print(f"Drone moves to {self.location}, energy left: {self.energy}")

    def detect_and_pursue(self, bots):
        for bot in bots:
            if distance(self.location, bot.location) <= 3:
                print(f"Drone at {self.location} detects bot at {bot.location}")
                self.move_towards(bot.location)
                self.attack(bot)

    def attack(self, bot):
        if self.energy > 20:
            bot.energy -= 15
            self.energy -= 5
            print(f"Drone attacks bot at {bot.location}, bot energy: {bot.energy}")
