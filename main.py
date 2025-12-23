import sys, os
from mutagen.mp3 import MP3
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

sys.stdout = open(os.devnull, "w")
sys.stderr = open(os.devnull, "w")
import pygame

matchtable = {
    "f1": "formula-1-radio-notification.mp3",
    "fnaf2": "fnaf-2-hallway-ambience.mp3",
    "ding": "ding-sound-effect_2.mp3",
    "raar": "raaar_FerSY7o.mp3",
    "bluetooth": "the-bluetooth-device-is-ready-to-pair.mp3"
}

signtable = {
    "!": matchtable["f1"],
    "?": matchtable["ding"],
    "-": matchtable["raar"],
    "+": matchtable["bluetooth"]
}
pygame.mixer.init()

def play(sound_path, wait=True):
    sound = pygame.mixer.Sound(sound_path)
    sound.play()

    if wait:
        length = MP3(sound_path).info.length
        pygame.time.wait(int(length * 1000))


command = "!&!&!&!&!&!&+&+++&+&--"
skip_wait = False

for i in command:
    if i == "&":
        skip_wait = True
        continue

    sound_path = f"media/{signtable[i]}"
    play(sound_path, wait=not skip_wait)
    skip_wait = False
