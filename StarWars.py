"""
Creator: Amit Jha(devbihari)
"""

import pygame 
import random

pygame.init() #initiating pygame module

white = [255, 255, 255] #defining colours
red = [255, 0, 0]
blue = [0, 105, 55]
black = [0, 0,0]
orange = [255, 115, 0]
gray = [128, 128, 128]
dark_gray = [110, 110, 110]
dark_red = [155, 0, 0]

display_width = 800 #width of the game's window
display_height = 600 #height of the game's window

statusBar_pos_y = 570 #Y-position of the status bar at the bottom of the screen
statusBar_pos_x = 0 #X-position of the status bar

pygame.display.set_caption("StarWars") #name of the game window
gameDisplay = pygame.display.set_mode((display_width, display_height)) #display surface
gameDisplay.fill(black) #fill the screen with black
pygame.display.update() #update the display to show changes

img = pygame.image.load("spaceship.png") #load the space ship
#enemyShip_one = pygame.image.load("enemyship.png") #load the larger enemy ship
enemyShip_two = pygame.image.load("spaceship2.png") #load the smaller enemy ship
explosion = pygame.image.load("explosion.png") #load the explosion image
noShip_one = pygame.image.load("noship1.png")
#noShip_two = pygame.image.load("noship2.png")
block_size = 3 #define the star size
FPS = 60 #frames per second

posterShip = pygame.transform.rotate(noShip_one, 245)

clock = pygame.time.Clock() #time attribute to update the display certain times a second


#fonts
smallfont = pygame.font.SysFont("Courier 10 Pitch", 25)
medfont = pygame.font.SysFont("Courier 10 Pitch", 30)
largefont = pygame.font.SysFont("Courier 10 Pitch", 100)

#functions
def button_to_screen(color, hover_color, buttonx, buttony, button_width, button_height, action = None):
	pygame.draw.rect(gameDisplay, color, (buttonx, buttony, button_width, button_height))
	cur = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	if buttonx + button_width > cur[0] > buttonx and buttony + button_height > cur[1] > buttony:
		pygame.draw.rect(gameDisplay, hover_color, (buttonx, buttony, button_width, button_height))
		if click[0] == 1:
			if action == "Play":
				gameLoop()
			elif action == "Quit":
				pygame.quit()
				quit()
			elif action == "Resume":
				 print("Resume")

def text_objects(text, color, size): #function to decide the font size
	if size == "small":
		textSurface = smallfont.render(text, True, color) #rendering font in the back ground
	elif size == "medium":
		textSurface = medfont.render(text, True, color)
	elif size == "large":
		textSurface = largefont.render(text, True, color)
	return textSurface, textSurface.get_rect() #returns the text and the rectangular surface on which it prints

def score_on_screen(msg, color, x_displace = 0,size = "small"): #prints score on the screen
	textSurf, textRect = text_objects(msg, color, size) #textSurf is the text and textRect is the rect. slab
	textRect.center = (statusBar_pos_x) + x_displace, (statusBar_pos_y) + 15 #center the rect. slab at the given co-ordinate
	gameDisplay.blit(textSurf, textRect) #put the text on the screen

def enemyShips(shipRand_pos_x, enemyShip_pos_y, size = "small"): #display the enemy ship on the screen
	if size == "small":
		gameDisplay.blit(enemyShip_two, (shipRand_pos_x, enemyShip_pos_y))

def movingStar(lead_y, block_size): #moving star system
	def stars(lead_y, block_size): #daughter function to print stars on the screen
		for i in range(0, 3000):
			if i % 20 == 0:
				pygame.draw.rect(gameDisplay, white, [i, lead_y, block_size, block_size])
	for i in range(0, 1000):
		if i % 30 == 0 and i < 900:
			stars(lead_y-i, block_size)
def statusBar(statusBar_pos_x, statusBar_pos_y):
	pygame.draw.rect(gameDisplay, gray, [statusBar_pos_x, statusBar_pos_y, display_width, 30]) #the main status bar
	pygame.draw.rect(gameDisplay, white, [statusBar_pos_x + 250, statusBar_pos_y, 3, 30]) #the first white line
	pygame.draw.rect(gameDisplay, white, [statusBar_pos_x + 500, statusBar_pos_y, 3, 30]) #the second white line
