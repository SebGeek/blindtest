import pygame
import glob

blind_test_dir = "music/noel/"

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
    pygame.mixer.music.pause()

def continue_music():
    pygame.mixer.music.unpause()

def set_volume(volume):
    ''' Set the volume of the music playback.
    The volume argument is a float between 0.0 and 1.0 that sets volume.
    '''
    print(f"set volume {volume}%")
    pygame.mixer.music.set_volume(volume / 100)


if __name__ == '__main__':

    pygame.init()

    pygame.mixer.init()
    file_list = glob.glob(blind_test_dir + "*.mp3")

    music_is_playing = False

    # Set the width and height of the screen (width, height).
    screen = pygame.display.set_mode((500, 700))

    pygame.display.set_caption("My Game")


    width = screen.get_width()
    height = screen.get_height()

    smallfont = pygame.font.SysFont('Corbel', 35)
    text = smallfont.render('continue', True, color)

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates.
    clock = pygame.time.Clock()

    # Initialize the joysticks
    pygame.joystick.init()

    # Get ready to print
    textPrint = TextPrint()

    # Get count of joysticks.
    joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

    print(f"Number of teams/joysticks: {len(joysticks)}")

    # For each joystick:
    for joystick in joysticks:
        joystick.init()

    team_pressed_a_button = ""
    red_score = 0
    blue_score = 0

    button_pos_X = 10  # width / 2
    button_pos_Y = 200  # height / 2
    button_width = 140
    button_height = 40

    # -------- Main Program Loop -----------
    while not done:

        mouse = pygame.mouse.get_pos()

        #
        # EVENT PROCESSING STEP
        #
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close in window bar
                done = True  # Flag that we are done, so we exit this loop

            elif event.type == pygame.JOYBUTTONDOWN:
                team_pressed_a_button = "blue" if event.__dict__['joy'] == 0 else "red"
                stop_music()
                music_is_playing = False

            # checks if a mouse is clicked
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # if the mouse is clicked on the button the game is terminated
                if button_pos_X <= mouse[0] <= button_pos_X + button_width and button_pos_Y <= mouse[1] <= button_pos_Y + button_height:
                    if not music_is_playing:
                        play_music(file_list[0])
                        music_is_playing = True
                    else:
                        continue_music()

        #
        # DRAWING STEP
        #
        # First, clear the screen to white
        screen.fill(WHITE)
        textPrint.reset()


        textPrint.tprint(screen, f"Last team having pressed a button is {team_pressed_a_button}")
        textPrint.tprint(screen, "")

        textPrint.indent()
        textPrint.tprint(screen, f"Score team BLUE: {blue_score}")
        textPrint.tprint(screen, f"Score team   RED: {red_score}")


        # if mouse is hovered on a button, it changes to lighter shade
        if button_pos_X <= mouse[0] <= button_pos_X + button_width and button_pos_Y <= mouse[1] <= button_pos_Y + button_height:
            color = color_light
        else:
            color = color_dark
        pygame.draw.rect(screen, color, [button_pos_X, button_pos_Y, button_width, button_height])
        # superimposing the text onto our button
        screen.blit(text, (button_pos_X, button_pos_Y))

        #
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        #

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # Limit to 20 frames per second
        clock.tick(20)

    stop_music()

    # Close the window and quit.
    pygame.quit()