import sys, pygame, math, random

# starts the simulation
pygame.init()

# tile size for screen and rover movement
tile = 50

# sets window size
size = width, height = (600, 400)

# background color
black = 0,0,0

# initializes window
screen = pygame.display.set_mode(size)

# creates rover
rover = pygame.Rect(tile ,size[1]/2 - tile,tile,tile)
rover_image = pygame.image.load("car.png")

# creates the obstacle, in this case a boulder
obstacle = pygame.Rect(size[0]/2 - tile*2, size[1]/2 - tile, tile, tile)

# Set the goal, which is a beacon
goal = pygame.Rect(size[0] -tile *4, size[1]/2 - tile, tile, tile)

# Calculates the distance between the rover and the goal
# The rover is trying to reach a beacon, the rover sends out a radio signal
# the beacon then sends one back, and the rover can calculate the distance 
# based on how long it took for the signal to return
def calcDistance(x1, y1, x2, y2):
    return math.floor(math.sqrt(abs(x2 - x1)+abs(y2 - y1)) * tile / 100) -1

def agent(rover, approached_obstacle : bool, distance_to_goal :int):

    # if the goal is close enough, approach it directly
    if distance_to_goal == 1.0:
        return rover.move(0, -rover.height)
    # move forward one unit if not prevented
    elif not approached_obstacle and distance_to_goal > 0:
        print(f"The rover moves one unit forward, and is now {distance_to_goal} units from the goal!")
        return rover.move(rover.width, 0)
    # Try to move around the obstacle if you hit it
    elif approached_obstacle and distance_to_goal > 0:
        print(f"There's a boulder in the way. Attempting to circumnavigate...")
        # For the sake of the simulation lets say there's a 50/50 chance that the rover can get the obstacle
        # On a success, it can move again in the next time unit, on a failure
        # it must try to get past the obstacle again
        prob = random.randint(1,100)
        if prob >= 50:
            # move down on success
            return rover.move(0, rover.height)
        else:
            # dont move on failure
            print("Rover Failed to move, will try again next turn")
            return rover
    else:
        print("Rover has reached its destination!")

# set the simulation time limit
simulation_units = random.randint(1,7)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # initialize hit variable
    hit = False
    # color background
    screen.fill(black)

    # draw objects to screen
    screen.blit(rover_image, rover)
    pygame.draw.rect(screen, "red", rover)
    pygame.draw.rect(screen, "blue", obstacle)
    pygame.draw.rect(screen, "green", goal)

    # it senses the boulder through a contact sensor (through bumping into it directly)
    if obstacle.topleft == rover.topright:
        hit = True

    # call the movement agent
    rover = agent(rover, hit, calcDistance(rover.centerx,rover.centery, goal.centerx, goal.centery))

    # make time move forward one unit
    pygame.display.update()
    pygame.time.delay(500)

    # end the game if it fails to reach the goal in time
    if simulation_units == 0:
        pygame.quit()
        sys.exit()
    
    # move time forward one unit
    simulation_units -= 1

# Performance Measure: 
# 
# (Distance Traveled / Total distance) + [1 - (time taken / time alloted)]
#
# Grade based on how close the rover got to the beacon
# 
# this system also grants additional points based on 
# how long it took to get there in the alloted time 