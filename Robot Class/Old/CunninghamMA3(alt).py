# This program simulates an automated plumbing system,
# which senses the pressure within the pipes, 
# and activates/deactivates an emergency release valve, 
# which keeps the system within a good pressure range

# Class for the sensor
class PressureSensor:
    def __init__(self, data):
        self.sensortype = "Pressure Sensor"
        #stores current pressure in pascals
        self.pressure = float(data)
    # Function for reading stored sensor data
    def read_current_pressure(self):
        return self.pressure
    # Function for updating the stored pressure value
    def update_pressure(self, data):
        self.pressure = data

# Class for the End Effector
# valves are used to control the flow of fluids through rotational force
class Valve:
    # Initializes variables
    def __init__(self):
        self.endEffector_type = "Pressure Valve"
        # Default state of the valve is closed
        self.state = "closed"

    # Opening the valve releaves pressure
    def open(self):
        print(f"   {self.endEffector_type} Opens! Releasing Pressure")
        self.state = "open"

    # Closing the valvue lets pressure build
    def close(self):
        print(f"   {self.endEffector_type} Closes! Pressure can now build")
        self.state = "closed"
    # Flag to let the program remember 
    # the current state of the effector
    def get_state(self):
        return self.state
    
class Motor:
    def __init__(self):
        self.actuator_type = "Rotary Motor"

    # Rotates the motor to the left
    # opening the pressure valve
    def rotate_left(self, effector):
        print(f"   {self.actuator_type} rotates counter-clockwise")
        effector.open()

    # Rotates the motor to the right
    # Closing the Pressure valve
    def rotate_right(self, effector):
        print(f"   {self.actuator_type} rotates clockwise")
        effector.close()

# Simulates the programmed logic the systme follows
def controller_agent(pressure):
    
    # If the pressure is too high, turn the motor left to open the valve
    if pressure > 15:
        print("   Pressure is too high!")

        # Dont need to open it if its already closed
        if effector.get_state() == "closed":
            # Send signal from actuator to end effector
            actuator.rotate_left(effector)
        else:
            print("   Pressure is currently being releaved")

    # If the pressure is too low, turn the motor right to close the valve
    elif pressure < 11:
        print("   Pressure is too low!")

        # Dont need to close it if its already closed
        if effector.get_state() == "open":
            # Send signal from actuator to end effector
            actuator.rotate_right(effector)
        else:
            print("   Please wait for the pressure to rebuild...")


simulation_loops = 12

# Initialize Objects
sensor = PressureSensor(18.25)
effector = Valve()
actuator = Motor()

# Initiate simulated loop
while simulation_loops > 0:

    pressure = sensor.read_current_pressure()

    print(f"Pressure is currently at {pressure} Pascals and the valve is {effector.get_state()}")

    # Call Controller Agent
    controller_agent(pressure)

    # simulates the pressure sensor seeing an update in pressure
    # based on the current state of the system
    if effector.get_state() == "closed": 
        sensor.update_pressure(pressure + 1)
    elif effector.get_state() == "open": 
        sensor.update_pressure(pressure - 1)

    simulation_loops -= 1