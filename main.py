import pygame
import time


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

    pygame.joystick.init()

    # Count the joysticks the computer has
    joystick_count = pygame.joystick.get_count()
    if joystick_count == 0:
        print("Error, I didn't find any joysticks.")
    else:
        # Use joystick #0 and initialize it
        my_joystick = pygame.joystick.Joystick(0)
        my_joystick.init()

        button_count = my_joystick.get_numbuttons()
        print(button_count)

        while True:
            # This gets the position of the axis on the game controller
            # It returns a number between -1.0 and +1.0
            # horiz_axis_pos = my_joystick.get_axis(0)
            # vert_axis_pos = my_joystick.get_axis(1)
            # print(horiz_axis_pos, vert_axis_pos)

            pygame.event.pump()

            but_list = []
            for but_item in range(button_count):
                but_list.append(my_joystick.get_button(but_item))
            print(but_list)

            time.sleep(0.5)



    # print("init pygame mixer")
    # pygame.mixer.init()
    #
    # play_music("music/Musique_Noel.mp3")
    #
    # time.sleep(5)
    #
    # stop_music()