import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

from aerforge.main import Forge
from aerforge.input import Input
from aerforge.gameobject import GameObject
from aerforge.error import ForgeError
from aerforge.shape import Rect, Circle
from aerforge.mixer import Mixer
from aerforge.text import Text
from aerforge.sprite import Sprite