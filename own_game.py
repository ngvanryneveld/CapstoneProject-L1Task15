
# import pygame allows for the game library functions to be included in the program
# import random allows for the program to generate random numbers
import pygame
import random

# this initializes the pygames modules to get everything started
pygame.init()

# the size of the screen display will be adjusted through these variables being width and height
screen_width = 800
screen_height = 600

# this creates the screen according to the above set variables
screen = pygame.display.set_mode((screen_width, screen_height))


# this is importing the images within this folder as the various characters and items within the pygame
player = pygame.image.load("player.png")
enemy1 = pygame.image.load("monster.png")
enemy2 = pygame.image.load("monster.png")
enemy3 = pygame.image.load("monster.png")
prize = pygame.image.load("prize.png")

# this evaluates the size of the player's image and is used in the boundary detection of the pygame
player_height = player.get_height()
player_width = player.get_width()

# this evaluates the size of the enemies' images and is used in the boundary detection of the pygame
enemy1_height = enemy1.get_height()
enemy1_width = enemy1.get_width()
enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()
enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()

# this evaluates the size of the prize's image and is used in the boundary detection of the pygame
prize_height = prize.get_height()
prize_width = prize.get_width()

# this print statement is just for interest of the user to see the size of the player's character
print("This is the height of the player " + str(player_height))
print("This is the width of the player " + str(player_width))

# this is to select a difficulty level within the game and will speed up the game play appropriately as well as speed up the user's movements if level 10 is selected
difficulty = input("""Enter a level you would like to play, ranging from 1 - 10,
10 can be discomforting but you will receive a slight speed bonus,
anything under 3 is for newbies: """)

# this while loop means the player cannot enter a false level number, but has to be from 1 - 10
while difficulty != "10" and difficulty != "9" and difficulty != "8" and difficulty != "7" and difficulty != "6" and difficulty != "5" and difficulty != "4" and difficulty != "3" and difficulty != "2" and difficulty != "1":
    difficulty = input("Enter a level you would like to play, ranging from 1 - 10: ")

# this determines the starting position of the player with the XPosition being set but the YPosition being random without the possibility of the player being outside the screen
playerXPosition = 100
playerYPosition = random.randint(0, screen_height - player_height)

# this determines the enemies starting positions are off the screen as well as ensures they are all at different XPositions so that they do not overlap with each other
# the enemies YPositions are all random but without allowing them to be out of the screen
enemy1XPosition = screen_width
enemy1YPosition = random.randint(0, screen_height - enemy1_height)
enemy2XPosition = screen_width + (2 * enemy1_width)
enemy2YPosition = random.randint(0, screen_height - enemy2_height)
enemy3XPosition = screen_width + (4 * enemy2_width)
enemy3YPosition = random.randint(0, screen_height - enemy3_height)

# this determines the prize's position but ensures that it only is available after the enemies have moved onto the screen
prizeXPosition = screen_width + (7 * enemy3_width)
prizeYPosition = random.randint(0, screen_height - prize_height)

# the boolean value here ensures that while the keys are not being pressed, the value is false
keyUp = False
keyDown = False
keyRight = False
keyLeft = False

