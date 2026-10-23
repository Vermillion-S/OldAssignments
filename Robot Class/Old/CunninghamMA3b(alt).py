import random

def agent(approached_obstacle, distance_to_goal):
    # Sets the flag for rover behavior:
    # 0 = Cant move forward, try again
    # 1 = Navigated Obstacle, move next turn
    # 2 = Can move without issue
    move_next = 0
    
    if not approached_obstacle and distance_to_goal > 0:
        print("Rover Senses the path is clear...")
        move_next = 2
        print(f"Rover moves one unit forward, and is now {distance_to_goal-1} units from the goal!")
        return move_next
    elif approached_obstacle:
        print(f"There's a boulder in the way. Attempting to circumnavigate...")
        # For the sake of the simulation lets say there's a 50/50 chance that the rover can get the obstacle
        # On a success, it can move again in the next time unit, on a failure
        # it must try to get past the obstacle again
        prob = random.randint(1,100)
        if prob >= 50:
            move_next = 1
            print(f"Navigating Success! The Rover can now move again!")
            return move_next
        elif prob < 50:
            move_next = 0
            print("Failed to navigate obstacle. Will try again next time unit")
    else:
        print("Rover has reached its destination!")
        
time_units = 1

time_limit = random.randint(1,7)

# The rover is trying to reach a beacon, the rover sends out a radio signal
# the beacon then sends one back, and the rover can calculate the distance 
# based on how long it took for the signal to return
distance = 5

while time_units <= time_limit:
    hit = False
    print(f"--Time Unit {time_units} of {time_limit} ")
    
    # there's a boulder in the rovers path at distance 3
    # it senses the boulder through a contact sensor (through bumping into it directly)
    if distance == 3:
        hit = True

    # Sets the flag for rover behavior:
    # 0 = Cant move forward, try again
    # 1 = Navigated Obstacle, but move a bit less this turn due
    #       to the time taken to circumnavigate
    # 2 = Can move without issue
    decision = agent(hit, distance)

    if decision == 0:
        pass
    elif decision == 1:
        hit = False

    elif decision == 2:
        distance -= 2

    if time_units == time_limit:
        print("Sorry, the rover has failed to reach the beacon in the alloted time")

    time_units += 1

# Performance Measure: 
# 
# (Distance Traveled / Total distance) + [1 - (time taken / time alloted)]
#
# Grade based on how close the rover got to the beacon
# 
# this system also grants additional points based on 
# how long it took to get there in the alloted time 