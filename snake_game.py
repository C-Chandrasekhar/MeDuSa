
import pygame
import time
import random
 
#initialising pygame
pygame.init()

#resolution of display
display_width=600
display_height=400

gameDisplay = pygame.display.set_mode((display_width,display_height))
#setting caption
pygame.display.set_caption('MeDuSa')

#to set colours to blocks
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0 , 150 , 0)

##speed controlers

block_size=10       #size of each block            
#frames per second while loop runs 10^9 times per second so u will not be able to visualize if fps is not set to some value
fps=10  
#initilising pygame clock inorder to use fps
clock = pygame.time.Clock()


#To print the snake
def snake(block_size , snakeList):
	for XnY in snakeList:
		pygame.draw.rect(gameDisplay , green , [XnY[0] , XnY[1],block_size , block_size])

#To display some text on screen
font = pygame.font.SysFont(None , 25)
def message_to_screen(msg , color):
	textSurface = font.render(msg , True , color)
	textRect= textSurface.get_rect()
	textRect.center = display_width/2 , display_height/2
	gameDisplay.blit(textSurface , textRect)

#loop where game runs 
def gameloop():

	gameExit = False          #True to exit the game
	gameOver = False          #True if game is over
	head_x=display_width/2
	head_y=display_height/2

	head_x_change=0
	head_y_change=0
    #initially length of the snake is empty
	snakeList=[]
	snakeLength=1
	#coordinates of apple (food)
	randAppleX= round(random.randrange(0,display_width-block_size)/ 10.0)*10.0
	randAppleY= round(random.randrange(0,display_height-block_size)/10.0)*10.0

	while not gameExit:

		while gameOver == True:
			gameDisplay.fill(white)
			#message_to_screen("your score is :"+str(snakeLength-1), green)
			message_to_screen("your score is : "+str(snakeLength-1) +'  Game Over, press c to replay and q to exit', red)
			pygame.display.update()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					gameExit=True
					gameOver=False
				if event.type== pygame.KEYDOWN:
					if event.key== pygame.K_q:
						gameExit=True
						gameOver=False
					if event.key==pygame.K_c:
						gameloop()

		#for handling the events
		for event in pygame.event.get():
			#print(event)
			if event.type==pygame.QUIT:
				gameExit=True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					head_x_change= -block_size
					head_y_change=0
				if event.key == pygame.K_RIGHT:
					head_x_change= block_size
					head_y_change=0
				if event.key == pygame.K_DOWN:
					head_y_change= block_size
					head_x_change= 0
				if event.key == pygame.K_UP:
					head_y_change= -block_size
					head_x_change= 0

		#to get borders unbunded
		if head_x >display_width:
			head_x=0
		if head_x <0:
			head_x=display_width
		if head_y >display_height:
			head_y=0
		if head_y <0:
			head_y=display_height


		#movement of snakee head
		head_x+=head_x_change
		head_y+=head_y_change

		gameDisplay.fill(white)
		#to display the food
		pygame.draw.rect(gameDisplay , red , [randAppleX , randAppleY , block_size , block_size])
		
		#defining the snake
		snakeHead=[]
		snakeHead.append(head_x)
		snakeHead.append(head_y)
		snakeList.append(snakeHead)
		
		#delete the extra nodes
		if len(snakeList) > snakeLength:
			del snakeList[0]

		#gameOver if snake head touches itself
		for position in snakeList[:-1]:
			if snakeHead== position:
				gameOver=True

		#constructing the snake
		snake(block_size , snakeList)
		#updating the display without this everything we had done will not be seen
		pygame.display.update()

		#if snake eats apple then produce another random apple ans increase its length by 1
		if head_x== randAppleX and head_y == randAppleY:
			randAppleX= round(random.randrange(0,display_width-block_size)/ 10.0)*10.0
			randAppleY= round(random.randrange(0,display_height-block_size)/10.0)*10.0
			snakeLength+=1

		#for updating the score every time
		pygame.display.set_caption("Snake-Game | Score :"+ str(snakeLength -1))
		clock.tick(fps) # with the help of fps and block_size we can alter speed of motion and smoothen the game 

	#to quit the pygame
	pygame.quit()
	#to quit the code
	quit()

#to run game for the first time
gameloop()