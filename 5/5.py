import re

line_regex = r"(\d+,\d+) -> (\d+,\d+)"
lines = []

points = {}
total_greater_than_2 = 0

def extract_points(line):
    matches = re.match(line_regex, line)
    groups = matches.groups()
    x1, y1 = groups[0].split(",")
    x2, y2 = groups[1].split(",")

    return [int(x1), int(y1)], [int(x2), int(y2)]

class Line:
    def __init__(self, start_point, end_point):
        self.covered_points = []
        self.start_point = start_point
        self.end_point = end_point
        self.is_horizontal = start_point[0] == end_point[0]
        self.is_vertical = start_point[1] == end_point[1]
        self.interpolate()

    def interpolate(self):
        interpolation_point = self.start_point
        horizontal_direction = int((self.end_point[0] - self.start_point[0]) / abs(self.end_point[0] - self.start_point[0])) if self.end_point[0] - self.start_point[0] else 0
        vertical_direction = int((self.end_point[1] - self.start_point[1]) / abs(self.end_point[1] - self.start_point[1])) if self.end_point[1] - self.start_point[1] else 0

        self.covered_points.append(interpolation_point)
        while interpolation_point != self.end_point:
            interpolation_point = [interpolation_point[0] + horizontal_direction, interpolation_point[1] + vertical_direction]
            self.covered_points.append(interpolation_point)
        

with open("input.txt") as fp: 
    while True: 
        line = fp.readline().strip()
        if not line: 
            break
        
        line_object = Line(*extract_points(line))

        if line_object.is_horizontal or line_object.is_vertical:
            lines.append(line_object)

for line in lines:
    for point in line.covered_points:
        points[str(point)] = points[str(point)] + 1 if points.get(str(point)) else 1

for value in points.values():
    if value >= 2:
        total_greater_than_2 += 1

print(total_greater_than_2)