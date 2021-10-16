import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

from aerforge.shape import *

from aerforge.vec2 import Vec2
from aerforge.color import Color
from aerforge.main import Forge, init
from aerforge.input import Input
from aerforge.gameobject import GameObject
from aerforge.error import ForgeError
from aerforge.mixer import Mixer
from aerforge.text import Text
from aerforge.sprite import Sprite
from aerforge.line import Line
from aerforge.animation import Animation