import pygame


# Define some colors.
BLACK = pygame.Color('black')
WHITE = pygame.Color('white')

# white color
color = (255, 255, 255)
# light shade of the button
color_light = (170, 170, 170)
# dark shade of the button
color_dark = (100, 100, 100)


# This is a simple class that will help us print to the screen.
# It has nothing to do with the joysticks, just outputting the
# information.
class TextPrint(object):
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def tprint(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, (self.x, self.y))
        self.y += self.line_height

    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15

    def indent(self):
        self.x += 10

    def unindent(self):
        self.x -= 10



def play_music(filepath):
    pygame.mixer.music.load(filepath)
    print("playing", filepath)
    pygame.mixer.music.play()

def stop_music():
    print("stop music")
    pygame.mixer.music.pause()

def continue_music():
    print("continue music")
    pygame.mixer.music.unpause()

def set_volume(volume):
    ''' Set the volume of the music playback.
    The volume argument is a float between 0.0 and 1.0 that sets volume.
    '''
    print(f"set volume {volume}%")
    pygame.mixer.music.set_volume(volume / 100)


if __name__ == '__main__':

    pygame.init()

    print("init pygame sound mixer")
    pygame.mixer.init()

    play_music("music/Musique_Noel.mp3")


    # Set the width and height of the screen (width, height).
    screen = pygame.display.set_mode((500, 700))

    pygame.display.set_caption("My Game")

    # stores the width of the
    # screen into a variable
    width = screen.get_width()
    # stores the height of the
    # screen into a variable
    height = screen.get_height()
    # defining a font
    smallfont = pygame.font.SysFont('Corbel', 35)
    # rendering a text written in
    # this font
    text = smallfont.render('quit', True, color)

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates.
    clock = pygame.time.Clock()

    # Initialize the joysticks.
    pygame.joystick.init()

    # Get ready to print.
    textPrint = TextPrint()

    # Get count of joysticks.
    joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

    # For each joystick:
    for joystick in joysticks:
        joystick.init()


    # -------- Main Program Loop -----------
    while not done:

        # stores the (x,y) coordinates into
        # the variable as a tuple
        mouse = pygame.mouse.get_pos()

        #
        # EVENT PROCESSING STEP
        #
        # Possible joystick actions: JOYAXISMOTION, JOYBALLMOTION, JOYBUTTONDOWN,
        # JOYBUTTONUP, JOYHATMOTION
        for event in pygame.event.get():  # User did something.
            if event.type == pygame.QUIT:  # If user clicked close.
                done = True  # Flag that we are done, so we exit this loop.
            elif event.type == pygame.JOYBUTTONDOWN:
                print(event)
            # checks if a mouse is clicked
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # if the mouse is clicked on the button the game is terminated
                if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
                    done = True  # Flag that we are done, so we exit this loop.


        #
        # DRAWING STEP
        #
        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(WHITE)
        textPrint.reset()

        textPrint.tprint(screen, "Number of joysticks: {}".format(len(joysticks)))
        textPrint.indent()

        # # For each joystick:
        # for joy_num in range(joystick_count):
        #     joystick = pygame.joystick.Joystick(joy_num)
        #     joystick.init()
        #
        #     textPrint.tprint(screen, "Joystick {}".format(joy_num))
        #     textPrint.indent()
        #
        #     # Get the name from the OS for the controller/joystick.
        #     name = joystick.get_name()
        #     textPrint.tprint(screen, "Joystick name: {}".format(name))
        #
        #     buttons = joystick.get_numbuttons()
        #     textPrint.tprint(screen, "Number of buttons: {}".format(buttons))
        #     textPrint.indent()
        #
        #     for i in range(buttons):
        #         button = joystick.get_button(i)
        #         textPrint.tprint(screen,
        #                          "Button {:>2} value: {}".format(i, button))
        #     textPrint.unindent()

        red = (200, 0, 0)
        circleX = 100
        circleY = 100
        radius = 10
        pygame.draw.circle(screen, red, (circleX, circleY), radius)  # DRAW CIRCLE



        # if mouse is hovered on a button it
        # changes to lighter shade
        if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
            pygame.draw.rect(screen, color_light, [width / 2, height / 2, 140, 40])

        else:
            pygame.draw.rect(screen, color_dark, [width / 2, height / 2, 140, 40])

        # superimposing the text onto our button
        screen.blit(text, (width / 2 + 50, height / 2))

        #
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        #

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # Limit to 20 frames per second.
        clock.tick(20)

    stop_music()

    # Close the window and quit.
    # If you forget this line, the program will 'hang' on exit if running from IDLE.
    pygame.quit()