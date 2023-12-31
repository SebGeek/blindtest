# Button to associate the joysticks
#     Tell to hit the blue joystick, then the red joystick

# Button to start a game
#     Pronounce: "Get ready..."

# Start a music, manually (from Youtube music playlist)

# As soon as one team has fired, Beeper sound, wait 2 seconds then pronounce the fastest team name
#     stop the music, manually

# Button to click on the team who scored
#     Pronounce the score


import sys
from PySide6 import QtWidgets
from functools import partial
from resource.quizz_master import Ui_Dialog

# C:\Users\famil\PycharmProjects\venv\Scripts\pyside6-uic.exe resource/quizz_master.ui -o resource/quizz_master.py


import time
import pygame
from gtts import gTTS
from io import BytesIO
import glob
import random

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
    time.sleep(2.5)

def play_burgerQuizzIntro():
    sounds_guns_list = glob.glob("sounds/BurgerQuizz/BurgerQuizzIntro.mp3")
    play_music(random.choice(sounds_guns_list))
    time.sleep(2.5)

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
    time.sleep(2)

def pronounce_fastest_team(team):
    play_gun_sound()
    fastest_team_list = {"blue_team": "Equipe bleue !", "red_team": "Equipe rouge !"}
    pronounce(fastest_team_list[team])
    time.sleep(1.5)

def pronounce_score(dict_score):
    if dict_score["red_team"] > dict_score["blue_team"]:
        text = f'Score {dict_score["red_team"]} à {dict_score["blue_team"]} pour les rouges !'
    elif dict_score["red_team"] == dict_score["blue_team"]:
        text = f'Egalité, {dict_score["red_team"]} partout !'
    else:
        text = f'Score {dict_score["blue_team"]} à {dict_score["red_team"]} pour les bleus !'
    pronounce(text)
    time.sleep(2.5)


class MainWindow(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton_start.clicked.connect(self.pushButton_start_func)
        self.pushButton_blueteam_plus1.clicked.connect(partial(self.pushButton_blueteam_func, 1))
        self.pushButton_blueteam_plus3.clicked.connect(partial(self.pushButton_blueteam_func, 3))
        self.pushButton_blueteam_minus1.clicked.connect(partial(self.pushButton_blueteam_func, -1))
        self.pushButton_redteam_plus1.clicked.connect(partial(self.pushButton_redteam_func, 1))
        self.pushButton_redteam_plus3.clicked.connect(partial(self.pushButton_redteam_func, 3))
        self.pushButton_redteam_minus1.clicked.connect(partial(self.pushButton_redteam_func, -1))

    def pushButton_start_func(self):
        print("start")
        play_burgerQuizzIntro()
        pronounce_start()

    def pushButton_blueteam_func(self, value):
        print(f"blue {value}")
        #self.ScoreBlue
        score = {"red_team": 2, "blue_team": 3}
        pronounce_score(score)

    def pushButton_redteam_func(self, value):
        print(f"red {value}")


if __name__ == '__main__':
    pygame.mixer.init()

    app = QtWidgets.QApplication(sys.argv)
    app.processEvents()

    window = MainWindow()
    window.show()
    window.activateWindow()

    ret = app.exec()  # Blocking
    sys.exit(ret)

    # pronounce_fastest_team("red_team")