def life(lifeLeft, statusBar_pos_x, statusBar_pos_y): #life bar
	if lifeLeft > 80: #if life greater than 80
		pygame.draw.rect(gameDisplay, blue, [statusBar_pos_x + 260, statusBar_pos_y + 5, lifeLeft, 20])
	elif lifeLeft <= 80: #if life smaller than 80
		pygame.draw.rect(gameDisplay, red, [statusBar_pos_x + 260, statusBar_pos_y + 5, lifeLeft, 20])

def spaceShip(spaceShip_pos_x, spaceShip_pos_y, display_height):
	gameDisplay.blit(img, (spaceShip_pos_x, spaceShip_pos_y))

def bullet(color, bullet_x, bullet_y):
	pygame.draw.rect(gameDisplay, color, [bullet_x, bullet_y, 20, 30])

def enemyBullet(color, enemyBullet_x, enemyBullet_y):
	pygame.draw.rect(gameDisplay, color, [enemyBullet_x, enemyBullet_y, 5, 30])
	pygame.draw.rect(gameDisplay, color, [enemyBullet_x, enemyBullet_y, 5, 30])

def text_to_button(msg, color, x_pos, y_pos):
	message_to_screen(msg, color, x_pos, y_pos, size = "small")

def game_intro():
	intro = True
	while intro:
		gameDisplay.fill(black)
		gameDisplay.blit(noShip_one, (display_width/2 - 100, display_height/2 - 100))
		message_to_screen("Welcome to Starwars", white, display_width/2, display_height/2 - 150, "large")
		button_to_screen(dark_gray, dark_gray, buttonx = display_width/2 - 130, buttony = display_height/2 + 180, button_width = 100, button_height = 50) 
		button_to_screen(gray, dark_gray, buttonx = display_width/2 - 130 + 5, buttony = display_height/2 + 180 + 5, button_width = 100 - 10, button_height = 50 - 10, action = "Play")
		button_to_screen(dark_red, dark_red, buttonx = display_width/2 - 130 + 150, buttony = display_height/2 + 180 , button_width = 100, button_height = 50) 
		button_to_screen(red, dark_red, buttonx = display_width/2 - 130 + 150 + 5, buttony = display_height/2 + 180 + 5 , button_width = 100 - 10, button_height = 50 - 10, action = "Quit") 
		
		text_to_button("Play", white, x_pos = display_width/2 - 130 + 40 + 5, y_pos = display_height/2 + 180 + 25)
		text_to_button("Quit", white, x_pos = display_width/2 - 130 + 150 + 40 + 5, y_pos = display_height/2 + 180 + 25)
		
		pygame.display.update()
		clock.tick(15)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

def message_to_screen(msg, color, x_pos, y_pos, size = "small"):
	textSurf, textRect = text_objects(msg, color, size)
	textRect.center = (x_pos), (y_pos)
	gameDisplay.blit(textSurf, textRect)

def pause():
	paused = True
	
	while paused:
		message_to_screen("Game Paused", white, display_width/2, display_height/2, "large")
		button_to_screen(dark_gray, dark_gray, buttonx = display_width/2 - 130, buttony = display_height/2 + 100, button_width = 100, button_height = 50) 
		button_to_screen(gray, dark_gray, buttonx = display_width/2 - 130 + 5, buttony = display_height/2 + 100 + 5, button_width = 100 - 10, button_height = 50 - 10, action = "Resume")
		button_to_screen(dark_red, dark_red, buttonx = display_width/2 - 130 + 150, buttony = display_height/2 + 100 , button_width = 100, button_height = 50) 
		button_to_screen(red, dark_red, buttonx = display_width/2 - 130 + 150 + 5, buttony = display_height/2 + 100 + 5 , button_width = 100 - 10, button_height = 50 - 10, action = "Quit") 
		
		text_to_button("Resume", white, x_pos = display_width/2 - 130 + 40 + 5, y_pos = display_height/2 + 100 + 25)
		text_to_button("Quit", white, x_pos = display_width/2 - 130 + 150 + 40 + 5, y_pos = display_height/2 + 100 + 25)
		pygame.display.update()
		clock.tick(15)


