# techburg_classes.py

class RechargeStation:
    """
    Represents a recharge station where survivor bots can store collected spare parts.
    """
    def __init__(self, location):
        self.location = location
        self.stored_parts = []

    def store_part(self, part):
        """
        Stores a spare part at the recharge station and prints a message.
        """
        self.stored_parts.append(part)
        print(f"Part of size {part.size} stored at Recharge Station located at {self.location}")

class SparePart:
    """
    Represents a spare part that can be collected by survivor bots.
    """
    def __init__(self, size, location):
        self.size = size
        self.location = location
        self.enhancement_value = {'small': 3, 'medium': 5, 'large': 7}[size]

class SurvivorBot:
    """
    Represents a survivor bot capable of moving, collecting spare parts, and depositing them at recharge stations.
    """
    def __init__(self, location, energy=100):
        self.location = location
        self.energy = energy
        self.carrying = None
        print(f"Survivor Bot created at location {self.location} with initial energy {self.energy}")

    def move(self, new_location):
        """
        Moves the bot to a new location if sufficient energy is available.
        """
        if self.energy >= 5:
            self.location = new_location
            self.energy -= 5
            print(f"Moved to {self.location}. Remaining energy: {self.energy}")
        else:
            print("Not enough energy to move. Energy left:", self.energy)

    def collect_part(self, part):
        """
        Collects a spare part if the bot is not already carrying one.
        """
        if self.carrying is None:
            self.carrying = part
            print(f"Collected a {part.size} part from location {part.location}")

    def deposit_part(self, station):
        """
        Deposits the carried spare part at a recharge station.
        """
        if self.carrying:
            station.store_part(self.carrying)
            print(f"Deposited a {self.carrying.size} part at station located at {station.location}")
            self.carrying = None

