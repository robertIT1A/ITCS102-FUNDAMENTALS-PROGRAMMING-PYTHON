def act28():
    import pygame
    import time
    import random

    # Initialize Pygame
    pygame.init()

    # Screen size
    width = 1000
    height = 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Snake Game')

    # Colors (RGB)
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)

    # Game speed and block size
    clock = pygame.time.Clock()
    speed = 20  # bilis ng galaw nung snake
    snake_block = 10  # size ng block o yung box red and green

    # Font for messages
    font_style = pygame.font.SysFont(None, 30)

    

    # Step 2
    def draw_snake(snake_list):
        for block in snake_list:
            pygame.draw.rect(screen, green, [block[0], block[1], snake_block, snake_block])

    # Step 3
    def game_loop():
        global score  # Make score global so it can be reset or accessed
        game_over = False
        game_close = False

        # Starting position of the snake
        x = width / 2
        y = height / 2

        x_change = 0
        y_change = 0

        snake_list = []
        length_of_snake = 1

        # Generate first food
        food_x = round(random.randrange(0, width - snake_block) / 10) * 10
        food_y = round(random.randrange(0, height - snake_block) / 10) * 10
        
        # for the score to count
        score = 0
        while not game_over:
            
            # Loss screen
            while game_close:
                screen.fill(black)
                message = font_style.render('Talo ka na nga sa kanya, talo ka pa dito! Press Q-Quit or C-Play Again', True, red)  # the message that you want to appear after loss
                screen.blit(message, [width / 5, height / 2.5])  # position of the message after lose
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        elif event.key == pygame.K_c:
                            score = 0  # Reset score on restart
                            game_loop()

            # Event handling (keyboard)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_change = -snake_block
                        y_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x_change = snake_block
                        y_change = 0
                    elif event.key == pygame.K_UP:
                        y_change = -snake_block
                        x_change = 0
                    elif event.key == pygame.K_DOWN:
                        y_change = snake_block
                        x_change = 0

            # Check if snake hits the wall
            if x >= width or x < 0 or y >= height or y < 0:
                game_close = True

            # Update position
            x += x_change
            y += y_change

            # Draw background and food
            screen.fill(black)
            pygame.draw.rect(screen, red, [food_x, food_y, snake_block, snake_block])

            # Add snake head
            snake_head = [x, y]
            snake_list.append(snake_head)

            # Remove extra segments if not growing
            if len(snake_list) > length_of_snake:
                del snake_list[0]

            # Check self-collision
            for segment in snake_list[:-1]:
                if segment == snake_head:
                    game_close = True

            # Draw the snake
            draw_snake(snake_list)

            # Draw the score
            score_text = font_style.render(f"Score: {score}", True, white)
            screen.blit(score_text, (10, 10))

            # Update display
            pygame.display.flip()

            # Check if snake eats food
            if x == food_x and y == food_y:
                food_x = round(random.randrange(0, width - snake_block) / 10) * 10
                food_y = round(random.randrange(0, height - snake_block) / 10) * 10
                length_of_snake += 1
                score += 1  # Increment score when food is eaten

            # Control game speed
            clock.tick(speed)

        # Quit Pygame
        pygame.quit()
        quit()

    # Start the game
    game_loop()

    
def code28():
    print("\nHere's the code for this program:")
    print("------------------------------------\n")
    print("""import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Screen size
width = 1000
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Colors (RGB)
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)

# Game speed and block size
clock = pygame.time.Clock()
speed = 20  # bilis ng galaw nung snake
snake_block = 10  # size ng block o yung box red and green

# Font for messages
font_style = pygame.font.SysFont(None, 30)



# Step 2
def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, green, [block[0], block[1], snake_block, snake_block])

# Step 3
def game_loop():
    global score  # Make score global so it can be reset or accessed
    game_over = False
    game_close = False

    # Starting position of the snake
    x = width / 2
    y = height / 2

    x_change = 0
    y_change = 0

    snake_list = []
    length_of_snake = 1

    # Generate first food
    food_x = round(random.randrange(0, width - snake_block) / 10) * 10
    food_y = round(random.randrange(0, height - snake_block) / 10) * 10
    
    # for the score to count
    score = 0
    while not game_over:
        
        # Loss screen
        while game_close:
            screen.fill(black)
            message = font_style.render('Talo ka na nga sa kanya, talo ka pa dito! Press Q-Quit or C-Play Again', True, red)  # the message that you want to appear after loss
            screen.blit(message, [width / 5, height / 2.5])  # position of the message after lose
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        score = 0  # Reset score on restart
                        game_loop()

        # Event handling (keyboard)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0

        # Check if snake hits the wall
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        # Update position
        x += x_change
        y += y_change

        # Draw background and food
        screen.fill(black)
        pygame.draw.rect(screen, red, [food_x, food_y, snake_block, snake_block])

        # Add snake head
        snake_head = [x, y]
        snake_list.append(snake_head)

        # Remove extra segments if not growing
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check self-collision
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        # Draw the snake
        draw_snake(snake_list)

        # Draw the score
        score_text = font_style.render(f"Score: {score}", True, white)
        screen.blit(score_text, (10, 10))

        # Update display
        pygame.display.flip()

        # Check if snake eats food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - snake_block) / 10) * 10
            food_y = round(random.randrange(0, height - snake_block) / 10) * 10
            length_of_snake += 1
            score += 1  # Increment score when food is eaten

        # Control game speed
        clock.tick(speed)

    # Quit Pygame
    pygame.quit()
    quit()

# Start the game
game_loop()
""")
    print("\n------------------------------------")