class SurvivorBot:
    def __init__(self, location, energy=100):
        self.location = location
        self.energy = energy
        self.carrying = None

    def move(self, new_location):
        if self.energy >= 5:
            self.location = new_location
            self.energy -= 5
            print(f"Bot moves to {self.location}, remaining energy: {self.energy}")
        else:
            print("Bot has insufficient energy to move.")

    def evade(self):
        if self.energy >= 5:
            # Move to a new location to evade; simple logic could be improved
            self.move((self.location[0] + 1, self.location[1]))
            print(f"Bot evades to {self.location}")
