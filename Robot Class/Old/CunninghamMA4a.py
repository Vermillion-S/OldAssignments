import sys, pygame, random

# starts the simulation
pygame.init()

# sets window size
size = width, height = (1200, 800)

# background color
black = 0,0,0

# initializes window
screen = pygame.display.set_mode(size)

# creates rover
#load image
rover_image = pygame.image.load("image/car.png")
#get image dimentions
rover_dimentions = rover_image.get_size()
#create rectangle with a random start position,
# and the dimentions of the loaded image
rover = pygame.Rect(random.randint(0, width - rover_dimentions[0]),
                    random.randint(0, height - rover_dimentions[1]),
                    rover_dimentions[0],
                    rover_dimentions[1])

#Create Goal
#load image
goal_image = pygame.image.load("image/flag.png")
#get image dimentions
goal_dimentions = goal_image.get_size()
#create rectangle with a random start position,
# and the dimentions of the loaded image
goal = pygame.Rect(random.randint(0, width - goal_dimentions[0]),
                   random.randint(0, height - goal_dimentions[1]),
                   goal_dimentions[0],
                   goal_dimentions[1])

# agent for controlling rover movments
def agent(character : pygame.Rect, destination):
    # initial vector for movement
    speed = [0,0]
    
    # Dont move if you reach the destination
    if character.colliderect(destination):
        # Tell user you have reached the goal
        print("You have reached the goal")
        # return the unmodified speed value
        return speed
    
    # Variable to decide if the rover will move 
    # left/right(0) or up/down(1)
    movementaxis = 0

    # Calculates the difference between the X positions of the goal and rover
    xdifferece = destination.centerx - character.centerx
    # Calculates the difference between the Y positions of the goal and rover
    ydifference = destination.centery - character.centery

    # If the difference in x values is greater than 
    # the distance in Y values...
    if abs(xdifferece) > abs(ydifference):
        # The movement axis is horizontal
        movementaxis = 0
    #otherwise the movement axis is vertical
    else: movementaxis = 1
    # if the distance bewteen the destination and rover (in the given axis) 
    # is positive.....
    if destination.center[movementaxis] > character.center[movementaxis]:
        # Move one unit in the positive direction of the given axis
        speed[movementaxis] = character.size[movementaxis]
    # Otherwise move one unit in the negative direction of the given axis
    else: speed[movementaxis] = -character.size[movementaxis]

    # return the modified vector
    return speed


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
    screen.blit(rover_image, rover)
    
    #draw goal to screen
    screen.blit(goal_image, goal)

    # set the movemement direction for this iteration and save it to a speed value
    speed = agent(rover, goal)
    # move rover by the speed value
    rover = rover.move(speed)

    # If the rover does not move, it means it has 
    # reached its destination and the program can end
    if speed == [0,0]:
        #quit pygame
        pygame.quit()
        # Close window
        sys.exit()

    # make time move forward one unit
    pygame.display.update()
    # wait before next update
    pygame.time.delay(500)

