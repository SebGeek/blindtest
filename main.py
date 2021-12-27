import pygame


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
    # Executed when app is loaded
    print("init pygame mixer")
    pygame.mixer.init()