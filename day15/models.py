from typing import Optional


class GPSObject:
    location: (int,int)

    def __init__(self, x, y):
        self.location = (x,y)

class Wall(GPSObject):
    def __str__(self):
        return '#'

class Box(GPSObject):
    def __str__(self):
        return 'O'

    def get_coordinate(self) -> int:
        return self.location[0] + self.location[1]*100

class Robot(GPSObject):
    def __str__(self):
        return '@'

class Field:
    width: int
    height: int
    objects: list[GPSObject]
    objects_by_location: dict[(int,int), GPSObject]

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.objects = []
        self.objects_by_location = {}

    def add_object(self, gps_object: GPSObject):
        self.objects.append(gps_object)
        self.objects_by_location[gps_object.location[0],gps_object.location[1]] = gps_object

    def get_object_at_location(self, x, y) -> Optional[GPSObject]:
        return self.objects_by_location.get((x,y))

    def move_object(self, object_to_move: GPSObject, dir_to_move: (int, int)):
        del self.objects_by_location[object_to_move.location[0],object_to_move.location[1]]
        object_to_move.location = (object_to_move.location[0]+dir_to_move[0],object_to_move.location[1]+dir_to_move[1])
        self.objects_by_location[object_to_move.location[0],object_to_move.location[1]] = object_to_move

    def get_coordinate_sum(self) -> int:
        coordinates = []
        for obj in self.objects:
            if isinstance(obj, Box):
                coordinates.append(obj.get_coordinate())
        print(coordinates)
        return sum(coordinates)

    def __str__(self):
        out = ''
        for y in range(self.height):
            for x in range(self.width):
                object_at_location = self.get_object_at_location(x,y)
                if object_at_location:
                    out += object_at_location.__str__()
                else:
                    out += '.'
            out += '\n'
        # out += '\n'
        return out

