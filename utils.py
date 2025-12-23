from mutagen.mp3 import MP3
# os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

# sys.stdout = open(os.devnull, "w")
# sys.stderr = open(os.devnull, "w")
import pygame
background = False 
def play(sound_path, wait=True, volume=100):
    try:
        pygame.mixer.init()
        sound = pygame.mixer.Sound(sound_path)
        sound.play()
        sound.set_volume(volume / 100)
        if wait:
            length = MP3(sound_path).info.length
            pygame.time.wait(int(length * 1000))
    except KeyboardInterrupt:
        quit(0)