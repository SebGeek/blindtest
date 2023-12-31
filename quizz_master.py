# Button to associate the joysticks
#     Tell to hit the blue joystick, then the red joystick

# Button to start a game
#     Pronounce: "Get ready..."

# Start a music, manually (from Youtube music playlist)

# As soon as one team has fired, Beeper sound, wait 2 seconds then pronounce the fastest team name
#     stop the music, manually

# Button to click on the team who scored
#     Pronounce the score


import time
import hid
import sys
from PySide6 import QtWidgets
from PySide6.QtCore import QTimer
from functools import partial
import pygame
from gtts import gTTS
from io import BytesIO
import glob
import random
from resource.quizz_master_gui import Ui_Dialog


def set_volume(volume):
    """ Set the volume of the music playback, in percentage (0 to 100)
    """
    #print(f"set volume {volume}%")
    pygame.mixer.music.set_volume(volume / 100)

def play_music(filepath):
    pygame.mixer.music.load(filepath)
    #print("playing", filepath)
    try:
        pygame.mixer.music.play()
    except pygame.error:
        print(f"bad format (not MPEG audio): {filepath}")

def pronounce(text_to_pronounce):
    tts = gTTS(text=text_to_pronounce, lang='fr')
    mp3 = BytesIO()
    tts.write_to_fp(mp3)
    mp3.seek(0)
    pygame.mixer.music.load(mp3)
    pygame.mixer.music.play()

def pronounce_fastest_team(team):
    fastest_team_list = {"blue_team": "sounds/guns/crash-2-lightsaber-101soundboards.mp3", "red_team": "sounds/guns/buzzer.mp3",
                         "draw_game": "sounds/guns/Rifle-Supressed-Burst-Fire-A-www.fesliyanstudios.com.mp3"}
    play_music(fastest_team_list[team])

    time.sleep(2)

    fastest_team_list = {"blue_team": "Mayo est le plus rapide", "red_team": "Ketchup est le plus rapide", "draw_game": "Egalité parfaite !"}
    pronounce(fastest_team_list[team])

def pronounce_score(dict_score):
    if dict_score["red_team"] > dict_score["blue_team"]:
        text = f'Score {dict_score["red_team"]} à {dict_score["blue_team"]} pour Ketchup !'
    elif dict_score["red_team"] == dict_score["blue_team"]:
        text = f'Egalité, {dict_score["red_team"]} partout !'
    else:
        text = f'Score {dict_score["blue_team"]} à {dict_score["red_team"]} pour Mayo !'
    pronounce(text)


class MainWindow(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(f"Quizz Master")

        self.gamepad_blue = None
        self.gamepad_red = None
        self.game_is_running = True
        self.score = {"red_team": 0, "blue_team": 0}

        self.pushButton_blueteam_plus1.clicked.connect(partial(self.pushButton_blueteam_func, 1))
        self.pushButton_blueteam_plus3.clicked.connect(partial(self.pushButton_blueteam_func, 3))
        self.pushButton_blueteam_minus1.clicked.connect(partial(self.pushButton_blueteam_func, -1))
        self.pushButton_redteam_plus1.clicked.connect(partial(self.pushButton_redteam_func, 1))
        self.pushButton_redteam_plus3.clicked.connect(partial(self.pushButton_redteam_func, 3))
        self.pushButton_redteam_minus1.clicked.connect(partial(self.pushButton_redteam_func, -1))

        self.fastestTeam.setText("")

        pygame.init()
        pygame.mixer.init()
        set_volume(100)
        self.joystick_init()

        self.timer = QTimer(self)
        # noinspection PyUnresolvedReferences
        self.timer.timeout.connect(self.joystick_read)
        self.timer.start(10) # time in milliseconds

    def closeEvent(self, event):
        # GUI is closed by user
        self.timer.stop()
        pygame.quit()

    def pushButton_blueteam_func(self, value):
        self.score["blue_team"] += value
        self.ScoreBlue.setText(f'{self.score["blue_team"]}')
        pronounce_score(self.score)

    def pushButton_redteam_func(self, value):
        self.score["red_team"] += value
        self.ScoreRed.setText(f'{self.score["red_team"]}')
        pronounce_score(self.score)

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
                        self.fastestTeam.setStyleSheet(u"color: blue")
                        self.fastestTeam.setText("Mayo est le plus rapide")
                    elif red_fire and not blue_fire:
                        fastest_team = "red_team"
                        self.fastestTeam.setStyleSheet(u"color: red")
                        self.fastestTeam.setText("Ketchup est le plus rapide")
                    elif blue_fire and red_fire:
                        fastest_team = "draw_game"
                        self.fastestTeam.setStyleSheet(u"color: black")
                        self.fastestTeam.setText("Egalité parfaite ! (à 10 ms près)")
                    self.repaint()
                    pronounce_fastest_team(fastest_team)
                    time.sleep(4)
                    self.fastestTeam.setText("")
                    self.game_is_running = True
            else:
                print("ERROR in reading gamepads")

    def joystick_init(self):
        # for device in hid.enumerate():
        #     print(device)
        try:
            self.gamepad_blue = hid.device()
            self.gamepad_blue.open_path(b'\\\\?\\HID#VID_0583&PID_2060#6&24f58a1&1&0000#{4d1e55b2-f16f-11cf-88cb-001111000030}')
            self.gamepad_blue.set_nonblocking(True)

            self.gamepad_red = hid.device()
            self.gamepad_red.open_path(b'\\\\?\\HID#VID_0583&PID_2060#6&2b307203&0&0000#{4d1e55b2-f16f-11cf-88cb-001111000030}')
            self.gamepad_red.set_nonblocking(True)
        except OSError:
            print("ERROR: gampepads not found")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.processEvents()

    window = MainWindow()
    window.show()
    window.activateWindow()

    ret = app.exec()  # Blocking
    sys.exit(ret)
