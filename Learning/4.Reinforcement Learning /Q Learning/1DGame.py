#https://itnext.io/reinforcement-learning-with-q-tables-5f11168862c8

import random
from random import randint
import time
environment_matrix = [[None, 0],
                      [-100, 0],
                      [0, 0],
                      [0, 0],
                      [0, 100],
                      [0, 0],
                      [100, 0],
                      [0, 0],
                      [0, 0],
                      [0, None]]

q_matrix = [[0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0]]

win_loss_states = [0, 5]

# Method for returning all the possible action
def getAllPossibleNextAction(cur_pos):
    step_matrix = [x != None for x in environment_matrix[cur_pos]]
    action = []
    if (step_matrix[0]):
        action.append(0)
    if (step_matrix[1]):
        action.append(1)
    return (action)

# Method for fetching status 
def isGoalStateReached(cur_pos):
    return (cur_pos in [6])

# Method for next state movement
def getNextState(cur_pos, action):
    if (action == 0):
        return cur_pos - 1
    else:
        return cur_pos + 1


def isGameOver(cur_pos):
    return cur_pos in win_loss_states

def gameView(cur_pos):
    win_pose = win_loss_states[1]
    loss_pose = win_loss_states[0]
    done = False
    for var in range (0,len(environment_matrix)):
        if( var == cur_pos):
            print("#", end="")
            if(var == win_pose):
                done =True
        elif( var == win_pose):
            print("W", end="")
        elif (var == loss_pose):
            print("L", end="")
        else:
            print("=", end="")
    if(done):
        print("\nMission Accomplished...")
    else:
        print()

# Method with game logic
def gameTest(startLoc):
    if ( not isGameOver(startLoc)):
        gameView(startLoc)
        while (startLoc>-1 and  startLoc<len(q_matrix)):
            if(q_matrix[startLoc][0]>q_matrix[startLoc][1]) :
                startLoc=startLoc-1
                gameView(startLoc)
            else:
                startLoc=startLoc+1
                gameView(startLoc)

            if (isGameOver(startLoc)):
                break
            time.sleep(2)

discount = 0.9
learning_rate = 0.1
for _ in range(100000):
    # get starting place
    cur_pos = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    # while goal state is not reached
    while (not isGameOver(cur_pos)):
        # get all possible next states from cur_step
        possible_actions = getAllPossibleNextAction(cur_pos)
        # select any one action randomly
        action = random.choice(possible_actions)
        # find the next state corresponding to the action selected
        next_state = getNextState(cur_pos, action)
        # update the q_matrix
        q_matrix[cur_pos][action] = q_matrix[cur_pos][action] + learning_rate * (environment_matrix[cur_pos][action] +
                                                                                 discount * max(q_matrix[next_state]) -
                                                                                 q_matrix[cur_pos][action])
        # go to next state
        cur_pos = next_state

print(q_matrix)
print("Training done...")

for _ in range(1):
    startLoc = randint(0, 9)
    print("Start Loc: ",startLoc)
    gameTest(startLoc)
