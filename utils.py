from mutagen.mp3 import MP3
# os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

# sys.stdout = open(os.devnull, "w")
# sys.stderr = open(os.devnull, "w")
import pygame
pygame.mixer.init()
background = False 

def play(sound_path, wait=True):
    sound = pygame.mixer.Sound(sound_path)
    sound.play()

    if wait:
        length = MP3(sound_path).info.length
        pygame.time.wait(int(length * 1000))