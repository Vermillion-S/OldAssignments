class LidarSensor():
    def __init__(self, data = 0.0):
        self.sensortype = "Lidar"
        # Stores object distance in meters
        self.object_distance = data
    def read_distance(self):
        print(f"The {self.sensortype} sensor reads sends and recieves as signal.....")
        return self.object_distance
    # Changes value based on changing environmental factors
    def update_distance(self, data):
        self.object_distance = data
    

class Motor():
    # Initiate the class
    def __init__(self):
        self.actuatortype = "Brush Motor"
    # Class method that activates the motor, and in turn moves the end effector
    def driveForward(self, effector):
        print(f"The {self.actuatortype} drives forward, turning the axle")
        effector.turn()

class Wheel():
    def __init__(self):
        self.effectorType = "Wheel"
    def turn(self):
        print(f"The {self.effectorType} rotates; pushing against the ground to move forward")


sensor = LidarSensor(22.22)

distance = sensor.read_distance()

print(f"The nearest obstacle is {distance} meters away")

actuator = Motor()

effector = Wheel()

# Activate the Actuator, which in turn influences the end effector
actuator.driveForward(effector)

