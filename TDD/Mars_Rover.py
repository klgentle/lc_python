class Mars_Rover(object):
    def __init__(self, position:tuple, oriented:tuple):
        self.position_x = position[0]
        self.position_y = position[1]
        # how to display oriented
        self.oriented = oriented

    def move(self, f_or_b:str):
        # how to calculate the step TODO
        if f_or_b == 'f':
            self.position_x += 1
        else:
            self.position_x -= 1
        return (self.position_x, self.position_y)
