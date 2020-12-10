import functools
import random
import time
import os
from io import BytesIO

from PIL import Image


def mkdir(path):
    """ Создать новую папку или убедиться что она уже существует

    :param str path: желаеный путь до новой папки
    """
    if os.path.exists(path):
        return True
    elif os.path.isfile(path):
        return False
    try:
        os.mkdir(path=path)
        return True
    except FileExistsError:
        return False


def get_filename():
    filename = 'result_{}_{}.png'.format(int(time.time()), random.randint(1, 100))
    return filename
