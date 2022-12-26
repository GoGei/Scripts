import pyautogui
import pydirectinput
from time import sleep
from skillClickers.constants import SKILL_COORDS, SIT_COORDS, CAST_SKILL_COUNTER, SKILL_DELAY


def info_window():
    WITH_INFO = input('Do you want to use info?')
    if WITH_INFO:
        pyautogui.mouseInfo()


def skill_coords():
    coords = input('Do you want to specify skill coords as "x y"?')
    if coords:
        SKILL_COORDS = tuple(map(int, coords.split()))
        print(f'use {str(SKILL_COORDS)} coords')


def sit_coords():
    coords = input('Do you want to specify sit coords as "x y"?')
    if coords:
        SIT_COORDS = tuple(map(int, coords.split()))
        print(f'use {str(SIT_COORDS)} coords')


def cast_counter():
    try:
        CAST_SKILL_COUNTER = int(input('Do you want to specify number of casts?'))
    except ValueError as e:
        print(str(e))


def skill_delay():
    try:
        SKILL_DELAY = float(input('Do you want to specify skill delay?'))
    except ValueError as e:
        print(str(e))


def init():
    info_window()
    skill_coords()
    sit_coords()
    cast_counter()
    skill_delay()


def execute():
    start_delay = 5
    print(f'start at {start_delay} seconds')
    sleep(start_delay)
    print('run')
    t = CAST_SKILL_COUNTER
    slp = 57

    while True:
        # cast
        pydirectinput.moveTo(*SKILL_COORDS)
        sleep(0.1)
        for i in range(t):
            pydirectinput.click()
            if i <= t - 1:
                sleep(SKILL_DELAY)

        # delay
        sleep(0.5)

        # sit down
        pydirectinput.moveTo(*SIT_COORDS)
        pydirectinput.click()
        sleep(slp)

        # sit up
        pydirectinput.moveTo(*SIT_COORDS)
        pydirectinput.click()
        sleep(1.5)


if __name__ == '__main__':
    init()
    execute()
