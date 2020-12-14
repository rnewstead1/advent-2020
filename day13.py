import math
import datetime
from itertools import count


DATA_FIlE = './data/day13.txt'


def get_bus_with_shortest_wait(time, bus_ids):
    wait_times = []
    for bus_id in bus_ids:
        multiplier = math.ceil(time / bus_id)
        wait = multiplier * bus_id - time
        wait_times.append((bus_id, wait))
    return sorted(wait_times, key=lambda bus: bus[1])[0]


def get_bus_ids(all_buses):
    bus_ids = []
    for bus_id in all_buses:
        if bus_id != 'x':
            bus_ids.append(int(bus_id))
    return bus_ids


def run_in_sequence(slowest_bus_time, index_to_subtract, other_buses):
    for bus in other_buses:
        if int((slowest_bus_time - index_to_subtract + bus[0]) % bus[1]) != 0:
            return False
    return True


def get_slowest_bus(buses):
    return sorted(buses, key=lambda bus: bus[1])[-1]


# start = 111881548000000
def get_first_bus_time_sloooow(buses, start):
    found = False
    slowest_bus = get_slowest_bus(buses)
    slowest_bus_time = slowest_bus[1]
    multiplier = math.ceil(start / slowest_bus_time)
    buses_without_slowest = buses[:]
    buses_without_slowest.remove(slowest_bus)
    while not found:
        if int(multiplier % 1000000) == 0:
            print(f'{datetime.datetime.now()}: {multiplier * slowest_bus_time}')
        if not run_in_sequence(multiplier * slowest_bus_time, slowest_bus[0], buses_without_slowest):
            multiplier += 1
        else:
            found = True

    return (multiplier * slowest_bus_time) - slowest_bus[0]


def buses_with_indexes(all_buses):
    buses = []
    for index, bus in enumerate(all_buses):
        if bus != 'x':
            buses.append((index, int(bus)))
    return buses


def get_first_bus_time(buses):
    first_bus_time, step = 0, 1
    for index, bus in buses:
        for c in count(first_bus_time, step):
            if (c + index) % bus == 0:
                first_bus_time, step = c, step * bus
                break
    return first_bus_time


with open(DATA_FIlE) as file:
    lines = file.readlines()

    arrival = int(lines[0].rstrip())
    all_buses = lines[1].rstrip().split(',')
    bus_ids = get_bus_ids(all_buses)

    bus_id, wait = get_bus_with_shortest_wait(arrival, bus_ids)
    print(f'answer: {bus_id * wait}')

    indexed_buses = buses_with_indexes(all_buses)
    print(f'first bus time: {get_first_bus_time(indexed_buses)}')
