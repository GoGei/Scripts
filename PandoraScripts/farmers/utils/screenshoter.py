import cv2
import pytesseract
import pyscreenshot as ImageGrab

from pathes import SCREEN_PATH

pytesseract.pytesseract.tesseract_cmd = r'F:/Applications/Tesseract-OCR/tesseract'
TARGET_NAME_PATH = f'{SCREEN_PATH}\\target_name.png'
TARGET_HP_PATH = f'{SCREEN_PATH}\\target_hp.png'
HERO_PATH = f'{SCREEN_PATH}\\hero.png'

TARGET_NAME_SCREEN_SHOOTER_BOX = (
    350,  # left X
    71,  # left Y
    480,  # right X
    86,  # right Y
)

HERO_SCREEN_SHOOTER_BOX = (
    177,  # left X
    95,  # left Y
    236,  # right X
    105,  # right Y
)

TARGET_HP_SCREEN_SHOOTER_BOX = (
    275,  # left X
    96,  # left Y
    475,  # right X
    105,  # right Y
)


def __save_image(coords, path):
    im = ImageGrab.grab(bbox=coords)
    im.save(path)


def __get_text_from_image(image_path):
    text = pytesseract.image_to_string(image_path, lang="rus")
    # text = pytesseract.image_to_string(image_path)
    return text


def get_text(coords, path):
    __save_image(coords, path)
    text = __get_text_from_image(path)
    return text.strip()


def get_image_color_pixels(coords, path):
    __save_image(coords, path)
    img = cv2.imread(path)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask1 = cv2.inRange(img_hsv, (0, 50, 20), (5, 255, 255))
    mask2 = cv2.inRange(img_hsv, (175, 50, 20), (180, 255, 255))
    mask = cv2.bitwise_or(mask1, mask2)

    pixels = cv2.countNonZero(mask)
    return pixels


HERO = {
    'coords': HERO_SCREEN_SHOOTER_BOX,
    'path': HERO_PATH,
}

TARGET_NAME = {
    'coords': TARGET_NAME_SCREEN_SHOOTER_BOX,
    'path': TARGET_NAME_PATH,
}

TARGET_HP = {
    'coords': TARGET_HP_SCREEN_SHOOTER_BOX,
    'path': TARGET_HP_PATH,
}
