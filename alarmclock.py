import time, winsound, os


# time.sleep
# winsound.Beep(frequency, duration)
# os.system('cmd')   execute a command in system terminal; cls menas clear the input for windows system; clear for mac/linux

def play_sound():
    for i in range(3):
        # winsound.MessageBeep(-1)
        freq = 1000
        dur = 2000
        winsound.Beep(freq, dur)
        time.sleep(2)


def delay_time(unit):
    if unit == 1:
        time = int(input('How many hours before the alarm? '))
        delay = 60 * 60 * time
    elif unit == 2:
        time = int(input('How many minutes before the alarm? '))
        delay = 60 * time
    elif unit == 3:
        time = int(input('How many seconds before the alarm? '))
        delay = time
    elif unit == 4:
        hours = int(input('input hours: '))
        minutes = int(input('input minutes: '))
        seconds = int(input('input seconds: '))
        delay = 60 * 60 * hours + 60 * minutes + seconds
    else:
        try:
            os.system('cls')
        except:
            os.system('clear')
    return delay


if __name__ == '__main__':
    while True:
        unit = int(input('please input 1 for hours, 2 for minutes, 3 for seconds, and 4 for combination: '))
        delay = delay_time(unit)
        time.sleep(delay)
        play_sound()
