#Adam NOwak 
import sys
import pygame
import random

pygame.init()
grid_size = 30
width = 10
height = 10
size = (width, height) = (grid_size * width, grid_size * height)

WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (220,20,60)
PURPLE = (148,0,211)

screen = pygame.display.set_mode(size)   
pygame.display.set_caption('Snake')

fps = pygame.time.Clock()

#STARTING POSITIONS
snake_body = [[5, 5]]  
snake_direction = 'RIGHT'

fruit_pos = [random.randint(0, width // grid_size -1 ), random.randint(0, height // grid_size- 1)]
bad_fruit_pos = [random.randint(0, width // grid_size -1 ), random.randint(0, height // grid_size- 1)]

score = 0 
speed = 3

fruit_time_limit = 7 #max time of existing 
fruit_timer = 0  
bad_fruit_timer = 0


#regenerating bad fruit position if it equals fruit position
def check_fruit_position(fruit_pos, bad_fruit_pos):
    while fruit_pos == bad_fruit_pos:
        bad_fruit_pos = [random.randint(0, width // grid_size -1 ), random.randint(0, height // grid_size- 1)]

check_fruit_position(fruit_pos, bad_fruit_pos)

def draw_grid():
    #iteration through columns and rows
    for x in range(0, width, grid_size):
        for y in range(0, height, grid_size):
            rect = pygame.Rect(x, y, grid_size, grid_size) # creating rectangle i point (x,y) with size (grid_size)
            pygame.draw.rect(screen, GRAY, rect, 1) # drawing on rectangle on screen 

def draw_snake(body):
    for part in body: 
        rect = pygame.Rect(part[0] * grid_size, part[1] * grid_size, grid_size, grid_size)
        pygame.draw.rect(screen, GREEN, rect) #drawing snake on screen 

#correcting snake positon in case of meeting with a border
def wrap_position(position, grid_width, grid_height):
    position[0] %= grid_width # left border = (-1) % 20 == 19 so snake appears on the right side 
    position[1] %= grid_height

#drawing druits 
def draw_fruit(position):
    rect = pygame.Rect(position[0] * grid_size, position[1] * grid_size, grid_size, grid_size)
    pygame.draw.rect(screen, RED, rect)
    
def draw_bad_fruit(position): 
    rect = pygame.Rect(position[0] * grid_size, position[1] * grid_size, grid_size, grid_size)
    pygame.draw.rect(screen, PURPLE, rect)

def draw_score(score):
    font = pygame.font.Font(None, 36)  
    text = font.render(f'Score: {score}', True, WHITE)
    screen.blit(text, (10, 10)) 

def game_over(score): 
    font = pygame.font.Font(None, 30)  
    text = font.render(f'Game Over! Your Score {score}', True, RED)
    screen.blit(text, (20, size[1]//2))
    pygame.display.flip()
    pygame.time.delay(3000)  
    pygame.quit()
    sys.exit()


while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #ending game if user presses opposite buttons after each other
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if snake_direction == 'DOWN': 
                    game_over(score)
                snake_direction = 'UP'
            elif event.key == pygame.K_DOWN:
                if snake_direction == 'UP':
                    game_over(score)
                snake_direction = 'DOWN'
            elif event.key == pygame.K_LEFT:
                if snake_direction == 'RIGHT':
                    game_over(score)
                snake_direction = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                if snake_direction == 'LEFT':
                    game_over(score)
                snake_direction = 'RIGHT'


    #resprawning fruits - if they are not eaten for more then 7s
    current_time = pygame.time.get_ticks() / 1000  #conversion to seconds 
    if current_time - fruit_timer >= fruit_time_limit: #if fruits exists for too long - without eating them 
        fruit_pos = [random.randint(0, width // grid_size - 1), random.randint(0, height // grid_size - 1)]
        check_fruit_position(fruit_pos, bad_fruit_pos)
        fruit_timer = current_time  # Reset the timer
    
    if current_time - bad_fruit_timer >= fruit_time_limit:
        bad_fruit_pos = [random.randint(0, width // grid_size -1 ), random.randint(0, height // grid_size- 1)]
        check_fruit_position(fruit_pos, bad_fruit_pos)
        bad_fruit_timer = current_time


    #analyzing user move and create new snake part in correct direction
    new_part = snake_body[0][:] #coping current head position and calculating new one 
    if snake_direction == 'UP':
        new_part[1] -= 1
    if snake_direction == 'DOWN':
        new_part[1] += 1
    if snake_direction == 'LEFT':
        new_part[0] -= 1
    if snake_direction == 'RIGHT':
        new_part[0] += 1

    if new_part in snake_body[1:]:
        game_over(score)

    # width / grid_size - to convert screen posion to actual one. 
    # wrap_postion is used to allow snake to go through walls
    wrap_position(new_part, width // grid_size, height // grid_size)

    snake_body.insert(0, new_part) # inserting new part to snake which now is snake head (always - every tick)

    #increasing speed, score and generating new fruit if snake head equals fruit position
    if snake_body[0] == fruit_pos:
        fruit_pos = [random.randint(0, width // grid_size - 1), random.randint(0, height // grid_size - 1)]
        check_fruit_position(fruit_pos, bad_fruit_pos)
        score +=1
        speed +=0.5
        fruit_timer = current_time #reseting timer after eating
        
    else:
        if len(snake_body) > 2: #only if snake is longer 1 part its tail can be deleted in other case bad fruit is ignored 
            if snake_body[0] == bad_fruit_pos:
                bad_fruit_pos = [random.randint(0, width // grid_size - 1), random.randint(0, height // grid_size - 1)]
                check_fruit_position(fruit_pos, bad_fruit_pos)
                score -=1
                speed -=0.5
                bad_fruit_timer = current_time 
                snake_body.pop() #extra pop when eat bed fruit - decreasing snake size 
            #usual pop beacause every interation we are adding new part and only if head position matches fruit position then we increase and dont pop
        snake_body.pop() 


    screen.fill(BLACK)
    draw_grid()
    draw_snake(snake_body)
    draw_fruit(fruit_pos)
    draw_bad_fruit(bad_fruit_pos)
    draw_score(score)
    pygame.display.flip()
    fps.tick(speed) #controlled by the score value (eaten fruits)

     
    