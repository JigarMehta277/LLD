class Road:
    def __init__(self, road_id, name):
        self.id = road_id
        self.name = name
        self.traffic_light = None

    def set_traffic_light(self, traffic_light):
        self.traffic_light = traffic_light

    def get_traffic_light(self):
        return self.traffic_light
    
    def get_if(self):
        return self.id