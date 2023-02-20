import time
import winsound

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    time_elapsed = 0
    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}Alarm will sound in:{minutes_left:02d}:{seconds_left:02d}")
        if seconds_left == 0:
            winsound.PlaySound(sound='SystemExclamation',flags=winsound.SND_ALIAS)


minutes = int(input("how many minutes do you want to set: "))
seconds = int(input("how many seconds do you want to set: "))
total = minutes * 60 + seconds
alarm(total)

