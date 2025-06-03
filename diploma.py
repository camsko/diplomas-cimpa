class Participant:
    def __init__(self):
        self.name = ""
        self.points = 0
        self.medal = '' #G for gold, S for silver or B for bronze
        self.points = 0

    def set_name(self, name):
        self.name = name    
        
    def set_points(self, points):
        self.points = points  

    def set_medal(self, medal):
        self.medal = medal 