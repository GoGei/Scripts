from difflib import SequenceMatcher


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


if __name__ == '__main__':
    print(similar('_^. 30 Бродячий волк.', 'Бродячий волк'))
