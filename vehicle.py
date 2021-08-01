


from random import randint


class Vehicle: 
    def __init__(self, x, y):
        self.pos = PVector(x, y)
        self.vel = PVector(0, 0)
        self.acc = PVector(0, 0)
        self.max_speed = 5
        self.max_force = 0.1
        
        
    # First, we're taking a look at the target and use position PVectors as
    # position vectors. Then, we look at them as velocity vectors. They help us
    # determine what our acceeration should be.
    def seek(self, target): # target is a PVector
        # desired velocity = the vector that shows the distance between us and the
        # target minus our current velocity. 
        # Get the distance away from the target; that'll help us.
        
        # Set the force to be max speed; we want our velocity to be it.
        
        # Limit the force; otherwise these vehicles will always be turning around.
        
        # We want our velocity to be max speed, not our acceleration! If our 
        # velocity will add to the acceleration, we will be over our max speed.
        
        # For flee, we don't wanna get all the code and then change it; instead
        # we are going to return the force.
        return
        
        
    def flee(self, target):
        # In seek, we are returning the appropriate force. To shorten the code, 
        # we can just return the return value * -1.
        return
        
        
    def persue(self, target):
        # We're basically going to seek a little bit ahead of our target.
        # But we need a number of frames ahead! 
        
        # Then, we're going to add the target's velocity to the target's position
        # (not frequentely) to get our seek target.
        
        # Now just return the output of seek on the target on our new position
        # variable.
        return
        
        
    def evade(self, target):
        # Evade is the oppisite of persue. To shorten our code, we can just return
        # the return value * -1.
        return
        
        
    def show(self, target):
        # Acceleration vector
        pushMatrix()
        popMatrix()
        # Velocity vector
        pushMatrix()
        popMatrix()
        # Real position
        pushMatrix()
        popMatrix()
        
