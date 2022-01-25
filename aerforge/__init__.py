import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

import aerforge.shape as shape
import aerforge.color as color
import aerforge.math as math

from aerforge.main import Forge, init
from aerforge.input import Input
from aerforge.entity import Entity
from aerforge.error import ForgeError
from aerforge.mixer import Mixer
from aerforge.text import Text
from aerforge.sprite import Sprite
from aerforge.line import Line
from aerforge.animation import Animation
from aerforge.polygon import Polygon
from aerforge.build import Builder

import aerforge.scripts as scripts
import aerforge.prefabs as prefabs