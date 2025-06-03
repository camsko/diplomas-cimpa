class Participant:
    def __init__(self):
        self.name = ""
        self.points = ""
        self.medal = "" 
        self.area = ""

    def set_name(self, name):
        self.name = name    
        
    def set_points(self, points):
        self.points = points  

    def set_medal(self, medal):
        self.medal = medal     
    
    def set_area(self, area):
        self.area = area 

    def create_from_parsed_text(self, name, points, medal, area):
        self.set_name(name)
        self.set_points(points)
        self.set_medal(medal)
        self.set_area(area)
    
    def __str__(self):
        return f"{self.name}, {self.points}, {self.medal}, {self.area}"
