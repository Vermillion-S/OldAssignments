import sys, pygame, math, random, time

# 1 px = 1 inch

# Constants

TPS = 30 # Ticks per Second


keyboardControl = False # True  = Keyboard Control Mode
						# False = Agent SImulation Mode

robotspeed = 20.0 # inches per tick (Actuator rotational speed)
				  # 20 in/tick * 30 ticks/sec = 60 inches per second

screensize = scr_width, scr_height = (800, 600) # screen size

obstacleWidth, obstacleHeight = [100, 300]
obstacleX, obstacleY = [screensize[0]/2 -obstacleWidth/2,screensize[1]/2 -obstacleHeight/2]
goalWidth, goalHeight = [50, 50]

# Colors
red = (200, 0, 0)
blue = (0, 0, 255)
green = (0, 155, 0)
yellow = (155, 155, 0)
white = (255, 255, 255)
black = (0, 0, 0)

# Actuator Class
class Motor():
	# Initiate the class
	def __init__(self, name):
		# Name
		self.actuatortype = name

	# Class method that activates the motor, and in turn moves the end effector
	def drive(self, forward : bool, amount, effector):
			
			error = 1 + (random.randint(10,20) / 100) # 10%-20% positive error
			
			# If direction is forward
			if forward:
				# Move forward by turn amount (speed)
				print(f"The {self.actuatortype} drives forward by {amount}, turning the axle")
				return effector.turn(1 * abs(amount) * error)
			else:
				# Otherwise Move forward by turn amount (speed)
				print(f"The {self.actuatortype} drives backward by {amount}, turning the axle")
				return effector.turn(-1 * abs(amount) * error)

# End effector class
class Wheel():
	# Constructor
	def __init__(self, name, radius):
		# Name
		self.effectorType = name
		# rotation
		self.rotationAngle = 0.0
		# Wheel Radius
		self.radius = radius
	# Turns The Wheel (Called by Actuator)
	def turn(self, angle):
		# convert angle to radians
		angleToRadian = angle * (math.pi/180)
		# Turns wheel by a certain amount
		self.rotationAngle += angle
		# clamps rotation to 360 degrees
		self.rotationAngle %= 360

		# Calculate the distance traveled based on the rotation angle
		# distance = r * θ
		distance = self.radius * angleToRadian
		error = 1 + (random.randint(10,20) / 100) # 10%-20% positive error
		# Print movement
		print(f"The {self.effectorType} turns by {angle} degrees, moving the robot {distance * error:.2f} inches (including error of +{((error-1) * 100):.2f}%)")
		# Return distance wheel travels (with added error)
		return distance * error

