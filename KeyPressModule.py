import pygame
# defined the RGB color code for the background
background_colour = (139, 0, 0)
# defined the size of the screen (width, height)
screen = pygame.display.set_mode((600, 300))

# set caption
pygame.display.set_caption('DroneControl')

# fill the screen with the above-defined background color
screen.fill(background_colour)


# update the display using flip
pygame.display.flip()


# keep the game looping
running = True

def getKey(keyName):
	ans = False
	for eve in pygame.event.get():
		pass
	keyInput = pygame.key.get_pressed()
	myKey = getattr(pygame, 'K_{}'.format(keyName))
	if keyInput[myKey]:
		ans = True
	pygame.display.update()
	return ans
def main():
	if getKey("LEFT"):
		 print ("Left Key Pressed")
	if getKey("RIGHT"):
		 print ("Right Key Pressed")

if __name__ == '__main__':
	while True:
		main()