def gameLoop():
	gameExit = False
	gameOver = False
	lifeLeft = 230
	global explosion
	point = 0
	shipRand_pos_x = round((random.randrange(100, display_width - 100)))#/ 10.0)) * 10.0
	enemyShip_pos_y = -100
	enemyShip_pos_y_change = 0
	spaceShip_pos_x = 256
	spaceShip_pos_y = 395
	lead_x_change = 0
	lead_y_change = 0
	lead_x = display_width
	lead_y = display_height
	bullet_x = 378
	bullet_y = 420
	bullet_x_change = 0
	bullet_y_change = 0
	enemyBullet_x = 0
	enemyBullet_y = -40
	enemyBullet_y_change = 0
	speed = 7
	statusBar_pos_y = 570
	statusBar_pos_x = 0
	score = 0
	while not gameExit:
		enemyShip_pos_y_change = speed #speed of the ENEMY SHIP
		enemyBullet_y_change = speed #speed of the ENEMY BULLET
		lead_y_change = 3 #speed of the players SHIP
		
		#when the game is paused
		while gameOver == True:
			message_to_screen("Game Over", white, x_pos = display_width/2,\
			y_pos = display_height/2 - 100, size = "large")
			button_to_screen(dark_gray, dark_gray, buttonx = display_width/2 - 130, buttony = display_height/2 + 100, button_width = 100, button_height = 50) 
			button_to_screen(gray, dark_gray, buttonx = display_width/2 - 130 + 5, buttony = display_height/2 + 100 + 5, button_width = 100 - 10, button_height = 50 - 10, action = "Play")
			button_to_screen(dark_red, dark_red, buttonx = display_width/2 - 130 + 150, buttony = display_height/2 + 100 , button_width = 100, button_height = 50) 
			button_to_screen(red, dark_red, buttonx = display_width/2 - 130 + 150 + 5, buttony = display_height/2 + 100 + 5 , button_width = 100 - 10, button_height = 50 - 10, action = "Quit") 
			
			text_to_button("Restart", white, x_pos = display_width/2 - 130 + 40 + 5, y_pos = display_height/2 + 100 + 25)
			text_to_button("Quit", white, x_pos = display_width/2 - 130 + 150 + 40 + 5, y_pos = display_height/2 + 100 + 25)
			pygame.display.update()
			score = 0
			lead_x_change = 0
			bullet_x_change = 0
			enemyBullet_pos_y = -40
			enemyBullet_pos_y_change = 0
			enemyShip_pos_y = -100
			enemyShip_pos_y_change = 0
			#functions of different keys
			for event in pygame.event.get(): #looking for events happening on the game window
				if event.type == pygame.QUIT: #if the X button on the top is pressed
					gameOver = False 
					gameExit = True
				elif event.type == pygame.KEYDOWN: #if any key on the keyboard is pressed
					if event.key == pygame.K_RETURN: #if enter is pressed
							gameOver = False
							lifeLeft = 230 #bring back the life
					elif event.key == pygame.K_q: #if q is pressed
							gameOver = False
							gameExit = True
							
		#look for events on the game window
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT: #if X is pressed
				gameExit = True
			elif event.type == pygame.KEYDOWN: #if key is pressed
				if event.key == pygame.K_LEFT: #if left arrow key is pressed
					lead_x_change = -speed
					bullet_x_change = -speed
				elif event.key == pygame.K_RIGHT:#if right arrow key is pressed
					lead_x_change = speed
					bullet_x_change = speed
				elif event.key == pygame.K_SPACE: #if space is pressed
					bullet_y_change = -10 #shoot
				elif event.key == pygame.K_p:
					paused = True
					pause()
	
	
		bullet_x += bullet_x_change
		bullet_y += bullet_y_change
		spaceShip_pos_x += lead_x_change
		lead_y += lead_y_change
		enemyShip_pos_y += enemyShip_pos_y_change
		enemyBullet_y += enemyBullet_y_change
	
		#if the player's ship hits the edge
		if spaceShip_pos_x < -30 or spaceShip_pos_x > display_width - 230:
			lead_x_change = 0
			bullet_x_change = 0
		
		#if bullet goes out of window ;)
		if bullet_y <= 0:
			bullet_y = 420
			bullet_y_change = 0
			bullet_x = spaceShip_pos_x + 122
			if lead_x_change == -speed:
				bullet_x_change = -speed
			elif lead_x_change == speed:
				bullet_x_change = speed
	
		#keep the bullet on the straight path even though the player's ship changes the position
		if bullet_y <= 400:
			if lead_x_change == -speed:
				bullet_x_change = 0
			elif lead_x_change == speed:
				bullet_x_change = 0
	
		#to keep the star in loop
		if lead_y > 900:
			lead_y = 600
	
		#enemy ship shoots
		if enemyShip_pos_y >= 10 and enemyShip_pos_y < display_height:
			enemyBullet_y += speed - 3
	
		#enemy's bullet hits the player's ship
		if enemyBullet_y >= spaceShip_pos_y and enemyBullet_y < spaceShip_pos_y + 20:
			if shipRand_pos_x > spaceShip_pos_x and shipRand_pos_x < spaceShip_pos_x + 230:
				lifeLeft -= 15
				score -= 5
	
		#enemy's ship is hit by the player's bullet
		if bullet_y <= enemyShip_pos_y + 20:
			if enemyShip_pos_y < display_height - 100:
				if (bullet_x > shipRand_pos_x and bullet_x + 30 < shipRand_pos_x + 140):
					gameDisplay.blit(explosion, (shipRand_pos_x- 100, enemyShip_pos_y - 130))
					pygame.display.update()
					shipRand_pos_x = round((random.randrange(100, 600)))#/ 10.0)) * 10.0
					enemyBullet_y = -110
					enemyShip_pos_y = -170
					point += 50
					bullet_y = 420
					bullet_y_change = 0
					bullet_x = spaceShip_pos_x + 122
					score += 20
					if lifeLeft <= 210:
						lifeLeft += 10
					if lead_x_change == -speed:
						bullet_x_change = -speed
					elif lead_x_change == speed:
						bullet_x_change = speed
	
		#enemy ship passes without being destroyed 
		if enemyShip_pos_y >= display_height-50:
			lifeLeft -= 30
			enemyShip_pos_y = -100
			enemyBullet_y = -40
			shipRand_pos_x = round((random.randrange(100, 600)))#/ 10.0)) * 10.0
			score -= 10
	
		#if the player's ship and enemy ship collide
		if enemyShip_pos_y >= spaceShip_pos_y:
			if shipRand_pos_x > spaceShip_pos_x and shipRand_pos_x + 80 < spaceShip_pos_x + 210:
				gameDisplay.blit(explosion, (spaceShip_pos_x - 30, spaceShip_pos_y - 20))
				pygame.display.update()
				gameOver = True
				enemyShip_pos_y = -100
				enemyBullet_y = -40
		
		#life goes below benchmark
		if lifeLeft <= 20:
			gameOver = True
		
		totalScore = str(score) #convert the integer score into string so as to be rendered 
		
		#to decide from where the enemy is coming
		if shipRand_pos_x + 80 <= statusBar_pos_x + 250:
			pygame.draw.rect(gameDisplay, red, [statusBar_pos_x, 0, 250, 5])
			pygame.display.update()
		elif shipRand_pos_x + 80 > statusBar_pos_x + 250 and shipRand_pos_x + 80 <= statusBar_pos_x + 500:
			pygame.draw.rect(gameDisplay, red, [statusBar_pos_x + 250, 0, 250, 5])
			pygame.display.update()
		elif shipRand_pos_x + 80 > statusBar_pos_x + 500:
			pygame.draw.rect(gameDisplay, red, [statusBar_pos_x + 500, 0, 300, 5])
			pygame.display.update()
	
		#render everything on the screen 
		gameDisplay.fill(black)
		movingStar(lead_y, block_size)
		bullet(orange, bullet_x, bullet_y)
		enemyBullet(orange, shipRand_pos_x + 90, enemyBullet_y)
		enemyBullet(orange, shipRand_pos_x + 25, enemyBullet_y)
		spaceShip(spaceShip_pos_x, spaceShip_pos_y, display_height)
		enemyShips(shipRand_pos_x, enemyShip_pos_y, size = "small")
		statusBar(statusBar_pos_x, statusBar_pos_y)
		life(lifeLeft, statusBar_pos_x, statusBar_pos_y)
		score_on_screen("Total score: ", white, 70, "medium")
		score_on_screen(totalScore, white, 170,"medium")
		pygame.display.update()
		
		clock.tick(FPS)
	pygame.quit()
	quit()


game_intro()
gameLoop()
