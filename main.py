import pygame
import glob

blind_test_dir = "music/noel/"

# Define some colors.
BLACK = pygame.Color('black')
WHITE = pygame.Color('white')
BLUE = pygame.Color('blue')
RED = pygame.Color('red')

# white color
color = (255, 255, 255)
# light shade of the button
color_light = (170, 170, 170)
# dark shade of the button
color_dark = (100, 100, 100)


# This is a simple class that will help us print to the screen
class TextPrint(object):
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 50)

    def tprint(self, screen, textString, color=BLACK):
        textBitmap = self.font.render(textString, True, color)
        screen.blit(textBitmap, (self.x, self.y))
        self.y += self.line_height

    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 50

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


def draw_button(screen, text, button_pos_X, button_pos_Y, button_width, button_height):
    # if mouse is hovered on a button, it changes to lighter shade
    if button_pos_X <= mouse[0] <= button_pos_X + button_width and button_pos_Y <= mouse[1] <= button_pos_Y + button_height:
        color = color_light
    else:
        color = color_dark
    pygame.draw.rect(screen, color, [button_pos_X, button_pos_Y, button_width, button_height])
    # superimposing the text onto our button
    screen.blit(text, (button_pos_X, button_pos_Y))

def new_music(music_number_to_play):
    play_music(file_list[music_number_to_play])
    music_number_to_play += 1
    if music_number_to_play == len(file_list):
        music_number_to_play = 0
        print("All musics have been played !")
    return music_number_to_play


if __name__ == '__main__':

    pygame.init()

    pygame.mixer.init()
    file_list = glob.glob(blind_test_dir + "*.mp3")

    music_is_playing = False

    # Set the width and height of the screen (width, height).
    screen = pygame.display.set_mode((1200, 700))

    pygame.display.set_caption("Blind Test")


    width = screen.get_width()
    height = screen.get_height()

    smallfont = pygame.font.SysFont('Corbel', 35)
    text_continue = smallfont.render('Start / continue playing the music', True, color)
    text_bad = smallfont.render('Bad answer', True, color)
    text_good = smallfont.render('Good answer', True, color)

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
    team_color = BLACK
    red_score = 0
    blue_score = 0
    music_number_to_play = 0

    button_continue_pos_X = 10
    button_continue_pos_Y = 300
    button_continue_width = 500
    button_continue_height = 40

    button_bad_pos_X = 300
    button_bad_pos_Y = 400
    button_bad_width = 200
    button_bad_height = 40

    button_good_pos_X = 10
    button_good_pos_Y = 400
    button_good_width = 200
    button_good_height = 40

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
                team_color = BLUE if event.__dict__['joy'] == 0 else RED
                stop_music()
                music_is_playing = False

            # checks if a mouse is clicked
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # if the mouse is clicked on the button CONTINUE
                if button_continue_pos_X <= mouse[0] <= button_continue_pos_X + button_continue_width and \
                   button_continue_pos_Y <= mouse[1] <= button_continue_pos_Y + button_continue_height:
                    if not music_is_playing:
                        music_number_to_play = new_music(music_number_to_play)
                        music_is_playing = True
                    else:
                        continue_music()

                elif button_good_pos_X <= mouse[0] <= button_good_pos_X + button_good_width and \
                   button_good_pos_Y <= mouse[1] <= button_good_pos_Y + button_good_height:
                    # increment the score of the team that has pressed the button
                    if team_pressed_a_button == "blue":
                        blue_score += 1
                    elif team_pressed_a_button == "red":
                        red_score += 1
                    team_pressed_a_button = ""
                    team_color = BLACK

                elif button_bad_pos_X <= mouse[0] <= button_bad_pos_X + button_bad_width and \
                   button_bad_pos_Y <= mouse[1] <= button_bad_pos_Y + button_bad_height:
                    # increment the score of other team
                    if team_pressed_a_button == "blue":
                        red_score += 1
                    elif team_pressed_a_button == "red":
                        blue_score += 1
                    team_pressed_a_button = ""
                    team_color = BLACK

        #
        # DRAWING STEP
        #
        # First, clear the screen to white
        screen.fill(WHITE)
        textPrint.reset()

        textPrint.tprint(screen, f"Score team BLUE: {blue_score}", color=BLUE)
        textPrint.tprint(screen, f"Score team   RED: {red_score}", color=RED)

        textPrint.tprint(screen, "")
        textPrint.indent()
        if team_pressed_a_button != "":
            textPrint.tprint(screen, f"{team_pressed_a_button} team has got an answer !", color=team_color)

        draw_button(screen, text_continue, button_continue_pos_X, button_continue_pos_Y, button_continue_width, button_continue_height)
        draw_button(screen, text_bad, button_bad_pos_X, button_bad_pos_Y, button_bad_width, button_bad_height)
        draw_button(screen, text_good, button_good_pos_X, button_good_pos_Y, button_good_width, button_good_height)

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