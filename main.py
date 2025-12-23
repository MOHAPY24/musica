from utils import play, background
from tables import *
import time

command = "&+!;0 "
skip_wait = False
preset = 0
if __name__ == "__main__":
    for i in command:
        if i == "":
            continue
        elif i == "&":
            skip_wait = True
            continue
        elif i == ";":
            try:
                preset = int(command[command.index(i)+1])
                continue
            except TypeError:
                preset = 0
                print("Invalid preset, resulting preset 0")
        elif i == ' ':
            time.sleep(1)
            continue
        elif command[command.index(i)-1] == ';':
            continue
            
        
        sound_path = f"media/{presettable[preset]}{signtable[i]}"
        play(sound_path, wait=not skip_wait)
        skip_wait = False

