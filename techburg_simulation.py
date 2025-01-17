# techburg_simulation.py
from techburg_classes import RechargeStation, SparePart, SurvivorBot

def setup_simulation():
    parts = [SparePart('small', (1, 1)), SparePart('medium', (2, 2))]
    stations = [RechargeStation((0, 0)), RechargeStation((3, 3))]
    bots = [SurvivorBot((0, 1)), SurvivorBot((1, 0))]

    return parts, stations, bots

def simulate_step(parts, stations, bots):
    for bot in bots:
        if not bot.carrying:
            if parts:
                target_part = parts.pop(0)
                bot.move(target_part.location)
                bot.collect_part(target_part)
        else:
            nearest_station = stations[0]
            bot.move(nearest_station.location)
            bot.deposit_part(nearest_station)

def run_simulation():
    parts, stations, bots = setup_simulation()
    while parts or any(bot.carrying for bot in bots):
        simulate_step(parts, stations, bots)

if __name__ == '__main__':
    run_simulation()
