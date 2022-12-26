from farmers.utils.keypresser import press_key
from farmers.utils.screenshoter import get_text, TARGET_NAME, TARGET_HP, get_image_color_pixels
from farmers.utils.string_similarity import similar
from farmers.utils.names import banned_names, target_names


class Controller:
    TEST = False
    DMGS = []
    DMG_PIXELS = 10
    DEAD_PIXELS = 5

    @classmethod
    def is_killed(cls):
        pixels = get_image_color_pixels(**TARGET_HP)
        state = pixels <= cls.DEAD_PIXELS
        if cls.TEST:
            print('is killed state', state)
        return state

    @classmethod
    def attack(cls):
        pixels = get_image_color_pixels(**TARGET_HP)
        cls.DMGS.append(pixels)
        lst = cls.DMGS.copy()

        if len(lst) >= 2 and (lst[-2] - lst[-1]) <= cls.DMG_PIXELS:
            if cls.TEST:
                print('mass agr triggered')
            press_key('6')
            return

        press_key('F')
        return

    @classmethod
    def loc_target(cls):
        press_key('R')
        return

    @classmethod
    def get_target_name(cls):
        text = get_text(**TARGET_NAME)
        if cls.TEST:
            print(text)
        return text

    @classmethod
    def is_banned(cls, text):
        for name in banned_names:
            similarity = similar(text, name)
            if similarity >= 0.6:
                return True
        return False

    @classmethod
    def is_target(cls, text):
        for name in target_names:
            similarity = similar(text, name)
            if similarity >= 0.6:
                return True
        return False

    @classmethod
    def is_allowed_to_attack(cls, target_name):
        if not target_name:
            if cls.TEST:
                print('No target')
            return False
        elif cls.is_banned(target_name):
            if cls.TEST:
                print('SKIPPED')
            return False
        elif cls.is_target(target_name):
            if cls.TEST:
                print('TARGET')
            return True
        else:
            if cls.TEST:
                print('ELSE')
            return True
