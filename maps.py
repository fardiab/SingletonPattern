class Map:
    def __init__(self, name):
        self.name = name
        self.cities = []
        self.roads = []

    def add_city(self, city):
        self.cities.append(city)

    def add_road(self, road):
        self.roads.append(road)

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name
    
    def __eq__(self, other):
        return self.name == other.name
    
MAP = Map('MAP')