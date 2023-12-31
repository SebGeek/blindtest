# Button to associate the joysticks
#     Tell to hit the blue joystick, then the red joystick

# Button to start a game
#     Pronounce: "Get ready..."

# Start a music, manually (from Youtube music playlist)

# As soon as one team has fired, Beeper sound, wait 2 seconds then pronounce the fastest team name
#     stop the music, manually

# Button to click on the team who scored
#     Pronounce the score

import hid
import sys
from PySide6 import QtWidgets
from PySide6.QtCore import QTimer
from functools import partial
from resource.quizz_master_gui import Ui_Dialog

# C:\Users\famil\PycharmProjects\venv\Scripts\pyside6-uic.exe resource/quizz_master_gui.ui -o resource/quizz_master_gui.py


import pygame
from gtts import gTTS
from io import BytesIO
import glob
import random

def set_volume(volume): # todo
    """ Set the volume of the music playback, in percentage (0 to 100)
    """
    print(f"set volume {volume}%")
    pygame.mixer.music.set_volume(volume / 100)

def play_buzzer():
    obj_buzz = pygame.mixer.Sound('sounds/guns/buzzer.mp3')
    obj_buzz.play(0)

def play_music(filepath):
    pygame.mixer.music.load(filepath)
    #print("playing", filepath)
    try:
        pygame.mixer.music.play()
    except pygame.error:
        print(f"bad format (not MPEG audio): {filepath}")

def play_gun_sound():
    sounds_guns_list = glob.glob("sounds/guns/*.mp3")
    play_music(random.choice(sounds_guns_list))

def play_burgerQuizzIntro():
    sounds_guns_list = glob.glob("sounds/BurgerQuizz/BurgerQuizzIntro.mp3")
    play_music(random.choice(sounds_guns_list))

def pronounce(text_to_pronounce):
    tts = gTTS(text=text_to_pronounce, lang='fr')
    mp3 = BytesIO()
    tts.write_to_fp(mp3)
    mp3.seek(0)
    pygame.mixer.music.load(mp3)
    pygame.mixer.music.play()

def pronounce_start():
    list_get_ready = ["A vos marques !", "Get ready... Go !", "Attention, c'est parti !"]
    pronounce(random.choice(list_get_ready))

def pronounce_fastest_team(team):
    play_gun_sound()
    fastest_team_list = {"blue_team": "Equipe bleue !", "red_team": "Equipe rouge !", "draw_game": "Egalité parfaite !"}
    pronounce(fastest_team_list[team])

def pronounce_score(dict_score):
    if dict_score["red_team"] > dict_score["blue_team"]:
        text = f'Score {dict_score["red_team"]} à {dict_score["blue_team"]} pour les rouges !'
    elif dict_score["red_team"] == dict_score["blue_team"]:
        text = f'Egalité, {dict_score["red_team"]} partout !'
    else:
        text = f'Score {dict_score["blue_team"]} à {dict_score["red_team"]} pour les bleus !'
    pronounce(text)


class MainWindow(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(f"Quizz Master")

        self.gamepad_blue = None
        self.gamepad_red = None
        self.game_is_running = False

        self.pushButton_start.clicked.connect(self.pushButton_start_func)
        self.pushButton_blueteam_plus1.clicked.connect(partial(self.pushButton_blueteam_func, 1))
        self.pushButton_blueteam_plus3.clicked.connect(partial(self.pushButton_blueteam_func, 3))
        self.pushButton_blueteam_minus1.clicked.connect(partial(self.pushButton_blueteam_func, -1))
        self.pushButton_redteam_plus1.clicked.connect(partial(self.pushButton_redteam_func, 1))
        self.pushButton_redteam_plus3.clicked.connect(partial(self.pushButton_redteam_func, 3))
        self.pushButton_redteam_minus1.clicked.connect(partial(self.pushButton_redteam_func, -1))

        pygame.init()
        pygame.mixer.init()
        self.joystick_init()

        self.timer = QTimer(self)
        # noinspection PyUnresolvedReferences
        self.timer.timeout.connect(self.joystick_read)
        self.timer.start(10) # time in milliseconds

    def closeEvent(self, event):
        # GUI is closed by user
        self.timer.stop()
        pygame.quit()

    def pushButton_start_func(self):
        #play_burgerQuizzIntro() todo
        pronounce_start()
        self.game_is_running = True

    @staticmethod
    def pushButton_blueteam_func(value):
        print(f"blue {value}")
        #self.ScoreBlue
        score = {"red_team": 2, "blue_team": 3}
        pronounce_score(score)

    @staticmethod
    def pushButton_redteam_func(value):
        print(f"red {value}")
        play_buzzer()

    def joystick_read(self):
        if self.game_is_running:
            report_blue = self.gamepad_blue.read(64)
            report_red  = self.gamepad_red.read(64)
            fastest_team = "none"
            if len(report_blue) > 2 and len(report_red) > 2:
                blue_fire = report_blue[2] != 0
                red_fire  = report_red[2] != 0
                if blue_fire or red_fire:
                    self.game_is_running = False
                    if blue_fire and not red_fire:
                        fastest_team = "blue_team"
                    elif red_fire and not blue_fire:
                        fastest_team = "red_team"
                    elif blue_fire and red_fire:
                        fastest_team = "draw_game"
            else:
                print("ERROR in reading gamepads")

            if fastest_team != "none":
                pronounce_fastest_team(fastest_team)

    def joystick_init(self):
        # for device in hid.enumerate():
        #     print(device)

        self.gamepad_blue = hid.device()
        self.gamepad_blue.open_path(b'\\\\?\\HID#VID_0583&PID_2060#6&24f58a1&1&0000#{4d1e55b2-f16f-11cf-88cb-001111000030}')
        self.gamepad_blue.set_nonblocking(True)

        self.gamepad_red = hid.device()
        self.gamepad_red.open_path(b'\\\\?\\HID#VID_0583&PID_2060#6&2b307203&0&0000#{4d1e55b2-f16f-11cf-88cb-001111000030}')
        self.gamepad_red.set_nonblocking(True)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.processEvents()

    window = MainWindow()
    window.show()
    window.activateWindow()

    ret = app.exec()  # Blocking
    sys.exit(ret)
