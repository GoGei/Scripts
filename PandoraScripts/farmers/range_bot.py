from time import sleep
from farmers.utils.actions import Controller


if __name__ == '__main__':
    input('Ready to execute?')
    start_delay = 2
    print(f'start at {start_delay} seconds')
    sleep(start_delay)
    print('run')

    while True:
        # hero_state = Controller.get_hero_state()
        #
        # if not hero_state:
        #     print('LOW HP')
        #     Controller.trigger_sit()
        #     sleep(55)
        #     Controller.trigger_sit()
        #     print('Stand up')
        #     continue

        Controller.loc_target()
        name = Controller.get_target_name()
        is_allowed = Controller.is_allowed_to_attack(name)
        if is_allowed:
            while not Controller.is_killed():
                Controller.attack()
                sleep(1.5)
        Controller.DMGS.clear()
        sleep(0.5)