# Class for Robot Object
class Robot:
	# Starting values
	def __init__(self,x,y):
		# Image
		self.car_img = pygame.image.load("img/rover.png")
		
		# Position/Rotation
		self.x = x
		self.y = y
		self.orientation = 0

		# Collision Detection
		self.collisionbox = self.car_img.get_rect()
		self.collisionflag = False
		
		# Width / Height
		self.width = self.car_img.get_width()
		self.height = self.car_img.get_height()

		# Motors
		self.lMotor = Motor("Left Motor")
		self.rMotor = Motor("Right Motor")

		# Wheels
		self.lWheel = Wheel("Left Wheel Track", 5)
		self.rWheel = Wheel("Right Wheel Track", 5)
	
	# Instantly sets location and orientation
	def set(self, x, y,orientation):
		self.x = x
		self.y = y
		self.orientation = orientation

	# Checks for collision of a future movement
	def checkCollision(self, linearVelocity, obstacle):
		#check for future collision
		future_rect = self.collisionbox.copy()
		#Moves predicted box
		future_rect.x += linearVelocity * math.cos(self.orientation*math.pi/180) # X Translation
		future_rect.y -= linearVelocity * math.sin(self.orientation*math.pi/180) # Y Translation
		# If the future collision detects an obstacle...
		if future_rect.colliderect(obstacle):
			return True # Return True
		return False # Else Return False
	
	# Calls actuators To rotate wheels
	# Based on wanted parameters
	def move(self, turn, forward, obstacle):
		# Reset collision flag
		self.collisionflag = False

		#Movement through differential drive
		linearVelocity = 0.0 # How much to move by
		angularVelocity = 0.0 # How much to turn by

		#Print starting position and orientation
		if turn != 0 or forward != 0:
			print(f"Robot starting position: ({self.x:.2f}, {self.y:.2f}), orientation: {self.orientation:.2f} degrees")

		# Call acutators through inverse kinematics (I.E: Mathmatically determine actuations through the end result we want)
		# calculate both angular and linear velocity since random error may cause both
		# to change during either turn or forward movement regardless of command

		# Turn command (Negative = Left turn; Pos = right turn)
		if turn != 0:

			# Actuate motors, which turn wheels, which return how much distance they moved
			# Rotate in opposite directions
			leftTurn = self.lMotor.drive(turn < 0, abs(turn), self.lWheel) ## Left motor
			rightTurn = self.rMotor.drive(turn > 0, abs(turn), self.rWheel) ## Right motor
			
			# Calculate rotation
			angularVelocity = (leftTurn - rightTurn) / 2
			# Calculate movement
			linearVelocity = (leftTurn + rightTurn) / 2
			#Print out movement values
			print(f"Results in {angularVelocity:.2f} degrees turn, new orientation is {self.orientation + angularVelocity:.2f} degrees")

		# Forward command [Overwrites turn command] (Negative = Backwards, Pos = Forwards)
		if forward != 0:
			# Actuate motors, which turn wheels, which return how much distance they moved
			# Rotate In same direction
			leftdistance = self.lMotor.drive(forward > 0, abs(forward), self.lWheel) ## Left Motor
			rightdistance = self.rMotor.drive(forward > 0, abs(forward), self.rWheel) ## Right Motor
			
			# Calculate forward movement
			linearVelocity = (leftdistance + rightdistance) / 2
			# Calculate rotation
			angularVelocity += (rightdistance - leftdistance) / (self.width / 2)
			#Print out movement values
			print(f"Results in {linearVelocity:.2f} inches forward, new position is ({self.x + linearVelocity * math.cos(self.orientation*math.pi/180):.2f}, {self.y - linearVelocity * math.sin(self.orientation*math.pi/180):.2f})")

		# Update rotation
		self.orientation += angularVelocity

		# Update position
		self.x += linearVelocity * math.cos(self.orientation*math.pi/180) # Horizontal movement
		self.y -= linearVelocity * math.sin(self.orientation*math.pi/180) # Vertical Movement

		# Check for potential collisions
		# If there is a collision...
		if self.checkCollision(linearVelocity, obstacle):
			print("Collision detected! Stopping movement.") # Send Message
			self.collisionflag = True # Set flag
			# Reverse the movement to simulate the obstacle stopping the rover
			self.x -= linearVelocity * math.cos(self.orientation*math.pi/180)
			self.y += linearVelocity * math.sin(self.orientation*math.pi/180)
		
		# Clamp values to bounds
		self.orientation %= 360

		# Prevent Rover from leaving the screen
		if self.x < 0:
			self.x = 0
		elif self.x > scr_width:
			self.x = scr_width
		if self.y < 0:
			self.y = 0
		elif self.y > scr_height:
			self.y = scr_height

		# Update the collision box position
		self.collisionbox.topleft = (self.x - self.width // 2, self.y - self.height // 2)

		#print out new position and orientation if there was movement
		if linearVelocity != 0:
			print(f"[NEW] Robot position: ({self.x:.2f}, {self.y:.2f})") # Movement message
		if angularVelocity != 0:
			print(f"[NEW] Robot orientation: {self.orientation:.2f} degrees") # Rotation Message

	# Draws Robot To screen
	def draw(self):
		#Draw collision box for debugging
		pygame.draw.rect(screen, yellow, self.collisionbox, 2)
		# Rotates image based on robot orientation
		rotated = pygame.transform.rotate(self.car_img, self.orientation)
		# Get Rotated Rect
		rect = rotated.get_rect()
		# Set center point
		rect.center = (self.x, self.y)
		# Attach rotated image to rect object
		screen.blit(rotated, rect)

# Definition for Robot Controller Agent
class ControllerAgent:
	# Constructor
	def __init__(self, pauseLength = 500.0):
		# How many cycles its been since last command
		self.waittime = pauseLength

		# Length of time between commands
		self.pauseLength = pauseLength

		# Saves last commmands
		self.lastDeltaForward = 0.0
		self.lastDeltaOrient = 0.0
		self.commandIndex = 0
		
		# Flag for moving to next command
		self.lastCommandFinished = False

	# Test method (Used this to test if the controller was working)
	def randomMovement(self):
		# If there is still time until next command...
		if self.waittime > 0:
			# Decrease wait time
			self.waittime -= 1
			# Perform last command
			return self.lastDeltaOrient, self.lastDeltaForward
		else: # otherwise...
			# Make a 50/50 choice 
			# First choice
			if random.randint(0,1) == 0:
				# Turn in a random direction
				self.lastDeltaOrient = random.randint(-robotspeed,robotspeed)
				self.lastDeltaForward = 0.0
				# Print Decision
				print(f"Robot decides to turn {self.lastDeltaOrient} degrees")
			else: # Second Choice
				# Move forward at a random speed
				self.lastDeltaOrient = 0.0
				self.lastDeltaForward = random.randint(1, robotspeed)
				# Print Decision
				print(f"Robot decides to move forward {self.lastDeltaForward} inches")
			# Reset wait time
			self.waittime = self.pauseLength  # Reset waittime after new command
			# return new command
			return self.lastDeltaOrient, self.lastDeltaForward

	# Real controller agent (Moves rover based on preset movements)
	def Command(self, rover: Robot, obstacle: pygame.Rect, goal: pygame.Rect):
		# List of comands, and their respective completion flags
		commandlist = [
			{
				# Move forward until it reaches to the obstacle
				"Action" : (0.0, robotspeed),
				"Flag" : rover.collisionflag
			},{
				# Move backwards for pauselength duration (1 second)
				"Action" : (0.0, -robotspeed),
				"Flag" : self.waittime == 0
			},{
				# Turn until it faces down (Take range to handle variance in actuation)
				"Action" : (robotspeed,0.0),
				"Flag" : rover.orientation >= 265 and rover.orientation <= 275
			},{
				# Move forward until it reaches the same y level as the goal
				"Action" : (0.0, robotspeed),
				"Flag" : rover.y >= goal.y
			},{
				# Rotate until it faces right (Take range to handle variance in actuation)
				"Action" : (-robotspeed,0.0),
				"Flag" : rover.orientation <= 5 or rover.orientation >= 355
			},{
				# Move forward until it reaches the goal
				"Action" : (0.0, robotspeed),
				"Flag" : None
			}
		]

		# If the last command finished
		if self.lastCommandFinished:
			# Reset timer
			self.waittime = self.pauseLength
			# Reset Flag
			self.lastCommandFinished = False
			# Move on to the next command
			self.commandIndex = (self.commandIndex + 1)
			# If we have gone past the last command, stop
			if self.commandIndex >= len(commandlist):
				return 0.0, 0.0 # Override movement
		
		# Get current command
		currentCommand = commandlist[self.commandIndex]

		# Get movement parameters from commmand Action
		self.lastDeltaOrient, self.lastDeltaForward = currentCommand["Action"]

		# Check to see if completion requirement is met
		if currentCommand["Flag"]:
			self.lastCommandFinished = True

		# count down timer
		self.waittime -= 1

		# Return the current command's action
		return self.lastDeltaOrient, self.lastDeltaForward

# Simulates PyGame environment
class Simulator(object):
	# Main call
	def main(self , screen , robot):
		# Cpu Clock
		clock = pygame.time.Clock()
		# Initialize controller
		controllerAgent = ControllerAgent(TPS) # Pause Timer = 1 second
		
		# Create Obstacle object
		obstacle = pygame.Rect(obstacleX, obstacleY, obstacleWidth, obstacleHeight)

		# create goal object
		
		goal = pygame.Rect(screensize[0] -100, screensize[1] -100, goalWidth, goalHeight)
		
		# Robot control variables
		delta_orient = 0.0
		delta_forward = 0.0
		# Simulation Loop
		while 1:
			# Move time 
			clock.tick(TPS)
			# Draw background
			screen.fill(white)
			robot.draw()
			# Draw Obstacle and Goal
			pygame.draw.rect(screen, red, obstacle)
			pygame.draw.rect(screen, green, goal)
			# Quit Event
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
			# Keyboard controller
			if keyboardControl:
				# Get Keypress
				keys = pygame.key.get_pressed()
				# Left Keypress >> turn left
				if keys[pygame.K_LEFT]:
					delta_orient = -robotspeed
				# Right Keypress >> turn right
				elif keys[pygame.K_RIGHT]:
					delta_orient = robotspeed
				else:
					# otherwise dont turn
					delta_orient = 0.0
				# Up keypress >> move forward
				if keys[pygame.K_UP]:
					delta_forward = robotspeed
				# Down Keypress >> move backwards
				elif keys[pygame.K_DOWN]:
					delta_forward = -robotspeed
				else:
					# Otherwise dont move
					delta_forward = 0.0
			else:
				# Call Controller commander if NOT using Keyboard Controls
				delta_orient, delta_forward = controllerAgent.Command(robot, obstacle, goal)

			#close the program if robot reaches the goal
			if robot.collisionbox.colliderect(goal):
				print("Goal reached!") # Win Message
				pygame.quit()
				sys.exit()
			
			# Move robot based on Controller Commands
			robot.move(delta_orient, delta_forward, obstacle)
			# Draw robot to screen
			robot.draw()

			# Display content
			pygame.display.flip()

# Main
if __name__ == '__main__':
	# Start Pygame
	pygame.init()
	# Window Title
	pygame.display.set_caption("Rover Simulation")
	# Create Window
	screen = pygame.display.set_mode(screensize)
	# create robot
	robot_instance = Robot(100, scr_height/2)

	# Metacontext Info display
	print(f"The simulation environment is {scr_width}x {scr_height} inches")
	print(f"The rover has 2 wheels, each with a radius of{robot_instance.lWheel.radius} inches")
	print(f"the main obstacle (Seen in red) spans from {obstacleX}, {obstacleY} to {(obstacleX+obstacleWidth)}, {(obstacleY+obstacleHeight)}")

	# Wait for 3 seconds before going to simulation
	# So user can read meta context
	time.sleep(3)
	# Run simulator
	Simulator().main(screen, robot_instance)