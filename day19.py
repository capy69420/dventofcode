import re

def can_build(blueprint, resources):
    combinations = []
    robots = {'ore':1, 'clay':0, 'obsidian':0, 'geode':0}
    # while resources
    for robot in blueprint:
        for r in blueprint[robot]:
            if robot == 'geode':
                # orb an obsidian cost
                if resources['ore'] >= r[0] and resources['obsidian'] >= r[1]:
                   robots['geode'] += 1
                   resources['ore'] -= r[0]
                   resources['obsidian'] -= r[1]
            if robot == 'ore':
                # cost of building an ore robot
                if resources['ore'] >= r[0]:
                    robots['ore']  += 1
                    resources['ore'] -= r[0]
            

    return combinations

def build_robots(blueprint, resources, robots):
    # check what type and amount of robots can be build
    # and get a list of those
    possible_robots = can_build(blueprint, resources)
    # build all possible combinations (including none)
    return robots

def simulate(blueprint):
    resources = {'ore':0, 'clay':0, 'obsidian':0, 'geode':0}
    robots = {'ore':1, 'clay':0, 'obsidian':0, 'geode':0}
    for minute in range(24):
        # Collect resources, takes 1 min for robots to collect resources
        for r in robots:
            resources[r] += robots[r]
        # Build robots, takes 1 min to build a robot
        # maximize the geode production
        # OPTION 1:
        # to do so maximize the geode robots, for this maximize the ore and obsidian robots
        # need blueprint['geode'] ore and obsidian robots to build a geode robot
        # for obsidian robots maximize the ore and clay
        # for clay robots maximize ore production
        # so the most important robots are ore, geode, obsidian, clay in this order
        # OPTION 2:
        # every minute check what robot can be build
        # build every option possible (includes not building anything)
        build_robots(blueprint, resources, robots)
    return resources['geode']


blueprints = []
# input
with open('input19.txt', 'r') as f:
    for line in f:
        # The blueprint id
        id = int(line.strip().split(':')[0].split(' ')[1])
        # get the robots
        robots = line.strip().split(':')[1].split('.')
        # get all the costs for each robot into arrays
        # ore
        ore_robot = [int(t) for t in re.findall(r'\d+', robots[0])]
        # ore
        clay_robot = [int(t) for t in re.findall(r'\d+', robots[1])]
        # ore and clay
        obsidian_robot = [int(t) for t in re.findall(r'\d+', robots[2])]
        # ore and obsidian
        geode_robot = [int(t) for t in re.findall(r'\d+', robots[3])]
        # blueprint an object with each robot type and an array of each building cost
        blueprint = {'ore': ore_robot, 'clay': clay_robot,
         'obsidian': obsidian_robot, 'geode': geode_robot}
        simulate(blueprint)
        blueprints.append(blueprint)

