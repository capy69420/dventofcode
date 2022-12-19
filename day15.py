sensors = []
beacons = []

with open('input15.txt', 'r') as f:
  for line in f:
    line = line.strip().split(':')
    sensor = line[0].split(',')
    sensor_x = line[0].split(',')[0].split('=')[1]
    sensor_y = line[0].split(',')[1].split('=')[1]
    sensors.append([int(sensor_x), int(sensor_y)])
    beacon_x = line[1].split(',')[0].split('=')[1]
    beacon_y = line[1].split(',')[1].split('=')[1]
    beacons.append([int(beacon_x), int(beacon_y)])

def biiggest_x():
    x = 0
    for sensor in sensors:
        if sensor[0] > x:
            x = sensor[0]
    for beacon in beacons:
        if beacon[0] > x:
            x = beacon[0]
    return x
def smallest_x():
    x = biiggest_x()
    for sensor in sensors:
        if sensor[0] < x:
            x = sensor[0]
    for beacon in beacons:
        if beacon[0] < x:
            x = beacon[0]
    return x

def beacon_exclusion_zone(y):
    count = 0
    x_set = set()
    min_map, max_map = smallest_x(),biiggest_x()
    for i in range(len(sensors)):
        # find the distance between sensor i and beacon i
        d = abs(beacons[i][0]-sensors[i][0]) + abs(beacons[i][1]-sensors[i][1])
        # find the possible x at distance d or less
        x_min = (d - abs(y-sensors[i][1])) - sensors[i][0]
        x_max = sensors[i][0] + (d - abs(y-sensors[i][1]))
        # sensor range
        for x in range(x_min, x_max+1):
            if x in range(min_map, max_map+1) and [x,y] not in beacons:
            # in that case there is no beacon at (x,y)
                x_set.add(x)
    return len(x_set)

print(beacon_exclusion_zone(2000000))