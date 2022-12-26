from time import sleep
from farmers.utils.keypresser import press_key
from skillClickers.constants import CAST_SKILL_COUNTER, SKILL_DELAY


if __name__ == '__main__':
    SKILL_BUTTON = '8'
    SIT_BUTTON = '7'

    start_delay = 5
    print(f'start at {start_delay} seconds')
    sleep(start_delay)
    print('run')
    t = CAST_SKILL_COUNTER
    slp = 57

    while True:
        # cast
        sleep(0.1)
        for i in range(t):
            press_key(SKILL_BUTTON)
            if i <= t - 1:
                sleep(SKILL_DELAY)

        # delay
        sleep(0.5)

        # sit down
        press_key(SIT_BUTTON)
        sleep(slp)

        # sit up
        press_key(SIT_BUTTON)
        sleep(1.5)