# this is the game loop in order to continue running the games' logic over and over until something occurs
# this continuously refreshes the game screen to represent the real time game play
# in terms of this game, it will keep looping until the pygame has a quit function reached, which would signify the end of the game
# boolean value 1 equals true so this will continuously run until quit
while 1:

    # this clears the screen
    screen.fill(0)

    # this draws the position of the player, enemies and prizes specified position
    screen.blit(player, (playerXPosition, playerYPosition))
    screen.blit(enemy1, (enemy1XPosition, enemy1YPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))

    # this updates the screen
    pygame.display.flip()

    # this for loop is to run through the events within the pygame
    for event in pygame.event.get():

        # this event checks if the player quits the pygame, in turn it exits the program
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        # this event checks if the player presses a down key
        if event.type == pygame.KEYDOWN:

            # it further tests if the key pressed is the one the player wants
            # pygame.K_(DIRECTION) represents the keyboard constant
            if event.key == pygame.K_UP:
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_RIGHT:
                keyRight = True
            if event.key == pygame.K_LEFT:
                keyLeft = True

        # this event checks if the key is up (i.e. not pressed by the player)
        if event.type == pygame.KEYUP:

            # tests if the key released is the one the player wants
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_RIGHT:
                keyRight = False
            if event.key == pygame.K_LEFT:
                keyLeft = False

    # this determines if the player selected the highest level
    if difficulty == "10":

        # the following if functions move the players positions when the appropriate key is pressed
        # the 2nd if functions of each mean the directions being pressed will not allow the player to move off the screen
        # because of the hard level being selected, the player has the added speed movement
        if keyUp == True:
            if playerYPosition > 0:
                playerYPosition -= 1.5

        if keyDown == True:
            if playerYPosition < (screen_height - player_height):
                playerYPosition += 1.5

        if keyRight == True:
            if playerXPosition < (screen_width - player_width):
                playerXPosition += 1.5

        if keyLeft == True:
            if playerXPosition > 0:
                playerXPosition -= 1.5


    # this is if the player does not select level 10    
    elif difficulty != "10":
        # the players movement is at normal speed
        # the 2nd if functions of each mean the directions being pressed will not allow the player to move off the screen
        if keyUp == True:
            if playerYPosition > 0:
                playerYPosition -= 1

        if keyDown == True:
            if playerYPosition < (screen_height - player_height):
                playerYPosition += 1

        if keyRight == True:
            if playerXPosition < (screen_width - player_width):
                playerXPosition += 1

        if keyLeft == True:
            if playerXPosition > 0:
                playerXPosition -= 1


    # this creates a box around the player in order to check for collision with the enemy or the prize
    # it checks if the boxes intersect
    playerBox = pygame.Rect(player.get_rect())

    # this updates the playerBox to the players position and creates the size of the box with width and height
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    playerBox.height = player_height
    playerBox.width = player_width

    # this creates a box around the enemies' in order to check for collision with the enemy or the prize
    # it checks if the boxes intersect
    enemy1Box = pygame.Rect(player.get_rect())

    # this updates the enemyBox's positions and creates the size of the box with width and height
    enemy1Box.top = enemy1YPosition
    enemy1Box.left = enemy1XPosition
    enemy1Box.height = enemy1_height
    enemy1Box.width = enemy1_width

    enemy2Box = pygame.Rect(player.get_rect())
    
    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition
    enemy2Box.height = enemy2_height
    enemy2Box.width = enemy2_width

    enemy3Box = pygame.Rect(player.get_rect())
    
    enemy3Box.top = enemy3YPosition
    enemy3Box.left = enemy3XPosition
    enemy3Box.height = enemy3_height
    enemy3Box.width = enemy3_width

    # this creates a box around the prize in order to check for collision with the enemy or the prize
    # it checks if the boxes intersect
    prizeBox = pygame.Rect(player.get_rect())

    # this updates the prizeBox to the prize's position and creates the size of the box with width and height
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition
    prizeBox.height = prize_height
    prizeBox.width = prize_width

    # this tests for the collision of the playerBox with the enemy boxes and prints out the appropriate message and quits the game and closes the window
    if playerBox.colliderect(enemy1Box):
        print("You lose!")
        pygame.quit()
        exit(0)

    if playerBox.colliderect(enemy2Box):
        print("You lose!")
        pygame.quit()
        exit(0)

    if playerBox.colliderect(enemy3Box):
        print("You lose!")
        pygame.quit()
        exit(0)


    # this test for the collision with the playerBox with the prizeBox and prints out the winning message and quits the game and closes the window
    if playerBox.colliderect(prizeBox):
        print("You win!")
        pygame.quit()
        exit(0)

    # this tests to see if the playerBox did not collide with the enemies but also missed the prize and means he therefore did not win the game and prints out the appropriate message and exits the game and exits the window
    if enemy1XPosition < (0 - enemy1_width) and enemy2XPosition < (0 - enemy2_width) and enemy3XPosition < (0 - enemy3_width) and prizeXPosition < (0 - prize_width):
        print("You almost won, but you missed the prize!")
        pygame.quit()
        exit(0)

    # the following if statements are to determine how fast the enemies and the prize approach the player, determined by the input of level
    if difficulty == "10":
        enemy1XPosition -= 5
        enemy2XPosition -= 5
        enemy3XPosition -= 5
        prizeXPosition -= 5

    if difficulty == "9":
        enemy1XPosition -= 4.5
        enemy2XPosition -= 4.5
        enemy3XPosition -= 4.5
        prizeXPosition -= 4.5

    if difficulty == "8":
        enemy1XPosition -= 4
        enemy2XPosition -= 4
        enemy3XPosition -= 4
        prizeXPosition -= 4

    if difficulty == "7":
        enemy1XPosition -= 3.5
        enemy2XPosition -= 3.5
        enemy3XPosition -= 3.5
        prizeXPosition -= 3.5

    if difficulty == "6":
        enemy1XPosition -= 3
        enemy2XPosition -= 3
        enemy3XPosition -= 3
        prizeXPosition -= 3

    if difficulty == "5":
        enemy1XPosition -= 2.5
        enemy2XPosition -= 2.5
        enemy3XPosition -= 2.5
        prizeXPosition -= 2.5

    if difficulty == "4":
        enemy1XPosition -= 2
        enemy2XPosition -= 2
        enemy3XPosition -= 2
        prizeXPosition -= 2

    if difficulty == "3":
        enemy1XPosition -= 1.5
        enemy2XPosition -= 1.5
        enemy3XPosition -= 1.5
        prizeXPosition -= 1.5

    if difficulty == "2":
        enemy1XPosition -= 1
        enemy2XPosition -= 1
        enemy3XPosition -= 1
        prizeXPosition -= 1

    if difficulty == "1":
        enemy1XPosition -= 0.5
        enemy2XPosition -= 0.5
        enemy3XPosition -= 0.5
        prizeXPosition -= 0.5



















