import re

pos_valves = []
def dfs(current_valve, pressure_released, opened, valves, tunnels, time_left, open):
    max_pressure = pressure_released
    if time_left > 0:
        # get the flow rate and reachable valves for the current valve
        flow_rate = valves[current_valve]['flow_rate']
        reachable_valves = valves[current_valve]['tunnels']
        # mark current_valve as visited
        # open the current valve or not open it
        if not valves[current_valve]['open'] and open:
            valves[current_valve]['open'] = True
            opened.add(current_valve)
            # time opening the valve
            time_left -= 1
            pressure_released = pressure_released + flow_rate * time_left
        
        max_pressure = pressure_released

        # visit each unvisited valve reachable from the current valve
        for v in reachable_valves:
            # not all open
            if len(opened) < len(pos_valves):
                # calculate the pressure released at the next valve
                pressure_released_at_v = pressure_released + flow_rate*(time_left-1)
                # recursively visit the next valve, time left - 1 after reaching the next valve
                opened_copy1 = opened.copy()
                opened_copy2 = opened.copy()
                pressure_open = dfs(v, pressure_released_at_v, opened_copy1, valves, tunnels, time_left-1, True)
                pressure_close = dfs(v, pressure_released_at_v, opened_copy2, valves, tunnels, time_left-1, False)
                if pressure_open[0] > pressure_close[0]:
                    opened = visited_copy1
                else:
                    opened = visited_copy2
                # update the maximum pressure if necessary
                max_pressure = max(max_pressure, pressure_open[0], pressure_close[0])
    return [max_pressure, opened]

def main():
  # read the input from a file
  with open('input16.txt', 'r') as f:
    lines = f.readlines()
  
  # parse the input and create a dictionary of valves and a list of tunnels
  valves = {}
  tunnels = []
  for line in lines:
    parts = line.strip().split(' ')
    valve = parts[1]
    flow_rate = int(parts[4].split('=')[1].split(';')[0])
    tunnels = parts[9:]
    tunnels = [t.strip(',') for t in tunnels]
    valves[valve] = {'flow_rate': flow_rate, 'tunnels': tunnels, 'open':False}
    if flow_rate > 0:
        pos_valves.append(valve)
   
  
  # start at valve AA with pressure_released = 0 and an empty set of visited valves
  max_pressure = max(dfs('AA', 0, set(), valves, tunnels, 30, True), dfs('AA', 0, set(), valves, tunnels, 30, False))
  print(f'The maximum pressure that can be released is {max_pressure}.')

if __name__ == '__main__':
  main()
