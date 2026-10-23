
# Super class for actuators
class Actuator:
    def __init__(self, type):
        self.ActuatorOn = False
        self.ActuatorType = type
    def toggleActuator(self):
        if self.ActuatorOn:
            print(f"{self.ActuatorType} is deactivating")
            self.ActuatorOn = False
        else:
            print(f"{self.ActuatorType} is Activating")
            self.ActuatorOn = True

# Class for rotating motor actuator
class Motor(Actuator):
    def __init__(self, angle = 0.0):
        super().__init__("Motor")
        self.turnAngle = angle
    # activates brushless motor in arm base to rotate the arm
    def turn(self, angle : float):
        # activate motor
        self.toggleActuator()
        # Add to turn angle
        self.turnAngle += angle

        # Clamps turn angle between 0 and 360 degrees
        if self.turnAngle > 360:
            self.turnAngle -= 360
        elif self.turnAngle < 0:
            self.turnAngle += 360
        elif self.turnAngle == 360:
            self.turnAngle = 0

        # Prints change to comandline
        if angle > 0:
            print(f"Arm turns left by {angle} degrees. Currently at {self.turnAngle}")
        elif angle < 0:
            print(f"Arm turns right by {-angle} degrees.  Currently at {self.turnAngle}")
        else:
            print("Arm does not turn")

        # deactivate motor
        self.toggleActuator()

# Class for Hydrolic Actuator arm
class Hydrolic(Actuator):
    def __init__(self, elevation = 5.0):
        super().__init__("Hydrolic")
        self.Elevation = elevation
        self.maxheight = 5.0
    # Activates the hydrolics to raise or lower the arm
    def elevate(self, height : float):
        # Prep the hydrolics
        self.toggleActuator()
        # Prevent the Claw from going out of 
        # Otherwise, add to claw elevation, 
        # and print change to terminal
        if self.Elevation + height > self.maxheight or self.Elevation + height < 0:
            print(f"The {self.ActuatorType} cannot be raised/lowered out of bounds")
        elif height > 0:
            self.Elevation += height
            print(f"{self.ActuatorType} raised by {height} ft, to {self.Elevation}")
            
        elif height < 0:
            self.Elevation += height
            print(f"{self.ActuatorType} lowered by {-height} ft, to {self.Elevation}")
        else:
            print(f"{self.ActuatorType} height does not change")

        # deactivate actuator
        self.toggleActuator()

class Claw(Actuator):
    def __init__(self, gripstate = "Open"):
        super().__init__("Claw")
        self.gripState = gripstate

    def toggleClaw(self):
        # Turn on Grip motor
        self.toggleActuator()
        # Close if open 
        # Open if closed
        if self.gripState == "Open":
            print("The grip closes")
            self.gripState = "Closed"
        else:
            print("The grip opens")
            self.gripState = "Open"
        
        # Deactivate Actuator
        self.toggleActuator()

# Controller object for the Robot Arm
class robotArmController:
    def __init__(self):
        self.type = "Robotic Claw"

    # Rotates Motor
    def rotate(self, angle : float, actuator : Motor):
        print(f"\n(!) The {self.type} is turning")
        actuator.turn(angle)
        

    # Raises hydrolic
    def Raise(self, height : float, actuator : Hydrolic):
        print(f"\n(!) The {self.type} is changing elevation")
        actuator.elevate(height)

    # Toggles claw state
    def grab(self, actuator : Claw):
        print(f"\n(!) The {self.type} is changing manipulating the claw")
        actuator.toggleClaw()

# initializes objects

base = Motor()

arm = Hydrolic()

hand = Claw()

newArm = robotArmController()

#--------------------------------#
# Code for controlling the robot #
#--------------------------------#

# Turn left 30 degrees
newArm.rotate(30, base)

# Lower 3 feet
newArm.Raise(-3, arm)

# Close Claw
newArm.grab(hand)

#Raise Arm 4 feet
newArm.Raise(4, arm)

# Rotate Right 60 degrees
newArm.rotate(-60, base)

# Open the claw
newArm.grab(hand)