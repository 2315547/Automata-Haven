class RechargeStation:
    def __init__(self, location):
        self.location = location
        self.stored_parts = []

    def store_part(self, part):
        self.stored_parts.append(part)
        print(f"Part stored at {self.location}")
