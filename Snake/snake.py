#%%
import pygame
import random
import Qlearning
import Sarsa
import matplotlib.pyplot as plot

pygame.init()

#%% CONSTANTS
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

BLOCK_SIZE = 10 
DIS_WIDTH = 600
DIS_HEIGHT = 400

QVALUES_N = 100
FRAMESPEED = 5000000

#%% Game 

# Everytime we call this function, it will play a game.
def GameLoop():
    global dis
    
    dis = pygame.display.set_mode((DIS_WIDTH, DIS_HEIGHT))
    pygame.display.set_caption('Snake')
    clock = pygame.time.Clock()

    # Starting position of snake
    x1 = DIS_WIDTH / 2
    y1 = DIS_HEIGHT / 2
    x1_change = 0
    y1_change = 0
    snake_list = [(x1,y1)]
    length_of_snake = 1

    # Create first food
    foodx = round(random.randrange(0, DIS_WIDTH - BLOCK_SIZE) / 10.0) * 10.0
    foody = round(random.randrange(0, DIS_HEIGHT - BLOCK_SIZE) / 10.0) * 10.0

    dead = False
    reason = None
    while not dead:
        # Get action from agent
        action = agent.act(snake_list, (foodx,foody))
        if action == "left":
            x1_change = -BLOCK_SIZE
            y1_change = 0
        elif action == "right":
            x1_change = BLOCK_SIZE
            y1_change = 0
        elif action == "up":
            y1_change = -BLOCK_SIZE
            x1_change = 0
        elif action == "down":
            y1_change = BLOCK_SIZE
            x1_change = 0

        # Move snake
        x1 += x1_change
        y1 += y1_change
        snake_head = (x1,y1)
        snake_list.append(snake_head) # The extra part of snake will be deleted at line 86

        # Check if snake is off screen
        if x1 >= DIS_WIDTH or x1 < 0 or y1 >= DIS_HEIGHT or y1 < 0:
            reason = 'Screen'
            dead = True

        # Check if snake hit tail
        if snake_head in snake_list[:-1]:
            reason = 'Tail'
            dead = True

        # Check if snake ate food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, DIS_WIDTH - BLOCK_SIZE) / 10.0) * 10.0
            foody = round(random.randrange(0, DIS_HEIGHT - BLOCK_SIZE) / 10.0) * 10.0
            length_of_snake += 1

        # Delete the last cell since we just added a head for moving, unless we ate a food
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Found out the next action
        agent.next_act(snake_list, (foodx,foody)) # This function is used for Sarsa specifically

        # Draw food, snake and update score
        dis.fill(BLUE)
        DrawFood(foodx, foody)
        DrawSnake(snake_list)
        DrawScore(length_of_snake - 1)
        pygame.display.update()

        # Update Q Table
        agent.UpdateQValues(reason)
        
        # Next Frame
        clock.tick(FRAMESPEED)

    return length_of_snake - 1, reason

def DrawFood(foodx, foody):
    pygame.draw.rect(dis, GREEN, [foodx, foody, BLOCK_SIZE, BLOCK_SIZE])   

def DrawScore(score):
    font = pygame.font.SysFont("comicsansms", 35)
    value = font.render(f"Score: {score}", True, YELLOW)
    dis.blit(value, [0, 0])

def DrawSnake(snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, BLACK, [x[0], x[1], BLOCK_SIZE, BLOCK_SIZE])


#%%
qlearning_result = []
sarsa_result = []
game_round = 400
# Q-Learning Part ------------------------------------------------------------------------------------------------
game_count = 1

agent = Qlearning.Learner(DIS_WIDTH, DIS_HEIGHT, BLOCK_SIZE)

while game_count <= game_round:
    # Terminate the game
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            pygame.quit()

    agent.Reset() # reset state/action history
    if game_count > 200: # Turn off the epsilon part.
        agent.epsilon = 0
    # else:
    #     agent.epsilon = .1
    score, reason = GameLoop()

    qlearning_result.append(score)

    print(f"Games: {game_count}; Score: {score}; Reason: {reason}") # Output results of each game to console to monitor as agent is training
    game_count += 1
    if game_count % QVALUES_N == 0: # Save qvalues every qvalue_dump_n games
        print("Save Qvals")
        agent.SaveQvalues()

# Sarsa Part ------------------------------------------------------------------------------------------------
print("Training Sarsa")
game_count = 1

agent = Sarsa.Learner(DIS_WIDTH, DIS_HEIGHT, BLOCK_SIZE)

while game_count <= game_round:
    # Terminate the game
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            pygame.quit()

    agent.Reset()
    if game_count > 200:
        agent.epsilon = 0
    # else:
    #     agent.epsilon = .1
    score, reason = GameLoop()

    sarsa_result.append(score)

    print(f"Games: {game_count}; Score: {score}; Reason: {reason}") # Output results of each game to console to monitor as agent is training
    game_count += 1
    if game_count % QVALUES_N == 0: # Save qvalues every qvalue_dump_n games
        print("Save Qvals")
        agent.SaveQvalues()

q_r = []
s_r = []
x_axis = []

# Rolling 30 Average
for start in range(len(qlearning_result)-30):
    q_r.append(sum(qlearning_result[start:start+31])/30)
    s_r.append(sum(sarsa_result[start:start+31])/30)

for i in range(30, len(qlearning_result)):
    x_axis.append(i)

plot.plot(x_axis, q_r, label = 'Q-Learning')
plot.plot(x_axis, s_r, label = "Sarsa")
plot.legend()
plot.title("Sarsa vs Q-Learning")
plot.xlabel("Games")
plot.ylabel("Score")
plot.show()