import sys, pygame, random, math

# starts the simulation
pygame.init()

tile_size = 50

# sets window size
size = width, height = (10*tile_size, 10*tile_size)

# background color
black = 0,0,0

# initializes window
screen = pygame.display.set_mode(size)

# creates rover

#create rectangle with a random start position,
rover = pygame.Rect(2*tile_size,
                    7*tile_size,
                    tile_size,
                    tile_size)

#Create Goal
goal_dimentions = [50,50]
#create rectangle with a random start position,
# and the dimentions of the loaded image
goal = pygame.Rect(8*tile_size,
                   2*tile_size,
                   tile_size,
                   tile_size)

def clampangle(angle):
    if angle < 0:
        angle = angle + 360
    elif angle > 360:
        angle = angle - 360
    elif angle == 360:
        angle = 0

    return angle

def camerasensor(xpos, ypos, angle):
    # Sightline
    # first point centered on rover
    point1 = (xpos, ypos)
    # second point to where the rover's sensor is facing
    point2 = (xpos + (width * math.cos(math.radians(angle))), ypos - (height * math.sin(math.radians(angle))))
    
    # If the line of sight collides with the goal
    # it means the sensor can see it
    if goal.clipline(point1, point2):
        return (math.sqrt((xpos - goal.centerx)**2 + (ypos - goal.centery))**2) / tile_size**2
    else:
        return -1

# agent for controlling rover movments
def agent(angle, xpos, ypos):    
    speed = [0,0]
    
    sensorval = camerasensor(xpos, ypos, angle)

    if sensorval != -1 and sensorval > 0:
        print(f"Goal in sight, and is {sensorval} units away. Moving forward")
        speed[0] = tile_size * math.cos(math.radians(angle))
        speed[1] = tile_size * -math.sin(math.radians(angle))
    elif sensorval == 0:
        print('You have reached the goal')
        return speed, -1
    elif angle == 90:
        speed[1] = -tile_size
        angle+=90
    else: angle+=90

    return speed, clampangle(angle)

angle = 0

#sets the event loop
while 1:
    # closes the program on quit
    for event in pygame.event.get():
        # If the game quit
        if event.type == pygame.QUIT:
            #quit pygame
            pygame.quit()
            # close the window
            sys.exit()

    # color background
    screen.fill(black)

    # draw rover to screen
    pygame.draw.rect(screen, "red", rover)
    
    #draw goal to screen
    pygame.draw.rect(screen, "green", goal)

    point1 = [rover.centerx, rover.centery]
    point2 = [rover.centerx + (width * math.cos(math.radians(angle))), rover.centery - (height * math.sin(math.radians(angle)))]
    
    pygame.draw.line(screen, "white", point1, point2)

    speed, angle = agent(angle, rover.centerx, rover.centery)

    if angle == -1:
        pygame.quit()
        # close the window
        sys.exit()

    rover = rover.move(speed[0], speed[1])
        
    

    # If the rover does not move, it means it has 
    # reached its destination and the program can end

    # make time move forward one unit
    pygame.display.update()
    # wait before next update
    pygame.time.delay(500)